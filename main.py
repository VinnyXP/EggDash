import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)
app.title = 'Egg Dash'

data = (
    pd.read_csv('eggs.csv')
)

egg_year = data.columns[1:]
dropdown_options = [{'label': year, 'value': year} for year in egg_year]

@app.callback(
    Output('bar-graph', 'figure'),
    Input('year-dropdown', 'value')
)
def update__bar_graph(selected_year):
    filtered_df = data[['State/Union Territory', selected_year]]
    fig = px.bar(filtered_df, x='State/Union Territory', y=selected_year, barmode="group", text_auto=True,  title=f"Egg Production {selected_year}")
    fig.update_layout(autotypenumbers='convert types')
    fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total ascending'})
    fig.update_traces(width=0.8)
    return fig

app.layout = html.Div(
    children=[
    html.H1(
        children='Egg Production in India',
        style={
            'textAlign': 'center'
        }
    ),
    html.Div(children='''
        Number of eggs produced in yearly intervals.
    '''),
    dcc.Dropdown(
        id='year-dropdown',
        options=dropdown_options,
        value=egg_year[0] 
    ),
    html.Div(
        dcc.Graph(id='bar-graph')
    )
]
)

if __name__ == '__main__':
    app.run_server(debug=True)