import React, {Component} from 'react';
import TeamsTableComponent from "./TeamTable/TeamsTableComponent"
import CreateTeamForm from "./CreateTeamForm/CreateTeamFrom";

import "./MainComponent.css"
import {serverApi} from "../../config";
import {Collapse} from "react-bootstrap";


class TeamsPageComponent extends Component {

    constructor() {
        super();

        this.state={
            teams : [],
            openForm: false,
            openButtons : false,
            openTasks : false,
        }
    }


    componentDidMount() {
        this.fetchContent();
    }

    fetchContent = () => {
        fetch(`http://${serverApi}/api/team`, {
            method: 'GET', // или 'PUT'
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => {
            return res.json();
        }).then(parsedJson => {
            this.setState({teams: parsedJson});
        }).catch(e => {
            console.log(e);
        })
    };

    render() {
        return (
            <main>
                <h2>
                    Teams
                </h2>

                <TeamsTableComponent updateParent={this.fetchContent} teams={this.state.teams}/>

                <div className="adminPanel">
                </div>
                <h3 className={"teamPageHeader"}>Managing Panel:</h3>


                <div className={"adminPanel"}>
                    <div>

                        <p>
                            <a className="btn btn-secondary" data-toggle="collapse" role="button"
                               aria-expanded="false" aria-controls="collapseForm"
                               onClick={() => this.setState({openForm: !this.state.openForm})}>
                                Create team
                            </a>
                        </p>

                        <Collapse in={this.state.openForm}>
                            <div className="collapse" id="collapseForm">
                                <CreateTeamForm updateParent={this.fetchContent}/>
                            </div>
                        </Collapse>
                    </div>

                    <div>
                        <p>
                            <a className="btn btn-success" data-toggle="collapse" role="button"
                               aria-expanded="false" aria-controls="collapseButtons"
                               onClick={() => this.setState({openButtons: !this.state.openButtons})}>
                                Other functions
                            </a>
                        </p>

                        <Collapse in={this.state.openButtons}>
                            <div className="collapse collapseButtons" id="collapseButtons">
                                <button type="button" className="btn btn-primary">Refresh workers</button>
                                <button type="button" className="btn btn-secondary">Secondary</button>
                                <button type="button" className="btn btn-success">Success</button>
                                <button type="button" className="btn btn-danger">Danger</button>
                                <button type="button" className="btn btn-warning">Warning</button>

                            </div>
                        </Collapse>
                    </div>
                </div>

            </main>
        );
    }
}

export default TeamsPageComponent;
