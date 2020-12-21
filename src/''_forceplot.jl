# AUTO GENERATED FILE - DO NOT EDIT

export ''_forceplot

"""
    ''_forceplot(;kwargs...)

A ForcePlot component.
The ForcePlot component is used to visualize the shapley contributions
to a single prediction made by a tree-based ML model. This is a simple
wrapper on top of React implementation published in shapjs package.
Read more about the component here: https://github.com/slundberg/shap
Keyword arguments:
- `id` (String; required): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique to the component.
- `style` (Dict; optional): Inline css of each element
- `title` (String; optional): Plot title
- `className` (String; optional): html class associated with the component, used for styling purposes
- `features` (Dict; required): Values corresponding to each feature, should have same set of keys as "featureNames" prop
- `baseValue` (Real; required): same as explainer.expected_value
- `plot_cmap` (a value equal to: 'RdBu', 'GnPR', 'CyPU', 'PkYg', 'DrDb', 'LpLb', 'YlDp', 'OrId' | Array of Strings; optional): The colors used for shap contributions that increase/decrease the prediction value.
Should be one of:
-- default colour combinations RdBu, GnPR, CyPU, PkYg, DrDb, LpLb, YlDp, OrId
-- list of two hex codes, e.g., ["#AAAA11", "#6633CC"]
-- list of two rgb values, e.g., ["rgb(255, 13, 87)", "rgb(30, 136, 229)"]
- `link` (a value equal to: 'identity', 'logit'; optional): either 'identity' or 'logit'
- `featureNames` (Dict with Strings as keys and values of type String; required): Label corrresponding to each feature, should have same set of keys as "features" prop
- `outNames` (Array of Strings; optional): Single element list of prediction variable name.
- `hideBaseValueLabel` (Bool; optional): Show/hide the label above the base value
- `hideBars` (Bool; optional): Show/hide the color bars
- `labelMargin` (Real; optional): Margin (in px) for labels on top of the plot
"""
function ''_forceplot(; kwargs...)
        available_props = Symbol[:id, :style, :title, :className, :features, :baseValue, :plot_cmap, :link, :featureNames, :outNames, :hideBaseValueLabel, :hideBars, :labelMargin]
        wild_props = Symbol[]
        return Component("''_forceplot", "ForcePlot", "dash_shap_components", available_props, wild_props; kwargs...)
end

