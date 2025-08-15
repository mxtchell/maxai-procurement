PAGES = ["1. Supplier Variance Overview", "2. Contract Deep Dive", "3. Recovery Pipeline"]

price_variance_layouts = {
    PAGES[0]: """{
        "layoutJson": {
            "type": "Document",
            "gap": "0px",
            "style": {
                "backgroundColor": "#ffffff",
                "width": "100%",
                "height": "max-content",
                "padding": "15px",
                "gap": "15px"
            },
            "children": [
                {
                    "name": "Paragraph0",
                    "type": "Paragraph",
                    "children": "",
                    "text": "Total Variance",
                    "style": {
                        "fontSize": "16px",
                        "fontWeight": "normal",
                        "textAlign": "left",
                        "verticalAlign": "start",
                        "color": "#050505",
                        "border": "none",
                        "textDecoration": "none",
                        "writingMode": "horizontal-tb"
                    },
                    "parentId": "FlexContainer7",
                    "flex": "shrink"
                },
                {
                    "name": "Paragraph1",
                    "type": "Paragraph",
                    "children": "",
                    "text": "$4,990,598",
                    "style": {
                        "fontSize": "32px",
                        "fontWeight": "600",
                        "textAlign": "left",
                        "verticalAlign": "start",
                        "color": "#000000",
                        "border": "none",
                        "textDecoration": "none",
                        "writingMode": "horizontal-tb"
                    },
                    "parentId": "FlexContainer7"
                },
                {
                    "name": "Paragraph2",
                    "type": "Paragraph",
                    "children": "",
                    "text": "Compliance Rate",
                    "style": {
                        "fontSize": "16px",
                        "fontWeight": "normal",
                        "textAlign": "left",
                        "verticalAlign": "start",
                        "color": "#000000",
                        "border": "none",
                        "textDecoration": "none",
                        "writingMode": "horizontal-tb"
                    },
                    "parentId": "FlexContainer8",
                    "flex": "shrink"
                },
                {
                    "name": "Paragraph3",
                    "type": "Paragraph",
                    "children": "",
                    "text": "60.0%",
                    "style": {
                        "fontSize": "32px",
                        "fontWeight": "600",
                        "textAlign": "left",
                        "verticalAlign": "start",
                        "color": "#000000",
                        "border": "none",
                        "textDecoration": "none",
                        "writingMode": "horizontal-tb"
                    },
                    "parentId": "FlexContainer8"
                },
                {
                    "name": "Paragraph4",
                    "type": "Paragraph",
                    "children": "",
                    "text": "Suppliers",
                    "style": {
                        "fontSize": "16px",
                        "fontWeight": "normal",
                        "textAlign": "left",
                        "verticalAlign": "start",
                        "color": "#000000",
                        "border": "none",
                        "textDecoration": "none",
                        "writingMode": "horizontal-tb"
                    },
                    "parentId": "FlexContainer9",
                    "flex": "shrink"
                },
                {
                    "name": "Paragraph5",
                    "type": "Paragraph",
                    "children": "",
                    "text": "20",
                    "style": {
                        "fontSize": "32px",
                        "fontWeight": "600",
                        "textAlign": "left",
                        "verticalAlign": "start",
                        "color": "#000000",
                        "border": "none",
                        "textDecoration": "none",
                        "writingMode": "horizontal-tb"
                    },
                    "parentId": "FlexContainer9"
                },
                {
                    "name": "Paragraph6",
                    "type": "Paragraph",
                    "children": "",
                    "text": "Avg Variance Rate",
                    "style": {
                        "fontSize": "16px",
                        "fontWeight": "normal",
                        "textAlign": "left",
                        "verticalAlign": "start",
                        "color": "#000000",
                        "border": "none",
                        "textDecoration": "none",
                        "writingMode": "horizontal-tb"
                    },
                    "parentId": "FlexContainer10",
                    "flex": "shrink"
                },
                {
                    "name": "Paragraph7",
                    "type": "Paragraph",
                    "children": "",
                    "text": "2.5%",
                    "style": {
                        "fontSize": "32px",
                        "fontWeight": "600",
                        "textAlign": "left",
                        "verticalAlign": "start",
                        "color": "#000000",
                        "border": "none",
                        "textDecoration": "none",
                        "writingMode": "horizontal-tb"
                    },
                    "parentId": "FlexContainer10"
                },
                {
                    "name": "Paragraph8",
                    "type": "Paragraph",
                    "children": "",
                    "text": "Total Invoice Price",
                    "style": {
                        "fontSize": "16px",
                        "fontWeight": "normal",
                        "textAlign": "left",
                        "verticalAlign": "start",
                        "color": "#000000",
                        "border": "none",
                        "textDecoration": "none",
                        "writingMode": "horizontal-tb"
                    },
                    "parentId": "FlexContainer11",
                    "flex": "shrink"
                },
                {
                    "name": "Paragraph9",
                    "type": "Paragraph",
                    "children": "",
                    "text": "$249,529,900",
                    "style": {
                        "fontSize": "32px",
                        "fontWeight": "600",
                        "textAlign": "left",
                        "verticalAlign": "start",
                        "color": "#000000",
                        "border": "none",
                        "textDecoration": "none",
                        "writingMode": "horizontal-tb"
                    },
                    "parentId": "FlexContainer11"
                },
                {
                    "name": "FlexContainer7",
                    "type": "FlexContainer",
                    "children": "",
                    "minHeight": "120px",
                    "direction": "column",
                    "parentId": "FlexContainer3",
                    "label": "FlexContainer-KPI_Card1",
                    "style": {
                        "borderRadius": "11.911px",
                        "box-shadow": "0px 0px 8.785px 0px rgba(0, 0, 0, 0.10) inset",
                        "padding": "10px",
                        "fontFamily": "Arial",
                        "backgroundColor": "#eff6ff",
                        "border-left": "4px solid #3b82f6"
                    }
                },
                {
                    "name": "FlexContainer8",
                    "type": "FlexContainer",
                    "children": "",
                    "minHeight": "120px",
                    "direction": "column",
                    "parentId": "FlexContainer3",
                    "label": "FlexContainer-KPI_Card2",
                    "style": {
                        "borderRadius": "11.911px",
                        "box-shadow": "0px 0px 8.785px 0px rgba(0, 0, 0, 0.10) inset",
                        "padding": "10px",
                        "fontFamily": "Arial",
                        "backgroundColor": "#f0fdf4"
                    }
                },
                {
                    "name": "FlexContainer9",
                    "type": "FlexContainer",
                    "children": "",
                    "minHeight": "120px",
                    "direction": "column",
                    "parentId": "FlexContainer3",
                    "label": "FlexContainer-KPI_Card3",
                    "style": {
                        "borderRadius": "11.911px",
                        "box-shadow": "0px 0px 8.785px 0px rgba(0, 0, 0, 0.10) inset",
                        "padding": "10px",
                        "fontFamily": "Arial",
                        "backgroundColor": "#fef3c7"
                    }
                },
                {
                    "name": "FlexContainer10",
                    "type": "FlexContainer",
                    "children": "",
                    "minHeight": "120px",
                    "direction": "column",
                    "parentId": "FlexContainer3",
                    "label": "FlexContainer-KPI_Card4",
                    "style": {
                        "borderRadius": "11.911px",
                        "box-shadow": "0px 0px 8.785px 0px rgba(0, 0, 0, 0.10) inset",
                        "padding": "10px",
                        "fontFamily": "Arial",
                        "backgroundColor": "#fef2f2"
                    }
                },
                {
                    "name": "FlexContainer11",
                    "type": "FlexContainer",
                    "children": "",
                    "minHeight": "120px",
                    "direction": "column",
                    "parentId": "FlexContainer3",
                    "label": "FlexContainer-KPI_Card5",
                    "style": {
                        "borderRadius": "11.911px",
                        "box-shadow": "0px 0px 8.785px 0px rgba(0, 0, 0, 0.10) inset",
                        "padding": "10px",
                        "fontFamily": "Arial",
                        "backgroundColor": "#f3f4f6"
                    }
                },
                {
                    "name": "FlexContainer3",
                    "type": "FlexContainer",
                    "children": "",
                    "minHeight": "150px",
                    "direction": "row",
                    "label": "FlexContainer-KPI_panel",
                    "extraStyles": "gap: 15px"
                },
                {
                    "name": "HighchartsChart0",
                    "type": "HighchartsChart",
                    "children": "",
                    "minHeight": "400px",
                    "chartOptions": {
                        "chart": {
                            "type": "column"
                        },
                        "title": {
                            "text": "Top 5 Suppliers by Variance"
                        },
                        "xAxis": {
                            "categories": [
                                "Supplier A",
                                "Supplier B",
                                "Supplier C"
                            ]
                        },
                        "yAxis": {
                            "title": {
                                "text": "Values"
                            }
                        },
                        "series": [
                            {
                                "name": "Series 1",
                                "data": [
                                    100000,
                                    80000,
                                    60000
                                ]
                            }
                        ]
                    },
                    "options": {
                        "chart": {
                            "type": "column",
                            "polar": false,
                            "backgroundColor": "#f8fafc"
                        },
                        "title": {
                            "text": "Top 5 Suppliers by Variance",
                            "style": {
                                "fontSize": "20px"
                            }
                        },
                        "xAxis": {
                            "categories": [
                                "EcoBox Packaging",
                                "Global Supply Co",
                                "SupplyBridge"
                            ],
                            "title": {
                                "text": "Suppliers"
                            }
                        },
                        "yAxis": {
                            "title": {
                                "text": "Variance ($)"
                            }
                        },
                        "series": [
                            {
                                "name": "Price Variance",
                                "data": [
                                    380058,
                                    340780,
                                    324270
                                ]
                            }
                        ],
                        "credits": {
                            "enabled": false
                        },
                        "legend": {
                            "enabled": false
                        }
                    },
                    "label": "HighchartsChart-suppliers",
                    "extraStyles": "border-radius: 8px"
                },
                {
                    "name": "Header0",
                    "type": "Header",
                    "children": "",
                    "text": "Price Variance Deep Dive",
                    "style": {
                        "fontSize": "20px",
                        "fontWeight": "normal",
                        "textAlign": "left",
                        "verticalAlign": "start",
                        "color": "#000000",
                        "border": "none",
                        "textDecoration": "none",
                        "writingMode": "horizontal-tb"
                    },
                    "parentId": "FlexContainer0",
                    "flex": "shrink",
                    "label": "Header-Main_Title"
                },
                {
                    "name": "Markdown0",
                    "type": "Markdown",
                    "children": "",
                    "text": "Analysis insights will appear here...",
                    "style": {
                        "fontSize": "16px",
                        "color": "#000000",
                        "border": "none"
                    },
                    "parentId": "FlexContainer0",
                    "label": "Markdown-insights"
                },
                {
                    "name": "FlexContainer0",
                    "type": "FlexContainer",
                    "children": "",
                    "minHeight": "250px",
                    "style": {
                        "borderRadius": "11.911px",
                        "box-shadow": "0px 0px 8.785px 0px rgba(0, 0, 0, 0.10) inset",
                        "padding": "10px",
                        "fontFamily": "Arial",
                        "backgroundColor": "#edf2f7",
                        "border-left": "4px solid #3b82f6"
                    },
                    "direction": "column",
                    "hidden": false,
                    "label": "FlexContainer-Insights",
                    "extraStyles": "border-radius: 8px;",
                    "flex": "1 1 250px"
                },
                {
                    "name": "DataTable0",
                    "type": "DataTable",
                    "children": "",
                    "columns": [
                        {
                            "name": "Rank"
                        },
                        {
                            "name": "Supplier"
                        },
                        {
                            "name": "Variance $"
                        },
                        {
                            "name": "Variance %"
                        }
                    ],
                    "data": [
                        [
                            1,
                            "Supplier A",
                            "$100,000",
                            "5.0%"
                        ],
                        [
                            2,
                            "Supplier B",
                            "$80,000",
                            "4.2%"
                        ],
                        [
                            3,
                            "Supplier C",
                            "$60,000",
                            "3.8%"
                        ]
                    ],
                    "label": "DataTable-Suppliers"
                }
            ]
        },
        "inputVariables": [
            {
                "name": "kpi1_value",
                "isRequired": false,
                "defaultValue": null,
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "Paragraph1",
                        "fieldName": "text"
                    }
                ]
            },
            {
                "name": "kpi2_value",
                "isRequired": false,
                "defaultValue": null,
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "Paragraph3",
                        "fieldName": "text"
                    }
                ]
            },
            {
                "name": "kpi3_value",
                "isRequired": false,
                "defaultValue": null,
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "Paragraph5",
                        "fieldName": "text"
                    }
                ]
            },
            {
                "name": "kpi4_value",
                "isRequired": false,
                "defaultValue": null,
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "Paragraph7",
                        "fieldName": "text"
                    }
                ]
            },
            {
                "name": "kpi5_value",
                "isRequired": false,
                "defaultValue": null,
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "Paragraph9",
                        "fieldName": "text"
                    }
                ]
            },
            {
                "name": "chart_title",
                "isRequired": false,
                "defaultValue": null,
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "HighchartsChart0",
                        "fieldName": "options.title.text"
                    }
                ]
            },
            {
                "name": "chart_categories",
                "isRequired": false,
                "defaultValue": null,
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "HighchartsChart0",
                        "fieldName": "options.xAxis.categories"
                    }
                ]
            },
            {
                "name": "chart_data_series",
                "isRequired": false,
                "defaultValue": null,
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "HighchartsChart0",
                        "fieldName": "options.series"
                    }
                ]
            },
            {
                "name": "exec_summary",
                "isRequired": false,
                "defaultValue": null,
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "Markdown0",
                        "fieldName": "text"
                    }
                ]
            },
            {
                "name": "data",
                "isRequired": false,
                "defaultValue": null,
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "DataTable0",
                        "fieldName": "data"
                    }
                ]
            },
            {
                "name": "col_defs",
                "isRequired": false,
                "defaultValue": null,
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "DataTable0",
                        "fieldName": "columns"
                    }
                ]
            }
        ]
    }""",

    PAGES[1]: """{
        "layoutJson": {
            "type": "Document",
            "gap": "0px",
            "style": {
                "backgroundColor": "#ffffff",
                "width": "100%",
                "height": "max-content",
                "padding": "15px",
                "gap": "15px"
            },
            "children": [
                {
                    "name": "Header1",
                    "type": "Header",
                    "children": "",
                    "text": "Top Supplier Contract Analysis", 
                    "style": {
                        "fontSize": "18px",
                        "fontWeight": "600",
                        "color": "#374151",
                        "marginTop": "10px"
                    },
                    "label": "Header-Subtitle"
                },
                {
                    "name": "FlexContainer0",
                    "type": "FlexContainer",
                    "children": "",
                    "minHeight": "150px",
                    "direction": "row",
                    "label": "FlexContainer-KPI_panel",
                    "extraStyles": "gap: 15px; margin-bottom: 30px;"
                },
                {
                    "name": "FlexContainer1",
                    "type": "FlexContainer", 
                    "children": "",
                    "minHeight": "120px",
                    "direction": "column",
                    "parentId": "FlexContainer0",
                    "label": "FlexContainer-KPI_Card1",
                    "style": {
                        "flex": "1",
                        "backgroundColor": "#eff6ff",
                        "padding": "15px",
                        "borderRadius": "8px",
                        "border": "1px solid #dbeafe"
                    }
                },
                {
                    "name": "Paragraph0",
                    "type": "Paragraph",
                    "children": "",
                    "text": "Total Contract Variance",
                    "style": {
                        "fontSize": "14px",
                        "color": "#6b7280",
                        "marginBottom": "5px"
                    },
                    "parentId": "FlexContainer1",
                    "flex": "shrink"
                },
                {
                    "name": "Paragraph1",
                    "type": "Paragraph",
                    "children": "",
                    "text": "$0",
                    "style": {
                        "fontSize": "24px",
                        "fontWeight": "bold",
                        "color": "#1f2937"
                    },
                    "parentId": "FlexContainer1"
                },
                {
                    "name": "FlexContainer2",
                    "type": "FlexContainer",
                    "children": "",
                    "minHeight": "120px", 
                    "direction": "column",
                    "parentId": "FlexContainer0",
                    "label": "FlexContainer-KPI_Card2",
                    "style": {
                        "flex": "1",
                        "backgroundColor": "#f0fdf4",
                        "padding": "15px",
                        "borderRadius": "8px",
                        "border": "1px solid #dcfce7"
                    }
                },
                {
                    "name": "Paragraph2",
                    "type": "Paragraph",
                    "children": "",
                    "text": "Number of Contracts",
                    "style": {
                        "fontSize": "14px",
                        "color": "#6b7280", 
                        "marginBottom": "5px"
                    },
                    "parentId": "FlexContainer2",
                    "flex": "shrink"
                },
                {
                    "name": "Paragraph3",
                    "type": "Paragraph",
                    "children": "",
                    "text": "0",
                    "style": {
                        "fontSize": "24px",
                        "fontWeight": "bold",
                        "color": "#1f2937"
                    },
                    "parentId": "FlexContainer2"
                },
                {
                    "name": "FlexContainer3",
                    "type": "FlexContainer",
                    "children": "",
                    "minHeight": "120px",
                    "direction": "column", 
                    "parentId": "FlexContainer0",
                    "label": "FlexContainer-KPI_Card3",
                    "style": {
                        "flex": "1",
                        "backgroundColor": "#fef3c7",
                        "padding": "15px",
                        "borderRadius": "8px",
                        "border": "1px solid #fde68a"
                    }
                },
                {
                    "name": "Paragraph4",
                    "type": "Paragraph",
                    "children": "",
                    "text": "Top Contract Variance",
                    "style": {
                        "fontSize": "14px",
                        "color": "#6b7280",
                        "marginBottom": "5px"
                    },
                    "parentId": "FlexContainer3",
                    "flex": "shrink"
                },
                {
                    "name": "Paragraph5",
                    "type": "Paragraph",
                    "children": "",
                    "text": "$0",
                    "style": {
                        "fontSize": "24px",
                        "fontWeight": "bold",
                        "color": "#1f2937"
                    },
                    "parentId": "FlexContainer3"
                },
                {
                    "name": "Header2",
                    "type": "Header",
                    "children": "",
                    "text": "Top Variance Opportunities",
                    "style": {
                        "fontSize": "18px",
                        "fontWeight": "600",
                        "color": "#374151",
                        "marginTop": "30px",
                        "marginBottom": "15px"
                    },
                    "label": "Header-Chart_Title"
                },
                {
                    "name": "HighchartsChart0",
                    "type": "HighchartsChart",
                    "children": "",
                    "minHeight": "400px",
                    "options": {
                        "chart": {
                            "type": "column",
                            "backgroundColor": "#f8fafc"
                        },
                        "title": {
                            "text": "Top 5 Contracts by Variance - {top_supplier}",
                            "style": {
                                "fontSize": "16px"
                            }
                        },
                        "xAxis": {
                            "categories": ["Contract A", "Contract B", "Contract C"],
                            "title": {
                                "text": "Contracts"
                            }
                        },
                        "yAxis": {
                            "title": {
                                "text": "Variance ($)"
                            }
                        },
                        "series": [
                            {
                                "name": "Contract Variance",
                                "data": [50000, 40000, 30000]
                            }
                        ],
                        "credits": {
                            "enabled": false
                        },
                        "legend": {
                            "enabled": false
                        }
                    },
                    "label": "HighchartsChart-Contracts",
                    "extraStyles": "border-radius: 8px;"
                },
                {
                    "name": "Header3",
                    "type": "Header",
                    "children": "",
                    "text": "Contract Analysis for EcoBox Packaging",
                    "style": {
                        "fontSize": "20px",
                        "fontWeight": "normal",
                        "textAlign": "left",
                        "verticalAlign": "start",
                        "color": "#000000",
                        "border": "none",
                        "textDecoration": "none",
                        "writingMode": "horizontal-tb"
                    },
                    "parentId": "FlexContainer4",
                    "flex": "shrink",
                    "label": "Header-Insights_Title"
                },
                {
                    "name": "Markdown0",
                    "type": "Markdown", 
                    "children": "",
                    "text": "Contract analysis insights will appear here...",
                    "style": {
                        "fontSize": "16px",
                        "color": "#000000",
                        "border": "none"
                    },
                    "parentId": "FlexContainer4",
                    "label": "Markdown-Insights_Text"
                },
                {
                    "name": "FlexContainer4",
                    "type": "FlexContainer",
                    "children": "",
                    "minHeight": "250px",
                    "style": {
                        "borderRadius": "11.911px",
                        "box-shadow": "0px 0px 8.785px 0px rgba(0, 0, 0, 0.10) inset",
                        "padding": "10px",
                        "fontFamily": "Arial",
                        "backgroundColor": "#edf2f7",
                        "border-left": "4px solid #3b82f6"
                    },
                    "direction": "column",
                    "hidden": false,
                    "label": "FlexContainer-Insights",
                    "extraStyles": "border-radius: 8px;",
                    "flex": "1 1 250px"
                },
                {
                    "name": "Header4",
                    "type": "Header",
                    "children": "",
                    "text": "Contract Details",
                    "style": {
                        "fontSize": "18px",
                        "fontWeight": "600", 
                        "color": "#374151",
                        "marginTop": "30px",
                        "marginBottom": "15px"
                    },
                    "label": "Header-Table_Title"
                },
                {
                    "name": "DataTable0",
                    "type": "DataTable",
                    "children": "",
                    "columns": [
                        {"name": "Variance Amount"},
                        {"name": "Contract Name"},
                        {"name": "Type"},
                        {"name": "Category"}
                    ],
                    "data": [
                        ["$50,000", "Master Agreement A", "Service Agreement", "Professional Services"],
                        ["$40,000", "Supply Contract B", "Supply Agreement", "Materials"],
                        ["$30,000", "Maintenance Contract C", "Maintenance Agreement", "Support Services"]
                    ],
                    "label": "DataTable-Contracts"
                }
            ]
        },
        "inputVariables": [
            {
                "name": "kpi1_value",
                "isRequired": false,
                "defaultValue": null,
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "Paragraph1",
                        "fieldName": "text"
                    }
                ]
            },
            {
                "name": "kpi2_value",
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "Paragraph3", 
                        "fieldName": "text"
                    }
                ]
            },
            {
                "name": "kpi3_value",
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "Paragraph5",
                        "fieldName": "text"
                    }
                ]
            },
            {
                "name": "chart_categories",
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "HighchartsChart0",
                        "fieldName": "options.xAxis.categories"
                    }
                ]
            },
            {
                "name": "chart_data_series",
                "isRequired": false,
                "defaultValue": null,
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "HighchartsChart0",
                        "fieldName": "options.series"
                    }
                ]
            },
            {
                "name": "exec_summary",
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "Markdown0",
                        "fieldName": "text"
                    }
                ]
            },
            {
                "name": "data",
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "DataTable0",
                        "fieldName": "data"
                    }
                ]
            },
            {
                "name": "col_defs",
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "DataTable0",
                        "fieldName": "columns"
                    }
                ]
            },
            {
                "name": "headline",
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "Header3",
                        "fieldName": "text"
                    }
                ]
            }
        ]
    }""",

    PAGES[2]: """{
        "layoutJson": {
            "type": "Document",
            "gap": "0px",
            "style": {
                "backgroundColor": "#ffffff",
                "width": "100%",
                "height": "max-content",
                "padding": "15px",
                "gap": "15px"
            },
            "children": [
                {
                    "name": "Header0",
                    "type": "Header",
                    "children": "",
                    "text": "Recovery Pipeline",
                    "style": {
                        "fontSize": "24px",
                        "fontWeight": "bold",
                        "textAlign": "center",
                        "color": "#1f2937"
                    },
                    "label": "Header-Main_Title"
                },
                {
                    "name": "Header1",
                    "type": "Header",
                    "children": "",
                    "text": "Price Variance Recovery Tracking & Opportunities",
                    "style": {
                        "fontSize": "18px",
                        "fontWeight": "600",
                        "color": "#374151",
                        "marginTop": "10px"
                    },
                    "label": "Header-Subtitle"
                },
                {
                    "name": "FlexContainer0",
                    "type": "FlexContainer",
                    "children": "",
                    "minHeight": "150px",
                    "direction": "row",
                    "label": "FlexContainer-KPI_panel",
                    "extraStyles": "gap: 15px; margin-bottom: 30px;"
                },
                {
                    "name": "FlexContainer1",
                    "type": "FlexContainer",
                    "children": "",
                    "minHeight": "120px",
                    "direction": "column",
                    "parentId": "FlexContainer0",
                    "label": "FlexContainer-KPI_Card1",
                    "style": {
                        "flex": "1",
                        "backgroundColor": "#eff6ff",
                        "padding": "15px",
                        "borderRadius": "8px",
                        "border": "1px solid #dbeafe"
                    }
                },
                {
                    "name": "Paragraph0",
                    "type": "Paragraph",
                    "children": "",
                    "text": "Recovery Potential",
                    "style": {
                        "fontSize": "14px",
                        "color": "#6b7280",
                        "marginBottom": "5px"
                    },
                    "parentId": "FlexContainer1",
                    "flex": "shrink"
                },
                {
                    "name": "Paragraph1",
                    "type": "Paragraph",
                    "children": "",
                    "text": "$156,400",
                    "style": {
                        "fontSize": "24px",
                        "fontWeight": "bold",
                        "color": "#1f2937"
                    },
                    "parentId": "FlexContainer1"
                },
                {
                    "name": "FlexContainer2",
                    "type": "FlexContainer",
                    "children": "",
                    "minHeight": "120px",
                    "direction": "column",
                    "parentId": "FlexContainer0",
                    "label": "FlexContainer-KPI_Card2",
                    "style": {
                        "flex": "1",
                        "backgroundColor": "#f0fdf4",
                        "padding": "15px",
                        "borderRadius": "8px",
                        "border": "1px solid #dcfce7"
                    }
                },
                {
                    "name": "Paragraph2",
                    "type": "Paragraph",
                    "children": "",
                    "text": "In Progress",
                    "style": {
                        "fontSize": "14px",
                        "color": "#6b7280",
                        "marginBottom": "5px"
                    },
                    "parentId": "FlexContainer2",
                    "flex": "shrink"
                },
                {
                    "name": "Paragraph3",
                    "type": "Paragraph",
                    "children": "",
                    "text": "$23,100",
                    "style": {
                        "fontSize": "24px",
                        "fontWeight": "bold",
                        "color": "#1f2937"
                    },
                    "parentId": "FlexContainer2"
                },
                {
                    "name": "FlexContainer3",
                    "type": "FlexContainer",
                    "children": "",
                    "minHeight": "120px",
                    "direction": "column",
                    "parentId": "FlexContainer0",
                    "label": "FlexContainer-KPI_Card3",
                    "style": {
                        "flex": "1",
                        "backgroundColor": "#fef3c7",
                        "padding": "15px",
                        "borderRadius": "8px",
                        "border": "1px solid #fde68a"
                    }
                },
                {
                    "name": "Paragraph4",
                    "type": "Paragraph",
                    "children": "",
                    "text": "Recovered This Month",
                    "style": {
                        "fontSize": "14px",
                        "color": "#6b7280",
                        "marginBottom": "5px"
                    },
                    "parentId": "FlexContainer3",
                    "flex": "shrink"
                },
                {
                    "name": "Paragraph5",
                    "type": "Paragraph",
                    "children": "",
                    "text": "$8,750",
                    "style": {
                        "fontSize": "24px",
                        "fontWeight": "bold",
                        "color": "#1f2937"
                    },
                    "parentId": "FlexContainer3"
                },
                {
                    "name": "FlexContainer4",
                    "type": "FlexContainer",
                    "children": "",
                    "minHeight": "120px",
                    "direction": "column",
                    "parentId": "FlexContainer0",
                    "label": "FlexContainer-KPI_Card4",
                    "style": {
                        "flex": "1",
                        "backgroundColor": "#fef2f2",
                        "padding": "15px",
                        "borderRadius": "8px",
                        "border": "1px solid #fecaca"
                    }
                },
                {
                    "name": "Paragraph6",
                    "type": "Paragraph",
                    "children": "",
                    "text": "Active Recovery Items",
                    "style": {
                        "fontSize": "14px",
                        "color": "#6b7280",
                        "marginBottom": "5px"
                    },
                    "parentId": "FlexContainer4",
                    "flex": "shrink"
                },
                {
                    "name": "Paragraph7",
                    "type": "Paragraph",
                    "children": "",
                    "text": "15",
                    "style": {
                        "fontSize": "24px",
                        "fontWeight": "bold",
                        "color": "#1f2937"
                    },
                    "parentId": "FlexContainer4"
                },
                {
                    "name": "Header2",
                    "type": "Header",
                    "children": "",
                    "text": "Recovery Timeline",
                    "style": {
                        "fontSize": "18px",
                        "fontWeight": "600",
                        "color": "#374151",
                        "marginTop": "30px",
                        "marginBottom": "15px"
                    },
                    "label": "Header-Timeline_Title"
                },
                {
                    "name": "HighchartsChart0",
                    "type": "HighchartsChart",
                    "children": "",
                    "minHeight": "400px",
                    "chartOptions": {
                        "chart": {
                            "type": "line"
                        },
                        "title": {
                            "text": "Recovery Timeline & Progress"
                        },
                        "xAxis": {
                            "categories": ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5+"]
                        },
                        "yAxis": {
                            "title": {
                                "text": "Recovery Amount ($K)"
                            }
                        },
                        "series": [
                            {
                                "name": "Volume Price Break - 90%",
                                "data": [5, 10, 15, 25, 30],
                                "color": "#059669"
                            },
                            {
                                "name": "Logistics Path - 75%",
                                "data": [2, 8, 18, 28, 35],
                                "color": "#f59e0b",
                                "dashStyle": "Dash"
                            },
                            {
                                "name": "Alt Source - 10%",
                                "data": [0, 1, 2, 3, 8],
                                "color": "#dc2626",
                                "dashStyle": "Dot"
                            }
                        ]
                    },
                    "options": {
                        "chart": {
                            "type": "line",
                            "backgroundColor": "#f8fafc"
                        },
                        "title": {
                            "text": "Recovery Timeline & Progress",
                            "style": {
                                "fontSize": "20px"
                            }
                        },
                        "xAxis": {
                            "categories": ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5+"],
                            "title": {
                                "text": "Timeline"
                            }
                        },
                        "yAxis": {
                            "title": {
                                "text": "Recovery Amount ($K)"
                            },
                            "labels": {
                                "format": "${value}K"
                            }
                        },
                        "series": [
                            {
                                "name": "Volume Price Break - 90%",
                                "data": [5, 10, 15, 25, 30],
                                "color": "#059669"
                            },
                            {
                                "name": "Logistics Path - 75%",
                                "data": [2, 8, 18, 28, 35],
                                "color": "#f59e0b",
                                "dashStyle": "Dash"
                            },
                            {
                                "name": "Alt Source - 10%",
                                "data": [0, 1, 2, 3, 8],
                                "color": "#dc2626",
                                "dashStyle": "Dot"
                            }
                        ],
                        "credits": {
                            "enabled": false
                        },
                        "legend": {
                            "enabled": true,
                            "align": "center",
                            "verticalAlign": "bottom"
                        },
                        "plotOptions": {
                            "line": {
                                "marker": {
                                    "enabled": true
                                }
                            }
                        }
                    },
                    "label": "HighchartsChart-Recovery_Timeline",
                    "extraStyles": "border-radius: 8px;"
                },
                {
                    "name": "Markdown0",
                    "type": "Markdown",
                    "children": "",
                    "text": "Recovery pipeline insights and timeline analysis...",
                    "style": {
                        "fontSize": "14px",
                        "lineHeight": "1.6",
                        "color": "#374151"
                    },
                    "label": "Markdown-Timeline_Text"
                },
                {
                    "name": "Header3",
                    "type": "Header",
                    "children": "",
                    "text": "Recovery Items",
                    "style": {
                        "fontSize": "18px",
                        "fontWeight": "600",
                        "color": "#374151",
                        "marginTop": "30px",
                        "marginBottom": "15px"
                    },
                    "label": "Header-Table_Title"
                },
                {
                    "name": "DataTable0",
                    "type": "DataTable",
                    "children": "",
                    "columns": [
                        {"name": "Recovery Item"},
                        {"name": "Supplier"},
                        {"name": "Variance Amount"},
                        {"name": "Recovery Status"},
                        {"name": "Expected Resolution"},
                        {"name": "Owner"}
                    ],
                    "data": [
                        ["Volume discount recalculation", "Gamma Supply", "$70,500", "Supplier acknowledged, credit processing", "Aug 15, 2024", "Sarah Johnson"],
                        ["Contract amendment pricing update", "Beta Industries", "$45,200", "System update scheduled", "Aug 5, 2024", "Mike Chen"],
                        ["Pricing tier correction", "Alpha Manufacturing", "$34,650", "Under supplier review", "Aug 10, 2024", "Lisa Rodriguez"]
                    ],
                    "label": "DataTable-Recovery"
                }
            ]
        },
        "inputVariables": [
            {
                "name": "kpi1_value",
                "isRequired": false,
                "defaultValue": null,
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "Paragraph1",
                        "fieldName": "text"
                    }
                ]
            },
            {
                "name": "kpi2_value",
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "Paragraph3",
                        "fieldName": "text"
                    }
                ]
            },
            {
                "name": "kpi3_value",
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "Paragraph5",
                        "fieldName": "text"
                    }
                ]
            },
            {
                "name": "kpi4_value",
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "Paragraph7",
                        "fieldName": "text"
                    }
                ]
            },
            {
                "name": "exec_summary",
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "Markdown0",
                        "fieldName": "text"
                    }
                ]
            },
            {
                "name": "data",
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "DataTable0",
                        "fieldName": "data"
                    }
                ]
            },
            {
                "name": "col_defs",
                "isRequired": false,
                "defaultValue": null,
                "targets": [
                    {
                        "elementName": "DataTable0",
                        "fieldName": "columns"
                    }
                ]
            }
        ]
    }"""
}