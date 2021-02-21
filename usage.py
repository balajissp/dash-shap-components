import json
import random

import dash
import dash_html_components as html
from dash.dependencies import Output, Input

from dash_shap_components import ForcePlot, ForceArrayPlot

external_stylesheets = ["https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"]
external_scripts = ["https://code.jquery.com/jquery-3.5.1.min.js",
                    "https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"]
app = dash.Dash(
    __name__,
    external_scripts=external_scripts,
    external_stylesheets=external_stylesheets
)

with open('./docs/demo.json', 'r') as f:
    data = json.loads(f.read())


def get_plot(gid, title=None):
    explanation = data['explanations'][random.randint(0, len(data['explanations']))]
    return ForcePlot(
        id=gid,
        className='col-md-12',
        title=title,
        baseValue=data['baseValue'],
        link=data['link'],
        featureNames=data['featureNames'],
        outNames=data['outNames'],
        features=explanation['features'],
        hideBaseValueLabel=False,
        hideBars=False,
        labelMargin=0,
        plot_cmap=['#DB0011', '#000FFF'],
        # style={'width': '50vw'},
    )


def get_array_plot(gid, title=None):
    return ForceArrayPlot(
        id=gid,
        className='col-md-12',
        title=title,
        baseValue=data['baseValue'],
        link=data['link'],
        featureNames=data['featureNames'],
        outNames=data['outNames'],
        explanations=data['explanations'][:200],
    )


app.layout = html.Div([
    html.Div([
        get_plot('sample11'),
        get_array_plot('sample21', 'Force Array Plot'),
    ], className='row'),
    html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
    html.Div([
        get_plot('sample12', 'Force Plot'),
        get_array_plot('sample22'),
    ], className='row'),
    html.Div(id='callback-output'),
], className='container-fluid')


@app.callback(
    Output('callback-output', 'children'),
    [Input('sample21', 'clickData')],
)
def echo_click_data(clickData):
    return html.P(['Force Array Plot Internal State:', html.Br(), f'{clickData=}'])


if __name__ == '__main__':
    app.run_server(debug=True)
