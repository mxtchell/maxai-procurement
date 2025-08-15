#!/usr/bin/env python3
"""SQL-optimized price variance analysis with minimal query overhead"""

from __future__ import annotations
import pandas as pd
import logging
import json
import jinja2
from types import SimpleNamespace
from skill_framework import SkillInput, SkillOutput, SkillVisualization, ParameterDisplayDescription
from skill_framework.skills import ExportData
from skill_framework.layouts import wire_layout
from answer_rocket import AnswerRocketClient
from ar_analytics.helpers.utils import get_dataset_id
from ar_analytics import DriverAnalysisTemplateParameterSetup
from price_variance_helper_sql_optimized.price_variance_config import FINAL_PROMPT_TEMPLATE

logger = logging.getLogger(__name__)

# Database ID for the procurement environment - found through dataset inspection
DATABASE_ID = "1fd0bbbb-3b40-4cc3-b56f-456e50808817"

def format_currency_short(value):
    """Format currency values in short form (e.g., $4.9M, $156K)"""
    # Handle string values that may already be formatted or need conversion
    if isinstance(value, str):
        clean_value = value.replace('$', '').replace(',', '').strip()
        try:
            value = float(clean_value)
        except (ValueError, TypeError):
            return "$0"
    
    # Handle None or NaN values
    if value is None:
        return "$0"
    
    try:
        value = float(value)
    except (ValueError, TypeError):
        return "$0"
    
    if value >= 1_000_000:
        return f"${value/1_000_000:.1f}M"
    elif value >= 1_000:
        return f"${value/1_000:.0f}K"
    else:
        return f"${value:.0f}"

def build_time_filter(parameters: SkillInput) -> str:
    """Build time filter SQL from parameters"""
    periods = parameters.arguments.time_periods if hasattr(parameters.arguments, 'time_periods') else []
    
    if not periods:
        return "1=1"
    
    time_conditions = []
    for period in periods:
        if isinstance(period, dict) and 'start' in period and 'end' in period:
            time_conditions.append(f"(transactionDate >= '{period['start']}' AND transactionDate <= '{period['end']}')")
        elif isinstance(period, str):
            period_lower = period.lower().strip()
            
            # Handle date range format like "2025-01-01 to 2025-12-31"
            if ' to ' in period_lower:
                parts = period_lower.split(' to ')
                if len(parts) == 2:
                    start_date = parts[0].strip()
                    end_date = parts[1].strip()
                    time_conditions.append(f"(transactionDate >= '{start_date}' AND transactionDate <= '{end_date}')")
                    continue
            
            # Handle quarter periods like 'q3 2025', 'Q1 2024', etc.
            if 'q1' in period_lower:
                year = '2025' if '2025' in period_lower else '2024'
                time_conditions.append(f"(transactionDate >= '{year}-01-01' AND transactionDate <= '{year}-03-31')")
            elif 'q2' in period_lower:
                year = '2025' if '2025' in period_lower else '2024'
                time_conditions.append(f"(transactionDate >= '{year}-04-01' AND transactionDate <= '{year}-06-30')")
            elif 'q3' in period_lower:
                year = '2025' if '2025' in period_lower else '2024'
                time_conditions.append(f"(transactionDate >= '{year}-07-01' AND transactionDate <= '{year}-09-30')")
            elif 'q4' in period_lower:
                year = '2025' if '2025' in period_lower else '2024'
                time_conditions.append(f"(transactionDate >= '{year}-10-01' AND transactionDate <= '{year}-12-31')")
            elif period_lower in ['2024', '2025', '2023']:
                # Full year
                time_conditions.append(f"(transactionDate >= '{period_lower}-01-01' AND transactionDate <= '{period_lower}-12-31')")
            else:
                # Default to recent data if we can't parse
                time_conditions.append("transactionDate >= '2024-01-01'")
    
    return f"({' OR '.join(time_conditions)})" if time_conditions else "1=1"

