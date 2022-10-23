from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

DATA_PATH = "./output.csv"
COLORS = {
    "bg-color": "#0d1117",
    "font": "#F5F5F5",
}

df = pd.read_csv(DATA_PATH, parse_dates=['date'], dayfirst=True)
df['date'] = df['date'].dt.to_period('M')
df = df.groupby([df['date'].astype(str), 'region'])['sales'].sum()

app = Dash(__name__)

app.layout = html.Div([
    html.H1(["Pink Morsel Visualizer"], id = 'header', style={
        "background-color": COLORS["bg-color"],
        "color": COLORS["font"],
        "border-radius": "20px"}),
    
     html.Div(dcc.Dropdown( id = 'dropdown',
        options = [
            {'label':'north', 'value':'north' },
            {'label': 'south', 'value':'south'},
            {'label': 'east', 'value':'east'},
            {'label': 'west', 'value':'west'},
            {'label': 'all', 'value':'all'}
            ],
        value = 'all')),

    html.Div(dcc.Graph(id='salesGraph'),
             style={
                "background-color": "#708090",
             })

], style={'width': '100%',
            "textAlign": "center",
            'display': 'inline-block', 
             "background-color": COLORS["bg-color"],
             "border-radius": "20px"})


@app.callback(
    Output('salesGraph', 'figure'),
    Input('dropdown', 'value'))

def update_graph(dropdown):
    if dropdown == 'all':
        dff = df
    else:
        dff = df[df.index.get_level_values('region').isin([dropdown])]

    fig = px.line(dff, x=dff.index.get_level_values(0), y='sales', color=dff.index.get_level_values('region'))
    fig.update_xaxes(title='Date')
    fig.update_layout(transition_duration=1000)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)