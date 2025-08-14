# HTML Templates for Price Variance Deep Dive Analysis

# Final prompt template
FINAL_PROMPT_TEMPLATE = """Based on the price variance analysis:

**Key Findings:**
- Total variance impact of {total_variance} indicates opportunities for cost savings through improved price compliance
- Average variance rate of {avg_variance_rate:.1f}% across {total_transactions:,} transactions
- Price compliance rate stands at {compliance_rate:.1f}%
- Top supplier {top_supplier} accounts for {top_supplier_variance} in variance

**Top Opportunities:**
{top_opportunities}

**Recommendations:**
1. Focus negotiation efforts on suppliers with highest variance impact
2. Review contracts with consistent overpayments for renegotiation opportunities
3. Implement automated price compliance alerts for high-variance categories
4. Consider consolidating spend with compliant suppliers"""

# Main visualization layout with tabs
PRICE_VARIANCE_LAYOUT = """
<div style="width: 100%; height: 100%; display: flex; flex-direction: column; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
    <!-- Tab Navigation -->
    <div style="display: flex; border-bottom: 2px solid #e1e5e9; background: #f8f9fa; padding: 0;">
        <button onclick="showTab('overview')" id="overview-tab" class="tab-button active" style="padding: 12px 24px; border: none; background: none; cursor: pointer; font-weight: 500; color: #1a73e8; border-bottom: 3px solid #1a73e8;">
            Supplier Variance Overview
        </button>
        <button onclick="showTab('contracts')" id="contracts-tab" class="tab-button" style="padding: 12px 24px; border: none; background: none; cursor: pointer; font-weight: 500; color: #5f6368;">
            Contract Deep Dive
        </button>
        <button onclick="showTab('placeholder')" id="placeholder-tab" class="tab-button" style="padding: 12px 24px; border: none; background: none; cursor: pointer; font-weight: 500; color: #5f6368;">
            Additional Analysis
        </button>
    </div>
    
    <!-- Tab Content -->
    <div style="flex: 1; overflow: auto; padding: 20px;">
        <!-- Tab 1: Supplier Variance Overview -->
        <div id="overview-content" class="tab-content" style="display: block;">
            <!-- KPI Cards -->
            <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 16px; margin-bottom: 24px;">
                <div class="kpi-card">
                    <div class="kpi-value">${total_variance}</div>
                    <div class="kpi-label">TOTAL VARIANCE IMPACT</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-value">${total_invoice}</div>
                    <div class="kpi-label">TOTAL INVOICE AMOUNT</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-value">{avg_variance_rate}%</div>
                    <div class="kpi-label">AVERAGE VARIANCE RATE</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-value">{compliance_rate}%</div>
                    <div class="kpi-label">PRICE COMPLIANCE RATE</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-value">{total_transactions}</div>
                    <div class="kpi-label">TOTAL TRANSACTIONS</div>
                </div>
            </div>
            
            <!-- Chart Title -->
            <h3 style="margin: 24px 0 16px 0; color: #202124; font-size: 18px; font-weight: 500;">
                Top Variance Opportunities (Ranked by Savings Potential)
            </h3>
            
            <!-- Bar Chart Container -->
            <div id="supplier-chart" style="height: 400px; margin-bottom: 24px; background: white; border: 1px solid #e1e5e9; border-radius: 8px; padding: 20px;">
                {supplier_chart}
            </div>
            
            <!-- Supporting Table -->
            <div style="background: white; border: 1px solid #e1e5e9; border-radius: 8px; overflow: hidden;">
                {supplier_table}
            </div>
        </div>
        
        <!-- Tab 2: Contract Deep Dive -->
        <div id="contracts-content" class="tab-content" style="display: none;">
            <h3 style="margin: 0 0 16px 0; color: #202124; font-size: 18px; font-weight: 500;">
                Top 5 Contracts - {rank1_supplier}
            </h3>
            <div style="background: #fef7e0; border: 1px solid #f9e7a0; border-radius: 4px; padding: 12px; margin-bottom: 16px;">
                <strong>Auto-filtered to Rank 1 Supplier:</strong> Showing contracts with highest variance opportunities
            </div>
            <div style="background: white; border: 1px solid #e1e5e9; border-radius: 8px; overflow: hidden;">
                {contract_table}
            </div>
        </div>
        
        <!-- Tab 3: Placeholder -->
        <div id="placeholder-content" class="tab-content" style="display: none;">
            <div style="text-align: center; padding: 80px 20px; color: #5f6368;">
                <h3 style="margin-bottom: 16px;">Additional Analysis Coming Soon</h3>
                <p>This tab is reserved for future analysis capabilities</p>
            </div>
        </div>
    </div>
</div>

<style>
.kpi-card {
    background: white;
    border: 1px solid #e1e5e9;
    border-radius: 8px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.kpi-value {
    font-size: 28px;
    font-weight: 600;
    color: #202124;
    margin-bottom: 8px;
}

.kpi-label {
    font-size: 11px;
    color: #5f6368;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 500;
}

.tab-button:hover {
    background-color: #f1f3f4 !important;
}

.tab-button.active {
    color: #1a73e8 !important;
    border-bottom: 3px solid #1a73e8 !important;
}

.tab-content {
    animation: fadeIn 0.3s ease-in;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

/* Table Styles */
table {
    width: 100%;
    border-collapse: collapse;
}

th {
    background-color: #f8f9fa;
    padding: 12px;
    text-align: left;
    font-weight: 500;
    color: #5f6368;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-bottom: 2px solid #e1e5e9;
}

td {
    padding: 12px;
    border-bottom: 1px solid #f1f3f4;
    color: #202124;
    font-size: 14px;
}

tr:hover {
    background-color: #f8f9fa;
}

/* Status Badge Styles */
.status-open {
    background-color: #fce8e6;
    color: #d33b27;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: 500;
}
</style>

<script>
function showTab(tabName) {
    // Hide all tab contents
    const contents = document.querySelectorAll('.tab-content');
    contents.forEach(content => content.style.display = 'none');
    
    // Remove active class from all tabs
    const tabs = document.querySelectorAll('.tab-button');
    tabs.forEach(tab => {
        tab.classList.remove('active');
        tab.style.color = '#5f6368';
        tab.style.borderBottom = 'none';
    });
    
    // Show selected content
    document.getElementById(tabName + '-content').style.display = 'block';
    
    // Activate selected tab
    const activeTab = document.getElementById(tabName + '-tab');
    activeTab.classList.add('active');
    activeTab.style.color = '#1a73e8';
    activeTab.style.borderBottom = '3px solid #1a73e8';
}
</script>
"""