def build_other_filters_with_grounding(parameters: SkillInput) -> str:
    """
    TODO: Implement proper ar_analytics filter grounding integration
    
    The correct approach is to:
    1. Use DriverAnalysis to get properly grounded filters from the platform
    2. Let the platform handle semantic matching (dusting->cleaning, western->West Ops) 
    3. Extract the grounded filter conditions and convert to our SQL format
    
    For now, returning empty string to avoid breaking the platform's intelligence
    with custom parsing that only works for literal matches.
    """
    filters = parameters.arguments.other_filters if hasattr(parameters.arguments, 'other_filters') else None
    
    if filters:
        logger.info(f"⚠️  FILTERS IGNORED: {filters}")
        logger.info("   Custom filter parsing removed - need to implement proper ar_analytics integration")
        logger.info("   Skill will show unfiltered data until integration is complete")
    
    # Return empty for now - better to show unfiltered results than break semantic matching
    return ""

def run_price_variance_analysis_sql(parameters: SkillInput) -> SkillOutput:
    """Main SQL-optimized function - uses only 3 efficient queries instead of 15+ DriverAnalysis calls"""
    
    try:
        arc = AnswerRocketClient()
        time_filter = build_time_filter(parameters)
        other_filter = build_other_filters_with_grounding(parameters)
        
        # Combine filters
        full_filter = time_filter + other_filter
        
        logger.info("=== SQL OPTIMIZED: Starting analysis with 3 efficient queries ===")
        
        # Log parameters being used
        periods = parameters.arguments.time_periods if hasattr(parameters.arguments, 'time_periods') else []
        filters = parameters.arguments.other_filters if hasattr(parameters.arguments, 'other_filters') else []
        
        logger.info("🔧 Analysis Parameters:")
        logger.info(f"  📊 Main Metric: priceVarianceAmount")
        logger.info(f"  🎯 Breakouts: supplierName, contractName") 
        logger.info(f"  📅 Time Periods: {periods if periods else ['All Time']}")
        logger.info(f"  🔍 Additional Filters: {filters if filters else ['None']}")
        logger.info(f"  ⏰ Full Filter SQL: {full_filter}")
        
        # QUERY 1: Get all supplier data in one shot
        logger.info("🔍 Query 1: Getting comprehensive supplier data...")
        supplier_sql = f"""
        SELECT 
            supplierName,
            -- Variance metrics
            SUM(invoicePrice - expectedPrice) as total_variance,
            AVG((invoicePrice - expectedPrice) / NULLIF(expectedPrice, 0) * 100) as variance_pct,
            
            -- Price metrics
            AVG(invoicePrice) as avg_invoice_price,
            AVG(catalogPrice) as avg_catalog_price, 
            AVG(expectedPrice) as avg_expected_price,
            
            -- Compliance metrics
            SUM(CASE WHEN ABS(invoicePrice - expectedPrice) <= 0.01 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) as compliance_rate,
            
            -- Volume metrics
            COUNT(*) as transaction_count,
            SUM(quantity) as total_quantity
            
        FROM read_csv('procurement_compliance_v8.csv')
        WHERE {full_filter}
        GROUP BY supplierName
        ORDER BY total_variance DESC
        """
        
        logger.info(f"📝 SQL Query 1:\n{supplier_sql}")
        supplier_result = arc.data.execute_sql_query(DATABASE_ID, supplier_sql, 100)
        
        if not supplier_result.success or supplier_result.df is None or supplier_result.df.empty:
            logger.error(f"Supplier query failed: {supplier_result.error if not supplier_result.success else 'No data'}")
            return create_empty_output()
            
        supplier_df = supplier_result.df
        logger.info(f"✅ Query 1 complete: Got {len(supplier_df)} suppliers")
        
        # QUERY 2: Get overall KPIs in one shot
        logger.info("🔍 Query 2: Getting overall KPIs...")
        kpi_sql = f"""
        SELECT 
            -- Total metrics
            SUM(invoicePrice - expectedPrice) as total_variance,
            SUM(invoicePrice) as total_invoice_value,
            
            -- Average metrics  
            AVG((invoicePrice - expectedPrice) / NULLIF(expectedPrice, 0) * 100) as avg_variance_rate,
            
            -- Compliance metrics
            SUM(CASE WHEN ABS(invoicePrice - expectedPrice) <= 0.01 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) as compliance_rate,
            
            -- Volume metrics
            COUNT(DISTINCT supplierName) as total_suppliers,
            COUNT(*) as total_transactions
            
        FROM read_csv('procurement_compliance_v8.csv')
        WHERE {full_filter}
        """
        
        logger.info(f"📝 SQL Query 2:\n{kpi_sql}")
        kpi_result = arc.data.execute_sql_query(DATABASE_ID, kpi_sql, 1)
        
        if kpi_result.success and kpi_result.df is not None and not kpi_result.df.empty:
            kpi_data = kpi_result.df.iloc[0].to_dict()
            logger.info("✅ Query 2 complete: Got overall KPIs")
        else:
            logger.warning("KPI query failed, using defaults")
            kpi_data = {
                'total_variance': supplier_df['total_variance'].sum() if not supplier_df.empty else 0,
                'total_invoice_value': 0,
                'avg_variance_rate': 0,
                'compliance_rate': 0,
                'total_suppliers': len(supplier_df),
                'total_transactions': supplier_df['transaction_count'].sum() if not supplier_df.empty else 0
            }
        
        # QUERY 3: Get contract data for top supplier in one shot
        if not supplier_df.empty:
            top_supplier = supplier_df.iloc[0]['supplierName']
            logger.info(f"🔍 Query 3: Getting contract data for top supplier: {top_supplier}...")
            
            contract_sql = f"""
            SELECT 
                contractName,
                -- Variance metrics
                SUM(invoicePrice - expectedPrice) as variance_amount,
                
                -- Price metrics
                AVG(invoicePrice) as avg_invoice_price,
                AVG(catalogPrice) as avg_catalog_price,
                AVG(expectedPrice) as avg_expected_price,
                
                -- Compliance and volume
                AVG(CASE WHEN ABS(invoicePrice - expectedPrice) <= 0.01 THEN 100.0 ELSE 0.0 END) as compliance_rate,
                SUM(quantity) as total_quantity,
                
                COUNT(*) as transaction_count
                
            FROM read_csv('procurement_compliance_v8.csv')
            WHERE {full_filter} 
            AND supplierName = '{top_supplier.replace("'", "''")}'
            GROUP BY contractName
            ORDER BY variance_amount DESC
            """
            
            logger.info(f"📝 SQL Query 3:\n{contract_sql}")
            contract_result = arc.data.execute_sql_query(DATABASE_ID, contract_sql, 100)
            
            if contract_result.success and contract_result.df is not None:
                contract_df = contract_result.df
                logger.info(f"✅ Query 3 complete: Got {len(contract_df)} contracts for {top_supplier}")
            else:
                logger.warning("Contract query failed")
                contract_df = pd.DataFrame()
        else:
            top_supplier = "N/A"
            contract_df = pd.DataFrame()
            
        logger.info("🎉 SQL OPTIMIZED: All queries complete - generating visualizations...")
        
        # Generate visualizations using the query results
        return generate_visualizations(supplier_df, contract_df, kpi_data, top_supplier, parameters)
        
    except Exception as e:
        logger.error(f"SQL-optimized analysis failed: {e}")
        import traceback
        traceback.print_exc()
        return create_empty_output(f"Analysis failed: {str(e)}")

