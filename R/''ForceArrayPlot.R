# AUTO GENERATED FILE - DO NOT EDIT

''ForceArrayPlot <- function(id=NULL, style=NULL, title=NULL, className=NULL, baseValue=NULL, plot_cmap=NULL, link=NULL, featureNames=NULL, outNames=NULL, labelMargin=NULL, ordering_keys=NULL, ordering_keys_time_format=NULL, explanations=NULL, clickData=NULL) {
    
    props <- list(id=id, style=style, title=title, className=className, baseValue=baseValue, plot_cmap=plot_cmap, link=link, featureNames=featureNames, outNames=outNames, labelMargin=labelMargin, ordering_keys=ordering_keys, ordering_keys_time_format=ordering_keys_time_format, explanations=explanations, clickData=clickData)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ForceArrayPlot',
        namespace = 'dash_shap_components',
        propNames = c('id', 'style', 'title', 'className', 'baseValue', 'plot_cmap', 'link', 'featureNames', 'outNames', 'labelMargin', 'ordering_keys', 'ordering_keys_time_format', 'explanations', 'clickData'),
        package = 'dashShapComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
