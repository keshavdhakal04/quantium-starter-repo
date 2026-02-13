from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# 1. Initialize the Dash app
app = Dash(__name__)

# 2. Data Preparation
df = pd.read_csv('data/formatted_output.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by="date")

# 3. App Layout
app.layout = html.Div(style={'backgroundColor': '#F8F9FB', 'padding': '40px', 'fontFamily': 'sans-serif'}, children=[
    html.H1("Pink Morsel Sales Visualiser", style={'textAlign': 'center', 'color': '#1A252F'}),

    # The Radio Button Component (from dash.plotly.com/layout)
    html.Div(style={'textAlign': 'center', 'padding': '20px'}, children=[
        dcc.RadioItems(
            id='region-picker',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            inline=True
        ),
    ]),

    dcc.Graph(id='sales-graph')
])

# 4. Callback
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-picker', 'value')
)
def update_graph(selected_region):
    # Filter data
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    # Create figure
    fig = px.line(filtered_df, x="date", y="sales", template="plotly_white")
    
    # Add marker with Adobe Color inspired Coral (#E74C3C)
    fig.add_vline(x='2021-01-15', line_dash="dash", line_color="#E74C3C")
    
    return fig

# 5. Run the App
if __name__ == '__main__':
    # Using app.run for compatibility with modern Dash versions
    app.run(debug=True)