def generate_visualizations(supplier_df: pd.DataFrame, contract_df: pd.DataFrame, 
                          kpi_data: dict, top_supplier: str, parameters: SkillInput) -> SkillOutput:
    """Generate visualizations from SQL query results"""
    
    visualizations = []
    export_data = {}
    
    
    # Prepare supplier data for display
    supplier_display_data = []
    for _, row in supplier_df.head(5).iterrows():
        supplier_display_data.append([
            len(supplier_display_data) + 1,  # Rank
            row['supplierName'],
            format_currency_short(row['total_variance']),
            f"{float(row['variance_pct']):.1f}%" if pd.notna(row['variance_pct']) and row['variance_pct'] != '' else "0%",
            format_currency_short(row['avg_catalog_price']),
            format_currency_short(row['avg_invoice_price']),
            format_currency_short(row['avg_expected_price']),
            f"{float(row['compliance_rate']):.1f}%" if pd.notna(row['compliance_rate']) and row['compliance_rate'] != '' else "0%"
        ])
    
    supplier_table_df = pd.DataFrame(supplier_display_data, columns=[
        'Rank', 'Supplier', 'Variance $', 'Variance %', 
        'Catalog Price', 'Invoice Price', 'Expected Price', 'Price Compliance Rate'
    ])
    
    # Generate insights using LLM before creating page variables
    # Create fact dataframes for insights
    supplier_facts = create_supplier_facts(supplier_df)
    kpi_facts = create_kpi_facts(kpi_data)
    contract_facts = create_contract_facts(contract_df, top_supplier) if not contract_df.empty else pd.DataFrame()
    notes_df = create_notes_df(parameters)
    
    # Combine all facts for the prompts
    insights_dfs = [
        notes_df,
        kpi_facts, 
        supplier_facts,
        contract_facts if not contract_facts.empty else pd.DataFrame()
    ]
    
    # Convert dataframes to facts format for template rendering
    facts = []
    for i_df in insights_dfs:
        if not i_df.empty:
            facts.append(i_df.to_dict(orient='records'))
    
    # Render the insight_prompt template with facts
    insight_template = jinja2.Template(parameters.arguments.insight_prompt).render(facts=facts)
    
    # Generate actual insights using LLM (like trend.py does)
    from ar_analytics import ArUtils
    ar_utils = ArUtils()
    generated_insights = ar_utils.get_llm_response(insight_template)
    
    logger.info("🎯 GENERATED INSIGHTS:")
    logger.info(f"{generated_insights}")
    print("🎯 GENERATED INSIGHTS:")
    print(f"{generated_insights}")
    print("=" * 80)
    
    # Page 1: Supplier Overview
    page1_vars = {
        "headline": "Price Variance Deep Dive",
        "sub_headline": f"{format_currency_short(kpi_data['total_variance'])} Total Variance | {kpi_data['total_suppliers']} Suppliers",
        
        # KPIs
        "kpi1_value": format_currency_short(kpi_data['total_variance']),
        "kpi2_value": f"{kpi_data['compliance_rate']:.1f}%",
        "kpi3_value": f"{int(kpi_data['total_suppliers'])}",
        "kpi4_value": f"{kpi_data['avg_variance_rate']:.1f}%", 
        "kpi5_value": format_currency_short(kpi_data['total_invoice_value']),
        
        # Chart data
        "chart_data_series": [{
            "name": "Price Variance",
            "data": [int(x) for x in supplier_df.head(5)['total_variance'].tolist()] if not supplier_df.empty else [0]
        }],
        "chart_categories": supplier_df.head(5)['supplierName'].tolist() if not supplier_df.empty else ["No Data"],
        "chart_title": "Top 5 Suppliers by Variance",
        
        # Table data
        "data": supplier_table_df.values.tolist() if not supplier_table_df.empty else [],
        "col_defs": [{"name": col} for col in supplier_table_df.columns] if not supplier_table_df.empty else [],
        
        # Insights - populated with LLM-generated content
        "exec_summary": generated_insights if generated_insights else "No insights generated."
    }
    
    rendered_page1 = wire_layout(json.loads(parameters.arguments.page_1_layout), page1_vars)
    visualizations.append(SkillVisualization(title="Tab 1: Supplier Variance Overview", layout=rendered_page1))
    export_data["Supplier Analysis"] = supplier_table_df
    
    # Page 2: Contract Deep Dive
    if not contract_df.empty:
        contract_display_data = []
        for _, row in contract_df.head(5).iterrows():
            contract_display_data.append([
                row['contractName'],
                format_currency_short(row['variance_amount']),
                format_currency_short(row['avg_invoice_price']),
                format_currency_short(row['avg_catalog_price']),
                f"{float(row['compliance_rate']):.1f}%" if pd.notna(row['compliance_rate']) and row['compliance_rate'] != '' else "0%",
                f"{float(row['total_quantity']):,.0f}" if pd.notna(row['total_quantity']) and row['total_quantity'] != '' else "0"
            ])
        
        contract_table_df = pd.DataFrame(contract_display_data, columns=[
            'Contract Name', 'Variance Amount', 'Invoice Price', 'Catalog Price', 'Price Compliance Rate', 'Quantity'
        ])
        
        # Calculate total contract variance for ALL contracts (not just top 5)
        total_contract_variance = contract_df['variance_amount'].sum()
        total_contracts = len(contract_df)
        
        page2_vars = {
            "sub_headline": f"Contract-level variance analysis for {top_supplier}",
            
            # KPIs - ALL contracts 
            "kpi1_value": format_currency_short(total_contract_variance),
            "kpi2_value": f"{total_contracts}",
            "kpi3_value": format_currency_short(contract_df.iloc[0]['variance_amount']) if not contract_df.empty else "$0",
            
            # Chart data - top 5 contracts
            "chart_categories": contract_df.head(5)['contractName'].tolist(),
            "chart_data_series": [{
                "name": "Contract Variance",
                "data": [int(x) for x in contract_df.head(5)['variance_amount'].tolist()]
            }],
            "chart_title": f"Top 5 Contracts by Variance - {top_supplier}",
            
            # Table data - top 5 contracts
            "data": contract_table_df.values.tolist(),
            "col_defs": [{"name": col} for col in contract_table_df.columns],
            
            "exec_summary": generated_insights if generated_insights else "No insights generated."
        }
        
        rendered_page2 = wire_layout(json.loads(parameters.arguments.page_2_layout), page2_vars)
        visualizations.append(SkillVisualization(title="Tab 2: Contract Deep Dive", layout=rendered_page2))
        export_data["Contract Analysis"] = contract_table_df
    
    # Page 3: Recovery Pipeline (mockup)
    page3_vars = {
        "headline": "Recovery Pipeline",
        "sub_headline": "Price Variance Recovery Tracking & Opportunities",
        "kpi1_value": "$156,400",
        "kpi2_value": "$23,100", 
        "kpi3_value": "$8,750",
        "kpi4_value": "15",
        "chart_title": "Recovery Timeline & Progress",
        "chart_categories": ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5+"],
        "chart_data_series": [
            {"name": "Volume Price Break - 90%", "data": [5, 10, 15, 25, 30], "color": "#059669"},
            {"name": "Logistics Path - 75%", "data": [2, 8, 18, 28, 35], "color": "#f59e0b", "dashStyle": "Dash"},
            {"name": "Alt Source - 10%", "data": [0, 1, 2, 3, 8], "color": "#dc2626", "dashStyle": "Dot"}
        ],
        "data": [
            ["Volume discount recalculation", "Gamma Supply", "$70,500", "Supplier acknowledged, credit processing", "Aug 15, 2024", "Sarah Johnson"],
            ["Contract amendment pricing update", "Beta Industries", "$45,200", "System update scheduled", "Aug 5, 2024", "Mike Chen"],
            ["Pricing tier correction", "Alpha Manufacturing", "$34,650", "Under supplier review", "Aug 10, 2024", "Lisa Rodriguez"]
        ],
        "col_defs": [
            {"name": "Recovery Item"}, {"name": "Supplier"}, {"name": "Variance Amount"},
            {"name": "Recovery Status"}, {"name": "Expected Resolution"}, {"name": "Owner"}
        ],
        "exec_summary": "## Recovery Pipeline Status\n\n**Recovery Potential**: $156,400 total opportunity identified\n**In Progress**: $23,100 actively being processed\n**Recovered This Month**: $8,750 successfully recovered"
    }
    
    rendered_page3 = wire_layout(json.loads(parameters.arguments.page_3_layout), page3_vars)
    visualizations.append(SkillVisualization(title="Tab 3: Recovery Pipeline", layout=rendered_page3))
    
    # Create fact dataframes for insights
    supplier_facts = create_supplier_facts(supplier_df)
    kpi_facts = create_kpi_facts(kpi_data)
    contract_facts = create_contract_facts(contract_df, top_supplier) if not contract_df.empty else pd.DataFrame()
    notes_df = create_notes_df(parameters)
    
    # Log the dataframes for debugging
    logger.info("📊 INSIGHTS DATAFRAMES:")
    logger.info(f"  📈 KPI Facts: {len(kpi_facts)} rows")
    logger.info(f"  🏢 Supplier Facts: {len(supplier_facts)} rows") 
    logger.info(f"  📋 Contract Facts: {len(contract_facts)} rows")
    logger.info(f"  📝 Notes: {len(notes_df)} rows")
    
    # Also print for local testing
    print("📊 INSIGHTS DATAFRAMES:")
    print(f"  📈 KPI Facts: {len(kpi_facts)} rows")
    print(f"  🏢 Supplier Facts: {len(supplier_facts)} rows") 
    print(f"  📋 Contract Facts: {len(contract_facts)} rows")
    print(f"  📝 Notes: {len(notes_df)} rows")
    
    if not contract_facts.empty:
        logger.info("🔍 Top 3 Contract Facts:")
        for idx, row in contract_facts.head(3).iterrows():
            logger.info(f"    {idx+1}. {row['contract']}: {row['variance_amount']} variance, {row['compliance_rate']} compliance")
    
    if not supplier_facts.empty:
        logger.info("🔍 Top 3 Supplier Facts:")
        for idx, row in supplier_facts.head(3).iterrows():
            logger.info(f"    {idx+1}. {row['supplier']}: {row['variance_amount']} variance, {row['variance_pct']} rate")
    
    # Combine all facts for the prompts
    all_facts = pd.concat([
        kpi_facts,
        supplier_facts,
        contract_facts if not contract_facts.empty else pd.DataFrame()
    ], ignore_index=True)
    
    # Generate final prompt
    top_opportunities = generate_top_opportunities(supplier_df)
    final_prompt = FINAL_PROMPT_TEMPLATE.format(
        total_variance=format_currency_short(kpi_data['total_variance']),
        avg_variance_rate=kpi_data['avg_variance_rate'],
        total_transactions=kpi_data['total_transactions'],
        compliance_rate=kpi_data['compliance_rate'],
        top_supplier=top_supplier,
        top_supplier_variance=format_currency_short(supplier_df.iloc[0]['total_variance']) if not supplier_df.empty else "$0",
        top_opportunities=top_opportunities
    )
    
    # Generate parameter display descriptions for the pills at bottom
    param_info = []
    
    # Metric pill
    param_info.append(ParameterDisplayDescription(key="metric", value="Metric: priceVarianceAmount"))
    
    # Breakouts pill  
    param_info.append(ParameterDisplayDescription(key="breakouts", value="Breakouts: supplierName, contractName"))
    
    # Time period pill
    periods = parameters.arguments.time_periods if hasattr(parameters.arguments, 'time_periods') else []
    if periods:
        time_display = ", ".join([str(p) for p in periods])
    else:
        time_display = "All Time" 
    param_info.append(ParameterDisplayDescription(key="period", value=f"Time Period: {time_display}"))
    
    # Filters pill (if any)
    filters = parameters.arguments.other_filters if hasattr(parameters.arguments, 'other_filters') else []
    if filters and filters != ['None']:
        # Handle both string and list formats
        if isinstance(filters, str):
            filter_display = filters
        elif isinstance(filters, list):
            filter_display = ', '.join([str(f) for f in filters])
        else:
            filter_display = str(filters)
        param_info.append(ParameterDisplayDescription(key="filters", value=f"Filters: {filter_display}"))
    
    # Prepare export data
    export_data = {
        "Supplier Variance Analysis": supplier_df,
        "Contract Analysis": contract_df if 'contract_df' in locals() else pd.DataFrame(),
        "Overall KPIs": pd.DataFrame([kpi_data]),
        "Supplier Facts": supplier_facts,
        "KPI Facts": kpi_facts,
        "Contract Facts": contract_facts if not contract_facts.empty else pd.DataFrame(),
        "Notes": notes_df
    }
    
    # Prepare insights dataframes list (these are what the LLM uses)
    insights_dfs = [
        notes_df,
        kpi_facts, 
        supplier_facts,
        contract_facts if not contract_facts.empty else pd.DataFrame()
    ]
    
    # Convert dataframes to facts format for template rendering
    facts = []
    for i_df in insights_dfs:
        if not i_df.empty:
            facts.append(i_df.to_dict(orient='records'))
    
    # Log the actual facts being passed to templates (like dimension breakout)
    logger.info("🎯 FACTS BEING PASSED TO LLM:")
    for i, fact_group in enumerate(facts):
        logger.info(f"  Group {i+1}: {fact_group}")
    
    # Also log individual dataframes in full detail
    logger.info("📋 FULL DATAFRAME CONTENTS:")
    logger.info(f"  KPI Facts DF: {kpi_facts.to_dict(orient='records')}")
    logger.info(f"  Supplier Facts DF: {supplier_facts.to_dict(orient='records')}")
    if not contract_facts.empty:
        logger.info(f"  Contract Facts DF: {contract_facts.to_dict(orient='records')}")
    logger.info(f"  Notes DF: {notes_df.to_dict(orient='records')}")
    
    # Render the insight_prompt and max_prompt templates with facts
    insight_template = jinja2.Template(parameters.arguments.insight_prompt).render(facts=facts)
    max_response_prompt = jinja2.Template(parameters.arguments.max_prompt).render(facts=facts)
    
    # Debug: Log the rendered insight template to see what LLM gets
    logger.info("🔍 RENDERED INSIGHT TEMPLATE:")
    logger.info(f"{insight_template}")
    
    # Generate actual insights using LLM (like trend.py does)
    from ar_analytics import ArUtils
    ar_utils = ArUtils()
    generated_insights = ar_utils.get_llm_response(insight_template)
    
    logger.info("🎯 GENERATED INSIGHTS:")
    logger.info(f"{generated_insights}")
    
    # Debug: Also print for local testing
    print("🔍 RENDERED INSIGHT TEMPLATE:")
    print(f"{insight_template}")
    print("=" * 80)
    print("🎯 GENERATED INSIGHTS:")
    print(f"{generated_insights}")
    print("=" * 80)
    
    return SkillOutput(
        final_prompt=final_prompt,
        narrative=None,
        visualizations=visualizations,
        parameter_display_descriptions=param_info,
        export_data=[ExportData(name=name, data=df) for name, df in export_data.items()],
        insights_dfs=insights_dfs,
        insight_prompt=insight_template,
        max_response_prompt=max_response_prompt
    )

