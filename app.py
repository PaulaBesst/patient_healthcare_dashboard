# Import necessary libraries
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def load_data():
    # Load and preprocess the data
    df = pd.read_csv('assets/healthcare.csv')
    df['Billing Amount'] = pd.to_numeric(df['Billing Amount'], errors='coerce')
    df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
    df['YearMonth'] = df['Date of Admission'].dt.to_period('M')  # Aggregating by month
    return df

df = load_data()

# Calculate summary statistics
num_records = len(df)
avg_billing = df['Billing Amount'].mean()

# Initialize the Dash app with a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, '/assets/styles.css'])

# Expose the server for deployment
server = app.server

# Modern color palette
colors = {
    'primary': '#34a6db',
    'secondary': '#102055',
    'success': '#2ca02c',
    'danger': '#d62728',
    'warning': '#ff7f0e',
    'info': '#17a2b8',
    'light': '#f8f9fa',
    'dark': '#343a40'
}

# Layout
app.layout = dbc.Container([
    # Header Section
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H1("Healthcare Analytics Dashboard", className="dashboard-title"),
                html.P("Comprehensive Patient Data Insights", className="dashboard-subtitle")
            ], className="header-content")
        ], width=12)
    ], className="header-row"),

    # Summary Statistics Cards
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.H3(f"{num_records:,}", className="metric-value"),
                        html.P("Total Patient Records", className="metric-label"),
                        html.I(className="fas fa-users metric-icon")
                    ], className="metric-content")
                ])
            ], className="summary-card patients-card")
        ], width=6),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.H3(f"${avg_billing:,.0f}", className="metric-value"),
                        html.P("Average Billing Amount", className="metric-label"),
                        html.I(className="fas fa-dollar-sign metric-icon")
                    ], className="metric-content")
                ])
            ], className="summary-card billing-card")
        ], width=6),
    ], className="summary-row"),

    # Main Charts Row 1
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H4("Patient Demographics", className="card-title"),
                    dcc.Dropdown(
                        id="gender-filter",
                        options=[{"label": gender, "value": gender} for gender in df['Gender'].unique()],
                        value=None,
                        placeholder="Filter by Gender",
                        className="modern-dropdown"
                    )
                ]),
                dbc.CardBody([
                    dcc.Graph(id="age-distribution", className="chart-container")
                ])
            ], className="chart-card")
        ], width=6),

        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H4("Medical Condition Distribution", className="card-title")
                ]),
                dbc.CardBody([
                    dcc.Graph(id="condition-distribution", className="chart-container")
                ])
            ], className="chart-card")
        ], width=6),
    ], className="charts-row"),

    # Insurance Provider Comparison
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H4("Insurance Provider Analysis", className="card-title")
                ]),
                dbc.CardBody([
                    dcc.Graph(id="insurance-comparison", className="chart-container")
                ])
            ], className="chart-card full-width-card")
        ], width=12),
    ], className="charts-row"),

    # Billing Distribution
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H4("Billing Amount Distribution", className="card-title"),
                    html.P("Adjust the slider to filter billing amounts", className="card-subtitle")
                ]),
                dbc.CardBody([
                    dcc.RangeSlider(
                        id='billing-slider',
                        min=df['Billing Amount'].min(),
                        max=df['Billing Amount'].max(),
                        value=[df['Billing Amount'].min(), df['Billing Amount'].max()],
                        marks={int(value): f'${int(value/1000)}K' for value in df['Billing Amount'].quantile([0, 0.25, 0.5, 0.75, 1]).values},
                        step=1000,
                        className="modern-slider"
                    ),
                    dcc.Graph(id="billing-distribution", className="chart-container")
                ])
            ], className="chart-card")
        ], width=12),
    ], className="charts-row"),

    # Admission Trends
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.Div([
                        html.H4("Admission Trends Over Time", className="card-title"),
                        html.Div([
                            dbc.RadioItems(
                                id='chart-type',
                                options=[
                                    {'label': 'Line Chart', 'value': 'line'}, 
                                    {'label': 'Bar Chart', 'value': 'bar'}
                                ],
                                value='line',
                                inline=True,
                                className='chart-type-selector'
                            )
                        ])
                    ], className="card-header-content")
                ]),
                dbc.CardBody([
                    dcc.Dropdown(
                        id="condition-filter",
                        options=[{"label": condition, "value": condition} for condition in df['Medical Condition'].unique()],
                        value=None,
                        placeholder="Filter by Medical Condition",
                        className="modern-dropdown"
                    ),
                    dcc.Graph(id="admission-trends", className="chart-container")
                ])
            ], className="chart-card")
        ], width=12),
    ], className="charts-row"),

    # Footer
    dbc.Row([
        dbc.Col([
            html.Div([
                html.Hr(),
                html.P("Healthcare Analytics Dashboard © 2024", className="footer-text")
            ])
        ], width=12)
    ])
], fluid=True, className="dashboard-container")


