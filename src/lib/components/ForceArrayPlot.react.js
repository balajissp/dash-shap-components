import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {AdditiveForceArrayVisualizer} from 'shapjs';
import './css/force.css';

// eslint-disable-next-line valid-jsdoc
/**
 * The ForceArrayPlot component is used to visualize the shapley contributions
 * to multiple predictions made by a tree-based ML model. This is a wrapper on
 * top of React implementation published in shapjs package.
 * Read more about the component here: https://github.com/slundberg/shap
 */
export default class ForceArrayPlot extends Component {
    constructor(props) {
        super(props);
        this.state = {...this.props};
        this.clickDataCapture = this.clickDataCapture.bind(this);
    }

    clickDataCapture() {
        var clickIndex = this.el.nearestExpIndex;
        var expl = this.state.explanations[clickIndex];
        this.setState({'clickData': expl});
        if (this.props.setProps) {
            this.props.setProps({'clickData': expl});
        }
    }

//    componentDidMount() {
//        console.log(this.el.svg);
//        removeEventListener('click', this.el.svg.on('click'));
//        console.log(this.el.svg.on('click'));
//    }

    render() {
        return (
            <div id={this.state.id} className={this.state.className} style={this.state.style}>
                <span
                style={{
                    fontWeight:"bold",
                    width:"100%",
                    textAlign:"center",
                    display:"block",
                    fontSize:"15",
                    }}
                >{this.state.title}</span>
                <div className="dash-force-plot" onClickCapture={this.clickDataCapture}>
                    <AdditiveForceArrayVisualizer ref={el => this.el = el} {...this.state} />
                </div>
            </div>
        );
    }
}

ForceArrayPlot.propTypes = {
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
     * Labels corresponding to each feature, should have same set of keys as "features" prop
     */
    featureNames: PropTypes.objectOf(PropTypes.string),

    /**
     * Single element list of prediction variable name.
     */
    outNames: PropTypes.arrayOf(PropTypes.string),

    /**
     * Margin (in px) for labels on top of the plot
     */
    labelMargin: PropTypes.number,

    /**
     *  X-Axis label for each point
     */
    ordering_keys: PropTypes.arrayOf(PropTypes.any),

    /**
     * Formatting for temporal axes, one of d3-time-formats
     */
    ordering_keys_time_format: PropTypes.string,

    /**
     * List of predictions, where each prediction is a dictionary
     * describing the predicted value, similarity index and shapley
     * contributions of each feature
     */
    explanations: PropTypes.arrayOf(
        PropTypes.shape({
            outValue: PropTypes.number.isRequired,
            simIndex: PropTypes.any.isRequired,
            features: PropTypes.object.isRequired,
        })
    ),

    /**
     * attribute for attaching callbacks on click events
     */
    clickData: PropTypes.object
};

/*
    hacky approach to suppress alerts from shapjs package
    TODO: change from anonymous function in original implementation!
*/
(function(proxied) {
  window.alert = function() {
    if (0 <= arguments[0].search("Ordering by category names is not yet supported.")){
        console.warn(arguments[0]);
    } else if (0 > arguments[0].search("This original index of the sample you clicked is ")) {
        return proxied.apply(this, arguments);
    }
  };
})(window.alert);

(function(proxied) {
  console.log = function() {
    if (!((arguments.length == 3) && (arguments[0] == "found ")&& (arguments[2] == " used features"))
     && 0 > arguments[0].search("joinPoint")){
        return proxied.apply(this, arguments);
    }
  };
})(console.log);

ForceArrayPlot.defaultProps = {
    plot_cmap: 'RdBu',
    link: 'identity',
};