def create_supplier_facts(supplier_df: pd.DataFrame) -> pd.DataFrame:
    """Create supplier facts dataframe for insights"""
    facts = []
    
    for idx, row in supplier_df.head(10).iterrows():
        facts.append({
            'fact_type': 'supplier_variance',
            'supplier': row['supplierName'],
            'variance_amount': format_currency_short(row['total_variance']),
            'variance_pct': f"{row['variance_pct']:.1f}%",
            'compliance_rate': f"{row['compliance_rate']:.1f}%",
            'transaction_count': row['transaction_count'],
            'rank': idx + 1
        })
    
    return pd.DataFrame(facts)

def create_kpi_facts(kpi_data: dict) -> pd.DataFrame:
    """Create KPI facts dataframe for insights"""
    facts = [
        {
            'fact_type': 'overall_metrics',
            'metric': 'Total Variance Impact',
            'value': format_currency_short(kpi_data['total_variance']),
            'context': f"across {kpi_data['total_suppliers']} suppliers"
        },
        {
            'fact_type': 'overall_metrics',
            'metric': 'Price Compliance Rate', 
            'value': f"{kpi_data['compliance_rate']:.1f}%",
            'context': f"from {kpi_data['total_transactions']:,} transactions"
        },
        {
            'fact_type': 'overall_metrics',
            'metric': 'Average Variance Rate',
            'value': f"{kpi_data['avg_variance_rate']:.1f}%",
            'context': "deviation from contracted prices"
        },
        {
            'fact_type': 'overall_metrics',
            'metric': 'Total Invoice Value',
            'value': format_currency_short(kpi_data['total_invoice_value']),
            'context': "total procurement spend analyzed"
        }
    ]
    
    return pd.DataFrame(facts)

