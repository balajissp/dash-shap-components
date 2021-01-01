# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ForceArrayPlot(Component):
    """A ForceArrayPlot component.
The ForceArrayPlot component is used to visualize the shapley contributions
to multiple predictions made by a tree-based ML model. This is a wrapper on
top of React implementation published in shapjs package.
Read more about the component here: https://github.com/slundberg/shap

Keyword arguments:
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique to the component.
- style (dict; optional): Inline css of each element
- title (string; optional): Plot title
- className (string; optional): html class associated with the component, used for styling purposes
- baseValue (number; optional): same as explainer.expected_value
- plot_cmap (a value equal to: 'RdBu', 'GnPR', 'CyPU', 'PkYg', 'DrDb', 'LpLb', 'YlDp', 'OrId' | list of strings; default 'RdBu'): The colors used for shap contributions that increase/decrease the prediction value.
Should be one of:
-- default colour combinations RdBu, GnPR, CyPU, PkYg, DrDb, LpLb, YlDp, OrId
-- list of two hex codes, e.g., ["#AAAA11", "#6633CC"]
-- list of two rgb values, e.g., ["rgb(255, 13, 87)", "rgb(30, 136, 229)"]
- link (a value equal to: 'identity', 'logit'; default 'identity'): either 'identity' or 'logit'
- featureNames (dict with strings as keys and values of type string; optional): Labels corresponding to each feature, should have same set of keys as "features" prop
- outNames (list of strings; optional): Single element list of prediction variable name.
- labelMargin (number; optional): Margin (in px) for labels on top of the plot
- ordering_keys (list of boolean | number | string | dict | lists; optional): X-Axis label for each point
- ordering_keys_time_format (string; optional): Formatting for temporal axes, one of d3-time-formats
- explanations (dict; optional): List of predictions, where each prediction is a dictionary
describing the predicted value, similarity index and shapley
contributions of each feature. explanations has the following type: list of dicts containing keys 'outValue', 'simIndex', 'features'.
Those keys have the following types:
  - outValue (number; required)
  - simIndex (boolean | number | string | dict | list; required)
  - features (dict; required)
- clickData (dict; optional): attribute for attaching callbacks on click events"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, title=Component.UNDEFINED, className=Component.UNDEFINED, baseValue=Component.UNDEFINED, plot_cmap=Component.UNDEFINED, link=Component.UNDEFINED, featureNames=Component.UNDEFINED, outNames=Component.UNDEFINED, labelMargin=Component.UNDEFINED, ordering_keys=Component.UNDEFINED, ordering_keys_time_format=Component.UNDEFINED, explanations=Component.UNDEFINED, clickData=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'style', 'title', 'className', 'baseValue', 'plot_cmap', 'link', 'featureNames', 'outNames', 'labelMargin', 'ordering_keys', 'ordering_keys_time_format', 'explanations', 'clickData']
        self._type = 'ForceArrayPlot'
        self._namespace = 'dash_shap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'style', 'title', 'className', 'baseValue', 'plot_cmap', 'link', 'featureNames', 'outNames', 'labelMargin', 'ordering_keys', 'ordering_keys_time_format', 'explanations', 'clickData']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(ForceArrayPlot, self).__init__(**args)
