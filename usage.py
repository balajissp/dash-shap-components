import dash
import dash_html_components as html
from dash.dependencies import Output, Input, State
import dash_core_components as dcc
from dash_shap_components import ForcePlot, ForceArrayPlot

# external_stylesheets = ["https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"]
# external_scripts = ["https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"]
app = dash.Dash(
    __name__,
    # external_scripts=external_scripts,
    # external_stylesheets=external_stylesheets
)


def get_plot(gid, title=None):
    return ForcePlot(
        id=gid,
        className='col-md-6',
        title=title,
        baseValue=100.0,
        link="identity",
        featureNames={
            "0": "Blue",
            "1": "Red",
            "2": "Green",
            "3": "Orange"
        },
        outNames=["color rating"],
        features={
            "0": {'value': 1.0, 'effect': 1.0},
            "1": {'value': 0.0, 'effect': 0.5},
            "2": {'value': 2.0, 'effect': -2.5},
            "3": {'value': 2.0, 'effect': -0.5}
        },
        hideBaseValueLabel=False,
        hideBars=False,
        labelMargin=0,
        plot_cmap=['#DB0011', '#000FFF'],
        style={'width': '50vw'},
    )


def get_array_plot(gid, title=None):
    return ForceArrayPlot(
        id=gid,
        className='col-md-6',
        title=title,
        baseValue=0.0,
        link="identity",
        featureNames={
            "0": "Blue",
            "1": "Red",
            "2": "Green",
            "3": "Orange"
        },
        outNames=["color rating"],
        explanations=[
            {
                'outValue': -1.5,
                'simIndex': 1,
                'features': {
                    "0": {'value': 1.0, 'effect': 1.0},
                    "1": {'value': 0.0, 'effect': 0.5},
                    "2": {'value': 2.0, 'effect': -2.5},
                    "3": {'value': 2.0, 'effect': -0.5}
                }
            },
            {
                'outValue': -0.5,
                'simIndex': 0,
                'features': {
                    "0": {'value': 1.0, 'effect': 1.0},
                    "1": {'value': 0.0, 'effect': 0.5},
                    "2": {'value': 1.0, 'effect': -1.5},
                    "3": {'value': 2.0, 'effect': -0.5}
                }
            },
            {
                'outValue': 0,
                'simIndex': 2,
                'features': {
                    "0": {'value': 1.5, 'effect': 1.5},
                    "1": {'value': 0.0, 'effect': 0.5},
                    "2": {'value': 1.0, 'effect': -1.5},
                    "3": {'value': 2.0, 'effect': -0.5}
                }
            }
        ],
    )


app.layout = html.Div([
    html.Div([
        get_plot('sample11'),
        get_array_plot('sample21', 'Entitled'),
    ], className='row'),
    html.Div([
        get_plot('sample12', 'Titled Plot'),
        get_array_plot('sample22'),
    ], className='row', style={'display': 'inline-flex'}),
    html.Div(id='callback-output'),
], className='container-fluid')


@app.callback(
    Output('callback-output', 'children'),
    [Input('sample22', 'clickData')],
    [State('sample22', 'explanations')]
)
def echo_click_data(clickData, explanations):
    return dcc.Markdown(f'{clickData=},\n\n {explanations=}')


if __name__ == '__main__':
    app.run_server(debug=True)