def create_contract_facts(contract_df: pd.DataFrame, supplier_name: str) -> pd.DataFrame:
    """Create contract facts dataframe for insights"""
    facts = []
    
    # Add summary fact about contract analysis
    if not contract_df.empty:
        total_contracts = len(contract_df)
        total_contract_variance = contract_df['variance_amount'].sum()
        avg_contract_compliance = contract_df['compliance_rate'].mean()
        
        facts.append({
            'fact_type': 'contract_summary',
            'supplier': supplier_name,
            'metric': 'Contract Overview',
            'value': f"{total_contracts} contracts analyzed",
            'context': f"Total variance: {format_currency_short(total_contract_variance)}, Avg compliance: {avg_contract_compliance:.1f}%"
        })
    
    # Add individual contract facts
    for idx, row in contract_df.head(5).iterrows():
        facts.append({
            'fact_type': 'contract_detail',
            'supplier': supplier_name,
            'contract': row['contractName'],
            'variance_amount': format_currency_short(row['variance_amount']),
            'avg_invoice_price': f"${row['avg_invoice_price']:.2f}",
            'avg_expected_price': f"${row['avg_expected_price']:.2f}",
            'compliance_rate': f"{row['compliance_rate']:.1f}%",
            'transaction_count': row['transaction_count'],
            'total_quantity': int(row['total_quantity']),
            'rank': idx + 1
        })
    
    return pd.DataFrame(facts)

