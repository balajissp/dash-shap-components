/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';

import { ForceArrayPlot } from '../lib';

class App extends Component {

    constructor() {
        super();
        this.state = {
          baseValue: 0.0,
          link: "identity",
          featureNames: {
            "0": "Blue",
            "1": "Red",
            "2": "Green",
            "3": "Orange"
          },
          outNames: ["color rating"],
          explanations: [
            {
              outValue: -1.5,
              simIndex: 1,
              features: {
                "0": { value: 1.0, effect: 1.0 },
                "1": { value: 0.0, effect: 0.5 },
                "2": { value: 2.0, effect: -2.5 },
                "3": { value: 2.0, effect: -0.5 }
              }
            },
            {
              outValue: -0.5,
              simIndex: 0,
              features: {
                "0": { value: 1.0, effect: 1.0 },
                "1": { value: 0.0, effect: 0.5 },
                "2": { value: 1.0, effect: -1.5 },
                "3": { value: 2.0, effect: -0.5 }
              }
            },
            {
              outValue: 0,
              simIndex: 2,
              features: {
                "0": { value: 1.5, effect: 1.5 },
                "1": { value: 0.0, effect: 0.5 },
                "2": { value: 1.0, effect: -1.5 },
                "3": { value: 2.0, effect: -0.5 }
              }
            }
          ]
        };
        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    render() {
        return <ForceArrayPlot setProps={this.setProps} {...this.state} />
    }
}

export default App;
