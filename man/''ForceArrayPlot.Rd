% Auto-generated: do not edit by hand
\name{''ForceArrayPlot}

\alias{''ForceArrayPlot}

\title{ForceArrayPlot component}

\description{
The ForceArrayPlot component is used to visualize the shapley contributions to multiple predictions made by a tree-based ML model. This is a wrapper on top of React implementation published in shapjs package. Read more about the component here: https://github.com/slundberg/shap
}

\usage{
''ForceArrayPlot(id=NULL, style=NULL, title=NULL, className=NULL,
baseValue=NULL, plot_cmap=NULL, link=NULL,
featureNames=NULL, outNames=NULL, labelMargin=NULL,
ordering_keys=NULL, ordering_keys_time_format=NULL,
explanations=NULL)
}

\arguments{
\item{id}{Character. The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique to the component.}

\item{style}{Named list. Inline css of each element}

\item{title}{Character. Plot title}

\item{className}{Character. html class associated with the component, used for styling purposes}

\item{baseValue}{Numeric. same as explainer.expected_value}

\item{plot_cmap}{A value equal to: 'rdbu', 'gnpr', 'cypu', 'pkyg', 'drdb', 'lplb', 'yldp', 'orid' | list of characters. The colors used for shap contributions that increase/decrease the prediction value.
Should be one of:
-- default colour combinations RdBu, GnPR, CyPU, PkYg, DrDb, LpLb, YlDp, OrId
-- list of two hex codes, e.g., ["#AAAA11", "#6633CC"]
-- list of two rgb values, e.g., ["rgb(255, 13, 87)", "rgb(30, 136, 229)"]}

\item{link}{A value equal to: 'identity', 'logit'. either 'identity' or 'logit'}

\item{featureNames}{List with named elements and values of type character. Labels corresponding to each feature, should have same set of keys as "features" prop}

\item{outNames}{List of characters. Single element list of prediction variable name.}

\item{labelMargin}{Numeric. Margin (in px) for labels on top of the plot}

\item{ordering_keys}{Character. Custom ordering}

\item{ordering_keys_time_format}{Character. Formatting for temporal axes, one of d3-time-formats}

\item{explanations}{List of lists containing elements 'outvalue', 'simindex', 'features'.
those elements have the following types:
  - outvalue (numeric; optional)
  - simindex (logical | numeric | character | named list | unnamed list; optional)
  - features (named list; optional)s. }
}

\value{named list of JSON elements corresponding to React.js properties and their values}