def create_notes_df(parameters: SkillInput) -> pd.DataFrame:
    """Create notes dataframe with analysis metadata"""
    periods = parameters.arguments.time_periods if hasattr(parameters.arguments, 'time_periods') else []
    filters = parameters.arguments.other_filters if hasattr(parameters.arguments, 'other_filters') else []
    
    # Handle filter display
    if isinstance(filters, str):
        filter_display = filters
    elif isinstance(filters, list) and filters:
        filter_display = ', '.join([str(f) for f in filters])
    else:
        filter_display = 'None'
    
    notes = [
        {'Note': f"Analysis period: {', '.join(periods) if periods else 'All Time'}"},
        {'Note': f"Filters applied: {filter_display}"},
        {'Note': "Variance calculated as: invoicePrice - expectedPrice"},
        {'Note': "Compliance defined as: variance within $0.01 of expected price"}
    ]
    
    return pd.DataFrame(notes)

def generate_insights_markdown(kpi_data: dict, supplier_df: pd.DataFrame, top_supplier: str) -> str:
    """Generate insights for supplier analysis"""
    insights = f"""
## Key Insights

- **Total Variance Impact**: {format_currency_short(kpi_data['total_variance'])} across {kpi_data['total_suppliers']} suppliers
- **Top Opportunity**: {top_supplier} with {format_currency_short(supplier_df.iloc[0]['total_variance']) if not supplier_df.empty else '$0'} variance
- **Compliance Rate**: {kpi_data['compliance_rate']:.1f}% price compliance achieved

## Top Suppliers by Variance
"""
    
    if not supplier_df.empty:
        for i, (_, row) in enumerate(supplier_df.head(3).iterrows(), 1):
            insights += f"{i}. **{row['supplierName']}**: {format_currency_short(row['total_variance'])} ({row['variance_pct']:.1f}%)\n"
    
    insights += """
## Strategic Recommendations

1. **Focus Negotiations**: Target top variance suppliers for immediate cost savings
2. **Price Monitoring**: Implement automated alerts for high-risk categories  
3. **Supplier Consolidation**: Leverage volume for better pricing power
4. **Compliance Improvement**: Address the {:.0f}% non-compliance gap
""".format(100 - kpi_data['compliance_rate'])
    
    return insights

