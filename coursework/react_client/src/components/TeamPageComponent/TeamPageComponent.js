import React from "react";
import {Collapse} from "react-bootstrap"
import WorkersTableComponent from "./WorkersTableComponent/WorkersTableComponent"
import CreateWorkerForm from "./CreateWorkerForm/CreateWorkerForm"
import "./TeamPageComponent.css"

class TeamPageComponent extends React.Component {
    constructor(props) {
        super(props);

        let queryStrArr = this.props.location.pathname.split("/");
        let teamName = queryStrArr[queryStrArr.length - 1];
        console.log(teamName)

        this.state = {
            teamName: teamName,
            openForm: false,
            openButtons: false,
        };
        console.log(this.state)
    }

    render() {
        return (
            <main>
                <h2 className={"teamPageHeader"}>{`Team ${this.state.teamName}`}</h2>


                <WorkersTableComponent teamName={this.state.teamName}/>

                <h3 className={"teamPageHeader"}>Managing Panel:</h3>

                <div className={"adminPanel"}>
                    <div>

                        <p>
                            <a className="btn btn-secondary" data-toggle="collapse" href="#collapseForm" role="button"
                               aria-expanded="false" aria-controls="collapseForm"
                               onClick={() => this.setState({openForm: !this.state.openForm})}>
                                Create worker
                            </a>
                        </p>

                        <Collapse in={this.state.openForm}>
                            <div className="collapse" id="collapseForm">
                                <CreateWorkerForm teamName={this.state.teamName}
                                                  updateTable={() => this.setState({"upd": true})}/>

                            </div>
                        </Collapse>
                    </div>

                    <div>
                        <p>
                            <a className="btn btn-success" data-toggle="collapse" href="#collapseButtons" role="button"
                               aria-expanded="false" aria-controls="collapseButtons"
                               onClick={() => this.setState({openButtons: !this.state.openButtons})}>
                                Other functions
                            </a>
                        </p>

                        <Collapse in={this.state.openButtons}>
                            <div className="collapse collapseButtons" id="collapseButtons">
                                {/*TODO REFRESH TEAM*/}
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

export default TeamPageComponent;