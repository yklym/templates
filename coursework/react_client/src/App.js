import React, {Component} from 'react';
import {Route, Switch} from 'react-router-dom'

import TeamsPageComponent from "./components/TeamsPageComponent/TeamsPageComponent.js"
import TeamPageComponent from "./components/TeamPageComponent/TeamPageComponent.js"
import TasksPageComponent from "./components/TasksPageComponent/TasksPageComponent";


class App extends Component {
    body;

    render() {
        return (
            <>
                <Switch>
                    <Route exact path="/teams" component={TeamsPageComponent}/>
                    <Route exact path="/tasks" component={TasksPageComponent}/>
                    <Route exact path="/teams/:name" component={TeamPageComponent}/>

                </Switch>
            </>
        )

    }
}

export default App;