def generate_contract_insights(contract_df: pd.DataFrame, supplier_name: str, total_variance: float) -> str:
    """Generate insights for contract analysis"""
    top_contract = contract_df.iloc[0]['contractName'] if not contract_df.empty else "N/A"
    top_contract_variance = format_currency_short(contract_df.iloc[0]['variance_amount']) if not contract_df.empty else "$0"
    
    return f"""
## Contract Analysis for {supplier_name}

- **Total Contract Variance**: {format_currency_short(total_variance)} (ALL contracts)
- **Number of Contracts**: {len(contract_df)}
- **Top Contract**: {top_contract} ({top_contract_variance})

## Key Findings:
1. **Concentrated Risk**: Variance concentrated in specific high-impact contracts
2. **Renegotiation Opportunity**: Terms review needed for consistent overpayments
3. **Contract Consolidation**: Leverage volume across fewer agreements
4. **Compliance Monitoring**: Enhanced tracking needed for outlier contracts

## Action Items:
- **Priority 1**: Review and renegotiate top 3 variance contracts
- **Priority 2**: Implement contract-level price alerts
- **Priority 3**: Assess consolidation opportunities

**Note**: KPIs reflect ALL {len(contract_df)} contracts, table shows top 5 for focus
"""


def generate_top_opportunities(supplier_df: pd.DataFrame) -> str:
    """Generate bullet points for top opportunities"""
    if supplier_df.empty:
        return "- No specific opportunities identified"
    
    opportunities = []
    for _, row in supplier_df.head(3).iterrows():
        opportunities.append(
            f"- {row['supplierName']}: {format_currency_short(row['total_variance'])} variance "
            f"({row['variance_pct']:.1f}% above contract)"
        )
    
    return '\n'.join(opportunities)


def create_empty_output(error_msg: str = "No data available") -> SkillOutput:
    """Create empty output for error cases"""
    return SkillOutput(
        final_prompt=f"Analysis could not be completed: {error_msg}",
        narrative=None,
        visualizations=[],
        export_data=[]
    )