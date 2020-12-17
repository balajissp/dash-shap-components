import dash
import dash_html_components as html

from dash_shap_components import ForcePlot

external_stylesheets = ["https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"]
external_scripts = ["https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"]
app = dash.Dash(__name__, external_scripts=external_scripts, external_stylesheets=external_stylesheets)


def get_plot(gid):
    return ForcePlot(
        id=gid,
        className='col-md-6',
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
        labelMargin=1000,
        plot_cmap=['#DB0011', '#F0F0F0'],
    )


# @app.callback(Output('output', 'children'), [Input('sample-plot', 'children')])
# def display_output(value):
#     return 'You have entered {}'.format(value)


app.layout = html.Div([
    html.Div([
        get_plot('sample11'),
        get_plot('sample21'),
    ], className='row'),
    html.Div([
        get_plot('sample12'),
        get_plot('sample22'),
    ], className='row'),
], className='container-fluid')

if __name__ == '__main__':
    app.run_server(debug=True)
