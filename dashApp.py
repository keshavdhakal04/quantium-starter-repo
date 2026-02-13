from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# 1. Initialize the Dash app
app = Dash(__name__)

# 2. Data Preparation
df = pd.read_csv('data/formatted_output.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by="date")

# 3. Visualization
fig = px.line(
    df, 
    x="date", 
    y="sales", 
    title="Pink Morsel Sales Analysis",
    labels={"date": "Transaction Date", "sales": "Total Sales (USD)"},
    template="plotly_white"
)

# Marker for the price increase
fig.add_vline(x='2021-01-15', line_dash="dash", line_color="#FF4136") 

fig.add_annotation(
    x='2021-01-15', 
    y=df['sales'].max(),
    text="Price Increase", 
    showarrow=False, 
    yshift=10
)

# 4. App Layout (Styled according to dash.plotly.com/layout)
# We use a dictionary for common colors to keep the style consistent
colors = {
    'background': '#F9F9F9',
    'text': '#2C3E50',
    'header': '#1A252F'
}

app.layout = html.Div(
    style={'backgroundColor': colors['background'], 'padding': '40px', 'fontFamily': 'sans-serif'},
    children=[
        
        # Header - Titles the visualiser
        html.H1(
            children='Pink Morsel Visualiser',
            style={
                'textAlign': 'center',
                'color': colors['header'],
                'fontWeight': 'bold'
            }
        ),

        # Subtext / Context
        html.Div(
            children='Analyzing the impact of the price increase on 15th January, 2021.',
            style={
                'textAlign': 'center',
                'color': colors['text'],
                'marginBottom': '40px'
            }
        ),

        # The Graph Component
        html.Div(
            style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px', 'boxShadow': '0px 4px 6px rgba(0,0,0,0.1)'},
            children=[
                dcc.Graph(
                    id='sales-line-chart',
                    figure=fig
                )
            ]
        )
    ]
)

# 5. Run the App
if __name__ == '__main__':
    # Using app.run for compatibility with modern Dash versions
    app.run(debug=True)