import React, {Component, lazy, Suspense} from 'react';
import PropTypes from 'prop-types';
import {AdditiveForceVisualizer} from 'shapjs';
import './css/force.css';

// eslint-disable-next-line valid-jsdoc
/**
 * The ForcePlot component is used to visualize the shapley contributions
 * to a single prediction made by a tree-based ML model. This is a simple
 * wrapper on top of React implementation published in shapjs package.
 * Read more about the component here: https://github.com/slundberg/shap
 */
export default class ForcePlot extends Component {

    render() {
        return (
            <div id={this.props.id} className={this.props.className} style={this.props.style}>
                <text
                style={{
                    fontWeight:"bold",
                    width:"100%",
                    textAlign:"center",
                    display:"block",
                    fontSize:"15",
                    }}
                >{this.props.title}</text>
                <div className="dash-force-plot">
                    <AdditiveForceVisualizer {...this.props} />
                </div>
            </div>
        );
    }
}

ForcePlot.propTypes = {
    /**
     * The ID of this component, used to identify dash components
     * in callbacks. The ID needs to be unique to the component.
     */
    id: PropTypes.string,

    /**
     * Inline css of each element
     */
    style: PropTypes.object,

    /**
     * Plot title
     */
    title: PropTypes.string,

    /**
     * html class associated with the component, used for styling purposes
     */
    className: PropTypes.string,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change.
     */
    setProps: PropTypes.func,

    /**
     * Values corresponding to each feature, should have same set of keys as "featureNames" prop
     */
    features: PropTypes.object,

    /**
     * same as explainer.expected_value
     */
    baseValue: PropTypes.number,

    /**
     * The colors used for shap contributions that increase/decrease the prediction value.
     * Should be one of:
     * -- default colour combinations RdBu, GnPR, CyPU, PkYg, DrDb, LpLb, YlDp, OrId
     * -- list of two hex codes, e.g., ["#AAAA11", "#6633CC"]
     * -- list of two rgb values, e.g., ["rgb(255, 13, 87)", "rgb(30, 136, 229)"]
     */
    plot_cmap: PropTypes.oneOfType([
            PropTypes.oneOf(['RdBu', 'GnPR', 'CyPU', 'PkYg', 'DrDb', 'LpLb', 'YlDp', 'OrId']),
            PropTypes.arrayOf(PropTypes.string),
        ]),
    /**
     * either 'identity' or 'logit'
     */
    link: PropTypes.oneOf(['identity', 'logit']),

    /**
     * Label corrresponding to each feature, should have same set of keys as "features" prop
     */
    featureNames: PropTypes.objectOf(PropTypes.string),

    /**
     * Single element list of prediction variable name.
     */
    outNames: PropTypes.arrayOf(PropTypes.string),

    /**
     * Show/hide the label above the base value
     */
    hideBaseValueLabel: PropTypes.bool,

    /**
     * Show/hide the color bars
     */
    hideBars: PropTypes.bool,

    /**
     * Margin (in px) for labels on top of the plot
     */
    labelMargin: PropTypes.number,
};

ForcePlot.defaultProps = {
    plot_cmap: 'RdBu',
    link: 'identity',
    hideBaseValueLabel: false,
    hideBars: false,
};
