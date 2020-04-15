import React, {Component} from 'react';
import TeamTableComponent from "./teamTable/TeamTableComponent"

import "./MainComponent.css"
class TeamsPageComponent extends Component {
    render() {
        return (
            <main>
                <h2>
                    My app
                </h2>
                <TeamTableComponent />

            </main>
        );
    }
}

export default TeamsPageComponent;
