# AUTO GENERATED FILE - DO NOT EDIT

''ForcePlot <- function(id=NULL, className=NULL, features=NULL, baseValue=NULL, plot_cmap=NULL, link=NULL, featureNames=NULL, outNames=NULL, hideBaseValueLabel=NULL, hideBars=NULL, labelMargin=NULL) {
    
    props <- list(id=id, className=className, features=features, baseValue=baseValue, plot_cmap=plot_cmap, link=link, featureNames=featureNames, outNames=outNames, hideBaseValueLabel=hideBaseValueLabel, hideBars=hideBars, labelMargin=labelMargin)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ForcePlot',
        namespace = 'dash_shap_components',
        propNames = c('id', 'className', 'features', 'baseValue', 'plot_cmap', 'link', 'featureNames', 'outNames', 'hideBaseValueLabel', 'hideBars', 'labelMargin'),
        package = 'dashShapComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
