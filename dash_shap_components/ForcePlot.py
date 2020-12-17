# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ForcePlot(Component):
    """A ForcePlot component.
The ForcePlot component is used to visualize the shapley contributions
to a single prediction made by a tree-based ML model. This is a simple
wrapper on top of React implementation published in shapjs package.
Read more about the component here: https://github.com/slundberg/shap

Keyword arguments:
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique to the component.
- className (string; optional): html class associated with the component, used for styling purposes
- features (dict; optional): Values corrresponding to each feature, should have same set of keys as "featureNames" prop
- baseValue (number; optional): same as explainer.expected_value
- plot_cmap (a value equal to: 'RdBu', 'GnPR', 'CyPU', 'PkYg', 'DrDb', 'LpLb', 'YlDp', 'OrId' | list of strings; default 'RdBu'): The colors used for shap contributions that increase/decrease the prediction value.
Should be one of:
-- default colour combinations RdBu, GnPR, CyPU, PkYg, DrDb, LpLb, YlDp, OrId
-- list of two hex codes, e.g., ["#AAAA11", "#6633CC"]
-- list of two rgb values, e.g., ["rgb(255, 13, 87)", "rgb(30, 136, 229)"]
- link (a value equal to: 'identity', 'logit'; default 'identity'): either 'identity' or 'logit'
- featureNames (dict; optional): Label corrresponding to each feature, should have same set of keys as "features" prop
- outNames (list of strings; optional): Single element list of prediction variable name.
- hideBaseValueLabel (boolean; default False): Show/hide the label above the base value
- hideBars (boolean; default False): Show/hide the color bars
- labelMargin (number; optional): Margin (in px) for labels on top of the plot"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, features=Component.UNDEFINED, baseValue=Component.UNDEFINED, plot_cmap=Component.UNDEFINED, link=Component.UNDEFINED, featureNames=Component.UNDEFINED, outNames=Component.UNDEFINED, hideBaseValueLabel=Component.UNDEFINED, hideBars=Component.UNDEFINED, labelMargin=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'features', 'baseValue', 'plot_cmap', 'link', 'featureNames', 'outNames', 'hideBaseValueLabel', 'hideBars', 'labelMargin']
        self._type = 'ForcePlot'
        self._namespace = 'dash_shap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'features', 'baseValue', 'plot_cmap', 'link', 'featureNames', 'outNames', 'hideBaseValueLabel', 'hideBars', 'labelMargin']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(ForcePlot, self).__init__(**args)
