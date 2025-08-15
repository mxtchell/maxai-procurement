from __future__ import annotations
from skill_framework import skill, SkillParameter, SkillInput, SkillOutput
from price_variance_helper_sql_optimized.price_variance_config import FINAL_PROMPT_TEMPLATE
from price_variance_helper_sql_optimized.price_variance_functionality_sql import run_price_variance_analysis_sql
from price_variance_helper_sql_optimized.price_variance_layouts import price_variance_layouts, PAGES
from ar_analytics.defaults import default_table_layout

@skill(
    name="Price Variance Deep Dive",
    llm_name="price_variance_deep_dive",
    description="Analyzes procurement price variance to identify cost savings opportunities by comparing actual prices against contracted prices across suppliers and contracts",
    capabilities="Shows total variance impact, compliance rates, and top variance opportunities by supplier. Provides detailed contract-level analysis for highest impact suppliers. Calculates savings potential and tracks compliance metrics over time.",
    limitations="Requires invoicePrice, expectedPrice, and priceVarianceAmount fields. Analysis limited to available transaction data. Does not perform root cause analysis of variances.",
    example_questions="What are my top price variance opportunities ranked by potential savings? Which suppliers have the highest variance from contracted prices? Show me price compliance trends by category. What contracts are driving the most leakage?",
    parameter_guidance="Select time periods to analyze specific months, quarters, or years. Filter by supplier to focus on specific vendor performance. Leave filters blank for comprehensive analysis across all data.",
    parameters=[
        SkillParameter(
            name="time_periods",
            constrained_to="date_filter",
            is_multi=True,
            description="Time periods in format 'q2 2023', '2021', 'jan 2023', 'mat nov 2022', 'ytd', or '<no_period_provided>'. Handles relative periods using today's date."
        ),
        SkillParameter(
            name="other_filters",
            constrained_to="filters",
            description="Additional filters like supplier, category, contract, etc."
        ),
        SkillParameter(
            name="max_prompt",
            parameter_type="prompt",
            description="Maximum response prompt for the analysis",
            default_value="Answer user question in 30 words or less using following facts:\n{{facts}}"
        ),
        SkillParameter(
            name="insight_prompt",
            parameter_type="prompt", 
            description="Prompt for generating insights from the price variance data",
            default_value="""Write a short headline followed by a 60 word or less paragraph about using facts below.
Use the structure from the price variance examples below to learn how I typically write summary.
Base your summary solely on the provided facts, avoiding assumptions or judgments.
Ensure clarity and accuracy.
Use markdown formatting for a structured and clear presentation.

###
Please use the following as an example of good insights for price variance analysis:

Example 1:
Facts:
[{'title': 'Supplier Facts', 'facts': [{'supplier': 'EcoBox Packaging', 'variance': '$491K', 'variance_pct': '12.5%', 'compliance_rate': '58.2%'}, {'supplier': 'Elite Source', 'variance': '$428K', 'variance_pct': '11.8%', 'compliance_rate': '62.1%'}]}, {'title': 'Contract Facts', 'facts': [{'contract': 'Service Level Agreement #11', 'variance': '$64K', 'supplier': 'EcoBox Packaging'}]}, {'title': 'Overall Facts', 'facts': [{'total_variance': '$6.2M', 'suppliers': 20, 'compliance_rate': '60.7%', 'transactions': 45680}]}]

Summary:
## Price Variance Analysis ##
**Variance Overview:**
Total price variance of $6.2M identified across 20 suppliers with 60.7% price compliance rate, representing significant cost recovery opportunity.

**Top Opportunities:**
EcoBox Packaging leads with $491K variance (12.5% above contract), followed by Elite Source at $428K (11.8%). Low compliance rates indicate systematic pricing issues requiring immediate supplier engagement.

**Key Drivers:**
Service Level Agreement #11 represents the highest single contract variance at $64K. Focus negotiations on top variance suppliers for immediate cost savings and compliance improvement.

###

Facts:
{{facts}}

Summary:"""
        ),
        SkillParameter(
            name="final_prompt_template",
            parameter_type="prompt",
            description="Template for generating final insights and recommendations",
            default_value=FINAL_PROMPT_TEMPLATE
        ),
        SkillParameter(
            name="page_1_layout",
            parameter_type="visualization",
            description="Layout for Tab 1 - Supplier Variance Overview",
            default_value=price_variance_layouts.get(PAGES[0])
        ),
        SkillParameter(
            name="page_2_layout", 
            parameter_type="visualization",
            description="Layout for Tab 2 - Contract Deep Dive",
            default_value=price_variance_layouts.get(PAGES[1])
        ),
        SkillParameter(
            name="page_3_layout",
            parameter_type="visualization", 
            description="Layout for Tab 3 - Recovery Pipeline",
            default_value=price_variance_layouts.get(PAGES[2])
        )
    ]
)
def price_variance_deep_dive(parameters: SkillInput) -> SkillOutput:
    """
    Price Variance Deep Dive Analysis skill
    
    Analyzes procurement data to identify price variance opportunities,
    showing top suppliers and contracts with savings potential.
    """
    return run_price_variance_analysis_sql(parameters)

if __name__ == '__main__':
    # Test the skill with mock input
    try:
        print("Testing Price Variance Deep Dive skill...")
        # Test without filters (filters will be ignored for now)
        mock_input = price_variance_deep_dive.create_input(
            arguments={
                'time_periods': ['q3 2025'],
                'other_filters': "operatingUnit: western"  # This should find "West Ops" with proper grounding
            }
        )
        print("Mock input created successfully")
        
        # This will fail at data retrieval but we can test the structure
        output = price_variance_deep_dive(mock_input)
        print(f"Skill executed - Final prompt: {output.final_prompt[:100]}...")
        print(f"Visualizations: {len(output.visualizations)}")
        if output.visualizations:
            print(f"First visualization title: {output.visualizations[0].title}")
    except Exception as e:
        print(f"Test failed with error: {str(e)}")
        import traceback
        traceback.print_exc()