# Chart template for supplier variance
SUPPLIER_CHART_TEMPLATE = """
<div id="supplierChart"></div>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script>
var data = [{{
    x: {suppliers},
    y: {variances},
    type: 'bar',
    marker: {{
        color: '#1a73e8'
    }},
    text: {variance_labels},
    textposition: 'outside',
    textfont: {{
        size: 12,
        color: '#202124'
    }},
    hovertemplate: '<b>%{{x}}</b><br>Variance: $%{{y:,.0f}}<extra></extra>'
}}];

var layout = {{
    margin: {{ t: 20, r: 20, b: 80, l: 80 }},
    xaxis: {{
        tickangle: -20,
        tickfont: {{ size: 12 }}
    }},
    yaxis: {{
        title: 'Variance Amount ($)',
        tickformat: '$,.0f',
        titlefont: {{ size: 14 }}
    }},
    plot_bgcolor: 'white',
    paper_bgcolor: 'white',
    showlegend: false,
    hoverlabel: {{
        bgcolor: 'white',
        bordercolor: '#e1e5e9',
        font: {{ size: 14 }}
    }}
}};

var config = {{
    responsive: true,
    displayModeBar: false
}};

Plotly.newPlot('supplierChart', data, layout, config);
</script>
"""

# Table templates
SUPPLIER_TABLE_TEMPLATE = """
<table>
    <thead>
        <tr>
            <th>Rank</th>
            <th>Supplier</th>
            <th>Category</th>
            <th>Contracted Price</th>
            <th>Actual Price</th>
            <th>Variance $</th>
            <th>Variance %</th>
        </tr>
    </thead>
    <tbody>
        {table_rows}
    </tbody>
</table>
"""

CONTRACT_TABLE_TEMPLATE = """
<table>
    <thead>
        <tr>
            <th>Variance Amount</th>
            <th>Contract Name</th>
            <th>Contract Type</th>
            <th>Category</th>
            <th>Invoice Price</th>
            <th>Expected Price</th>
        </tr>
    </thead>
    <tbody>
        {table_rows}
    </tbody>
</table>
"""