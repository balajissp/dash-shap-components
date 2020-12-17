/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';

import { ForcePlot } from '../lib';

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
          features: {
            "0": { value: 1.0, effect: 1.0 },
            "1": { value: 0.0, effect: 0.5 },
            "2": { value: 2.0, effect: -2.5 },
            "3": { value: 2.0, effect: -0.5 }
          }
        };
        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    render() {
        return (
            <div>
                <ForcePlot
                    setProps={this.setProps}
                    {...this.state}
                />
            </div>
        )
    }
}

export default App;
