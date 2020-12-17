% Auto-generated: do not edit by hand
\name{''ForcePlot}

\alias{''ForcePlot}

\title{ForcePlot component}

\description{
The ForcePlot component is used to visualize the shapley contributions
}

\usage{
''ForcePlot(id=NULL, className=NULL, features=NULL, baseValue=NULL,
plot_cmap=NULL, link=NULL, featureNames=NULL, outNames=NULL,
hideBaseValueLabel=NULL, hideBars=NULL, labelMargin=NULL)
}

\arguments{
\item{id}{Character. The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique to the component.}

\item{className}{Character. html class associated with the component, used for styling purposes}

\item{features}{Named list. Values corrresponding to each feature, should have same set of keys as "featureNames" prop}

\item{baseValue}{Numeric. same as explainer.expected_value}

\item{plot_cmap}{A value equal to: 'rdbu', 'gnpr', 'cypu', 'pkyg', 'drdb', 'lplb', 'yldp', 'orid' | list of characters. The colors used for shap contributions that increase/decrease the prediction value.
Should be one of:
-- default colour combinations RdBu, GnPR, CyPU, PkYg, DrDb, LpLb, YlDp, OrId
-- list of two hex codes, e.g., ["#AAAA11", "#6633CC"]
-- list of two rgb values, e.g., ["rgb(255, 13, 87)", "rgb(30, 136, 229)"]}

\item{link}{A value equal to: 'identity', 'logit'. either 'identity' or 'logit'}

\item{featureNames}{Named list. Label corrresponding to each feature, should have same set of keys as "features" prop}

\item{outNames}{List of characters. Single element list of prediction variable name.}

\item{hideBaseValueLabel}{Logical. Show/hide the label above the base value}

\item{hideBars}{Logical. Show/hide the color bars}

\item{labelMargin}{Numeric. Margin (in px) for labels on top of the plot}
}

\value{named list of JSON elements corresponding to React.js properties and their values}
