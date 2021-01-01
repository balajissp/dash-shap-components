# AUTO GENERATED FILE - DO NOT EDIT

export ''_forcearrayplot

"""
    ''_forcearrayplot(;kwargs...)

A ForceArrayPlot component.
The ForceArrayPlot component is used to visualize the shapley contributions
to multiple predictions made by a tree-based ML model. This is a wrapper on
top of React implementation published in shapjs package.
Read more about the component here: https://github.com/slundberg/shap
Keyword arguments:
- `id` (String; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique to the component.
- `style` (Dict; optional): Inline css of each element
- `title` (String; optional): Plot title
- `className` (String; optional): html class associated with the component, used for styling purposes
- `baseValue` (Real; optional): same as explainer.expected_value
- `plot_cmap` (a value equal to: 'RdBu', 'GnPR', 'CyPU', 'PkYg', 'DrDb', 'LpLb', 'YlDp', 'OrId' | Array of Strings; optional): The colors used for shap contributions that increase/decrease the prediction value.
Should be one of:
-- default colour combinations RdBu, GnPR, CyPU, PkYg, DrDb, LpLb, YlDp, OrId
-- list of two hex codes, e.g., ["#AAAA11", "#6633CC"]
-- list of two rgb values, e.g., ["rgb(255, 13, 87)", "rgb(30, 136, 229)"]
- `link` (a value equal to: 'identity', 'logit'; optional): either 'identity' or 'logit'
- `featureNames` (Dict with Strings as keys and values of type String; optional): Labels corresponding to each feature, should have same set of keys as "features" prop
- `outNames` (Array of Strings; optional): Single element list of prediction variable name.
- `labelMargin` (Real; optional): Margin (in px) for labels on top of the plot
- `ordering_keys` (Array of Bool | Real | String | Dict | Arrays; optional): X-Axis label for each point
- `ordering_keys_time_format` (String; optional): Formatting for temporal axes, one of d3-time-formats
- `explanations` (optional): List of predictions, where each prediction is a dictionary
describing the predicted value, similarity index and shapley
contributions of each feature. explanations has the following type: Array of lists containing elements 'outValue', 'simIndex', 'features'.
Those elements have the following types:
  - `outValue` (Real; required)
  - `simIndex` (Bool | Real | String | Dict | Array; required)
  - `features` (Dict; required)s
- `clickData` (Dict; optional): attribute for attaching callbacks on click events
"""
function ''_forcearrayplot(; kwargs...)
        available_props = Symbol[:id, :style, :title, :className, :baseValue, :plot_cmap, :link, :featureNames, :outNames, :labelMargin, :ordering_keys, :ordering_keys_time_format, :explanations, :clickData]
        wild_props = Symbol[]
        return Component("''_forcearrayplot", "ForceArrayPlot", "dash_shap_components", available_props, wild_props; kwargs...)
end