# Callbacks for interactivity

@app.callback(
    Output('age-distribution', 'figure'),
    Input('gender-filter', 'value')
)
def update_age_distribution(selected_gender):
    # Filter the dataframe based on the selected gender
    if selected_gender:
        filtered_df = df[df['Gender'] == selected_gender]
    else:
        filtered_df = df

    # Check if the filtered dataframe is not empty
    if filtered_df.empty:
        return {}

    # Create the histogram with modern styling
    fig = px.histogram(
        filtered_df, 
        x="Age", 
        nbins=20, 
        color="Gender", 
        title="Age Distribution by Gender",
        color_discrete_sequence=["#1d6a96", "#38a6a4"],
        template="plotly_white"
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter, sans-serif"),
        title_font_size=16,
        title_x=0.5
    )

    return fig


@app.callback(
    Output('condition-distribution', 'figure'),
    Input('gender-filter', 'value')
)
def update_condition_distribution(selected_gender):
    filtered_df = df[df['Gender'] == selected_gender] if selected_gender else df
    
    fig = px.pie(
        filtered_df, 
        names="Medical Condition", 
        title="Medical Condition Distribution",
        color_discrete_sequence=px.colors.qualitative.Prism,
        template="plotly_white"
    )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter, sans-serif"),
        title_font_size=16,
        title_x=0.5,
        showlegend=True,
        legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1.05)
    )
    
    return fig


@app.callback(
    Output('admission-trends', 'figure'),
    [Input('chart-type', 'value'),
     Input('condition-filter', 'value')]
)
def update_admission_trends(chart_type, selected_condition):
    filtered_df = df[df['Medical Condition'] == selected_condition] if selected_condition else df
    
    # Group by YearMonth and convert to string
    trend_df = filtered_df.groupby('YearMonth').size().reset_index(name='Count')
    trend_df['YearMonth'] = trend_df['YearMonth'].astype(str)

    if chart_type == 'line':
        fig = px.line(
            trend_df, 
            x='YearMonth', 
            y='Count', 
            title="Admission Trends Over Time",
            line_shape='spline',
            template="plotly_white"
        )
        fig.update_traces(line=dict(color='#3498db', width=3))
    else:
        fig = px.bar(
            trend_df, 
            x='YearMonth', 
            y='Count', 
            title="Admission Trends Over Time",
            template="plotly_white"
        )
        fig.update_traces(marker_color='#3498db')
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter, sans-serif"),
        title_font_size=16,
        title_x=0.5,
        xaxis_title="Time Period",
        yaxis_title="Number of Admissions"
    )
    
    return fig


@app.callback(
    Output('billing-distribution', 'figure'),
    [Input('gender-filter', 'value'),
     Input('billing-slider', 'value')]
)
def update_billing_distribution(selected_gender, slider_value):
    filtered_df = df[df['Gender'] == selected_gender] if selected_gender else df
    filtered_df = filtered_df[
        (filtered_df['Billing Amount'] >= slider_value[0]) & 
        (filtered_df['Billing Amount'] <= slider_value[1])
    ]
    
    fig = px.histogram(
        filtered_df, 
        x="Billing Amount", 
        nbins=20, 
        title="Billing Amount Distribution",
        template="plotly_white"
    )
    
    fig.update_traces(marker_color='#2e95cc', opacity=0.7)
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter, sans-serif"),
        title_font_size=16,
        title_x=0.5,
        xaxis_title="Billing Amount ($)",
        yaxis_title="Frequency"
    )
    
    return fig


@app.callback(
    Output('insurance-comparison', 'figure'),
    Input('gender-filter', 'value')
)
def update_insurance_comparison(selected_gender):
    filtered_df = df[df['Gender'] == selected_gender] if selected_gender else df
    
    # Group by insurance provider and medical condition, sum billing amounts
    insurance_data = filtered_df.groupby(['Insurance Provider', 'Medical Condition'])['Billing Amount'].sum().reset_index()
    
    fig = px.bar(
        insurance_data, 
        x="Insurance Provider", 
        y="Billing Amount", 
        color="Medical Condition", 
        barmode="group",
        title="Total Billing Amount by Insurance Provider and Medical Condition",
        color_discrete_sequence=px.colors.qualitative.Pastel,
        template="plotly_white"
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter, sans-serif"),
        title_font_size=16,
        title_x=0.5,
        xaxis_title="Insurance Provider",
        yaxis_title="Total Billing Amount ($)",
        legend_title="Medical Condition"
    )
    
    return fig


# Run the app
if __name__ == "__main__":
    app.run(debug=True)