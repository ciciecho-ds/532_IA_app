from dash import Dash, html, dcc, Input, Output
import altair as alt
from vega_datasets import data


iris = data.iris()

app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

server = app.server

app.layout = html.Div([
    html.Iframe(
        id='scatter',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='xcol-widget',
        value='sepalLength',
        options=[{'label': col, 'value': col} for col in iris.columns])])

@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol-widget', 'value'))

def plot_altair(xcol):
    chart = alt.Chart(iris).mark_point().encode(
        x=xcol,
        y='sepalWidth',
        tooltip='sepalLength').interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)
