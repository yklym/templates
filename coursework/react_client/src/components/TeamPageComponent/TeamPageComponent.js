import React from "react";
import {Collapse} from "react-bootstrap"
import WorkersTableComponent from "./WorkersTableComponent/WorkersTableComponent"
import CreateWorkerForm from "./CreateWorkerForm/CreateWorkerForm"
import "./TeamPageComponent.css"
import {serverApi} from "../../config";
import TasksResolutionTable from "./TasksResolutionTable/TasksResolutionTable"


class TeamPageComponent extends React.Component {
    constructor(props) {
        super(props);

        let queryStrArr = this.props.location.pathname.split("/");
        let teamName = queryStrArr[queryStrArr.length - 1];

        this.state = {
            teamName: teamName,

            openForm: false,
            openButtons: false,

            workers: [],
        };
    }

    componentDidMount() {
        this.fetchContent();
    };

    refreshTeam = () => {
        fetch(`http://${serverApi}/api/team/refreshTeam/${this.state.teamName}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => {
            if (res.status === 200) {
                this.fetchContent();
            } else {
                return new Promise.reject("error code");
            }
        }).catch(e => {
            console.log(e);
        })
    };

    fetchContent = () => {
        fetch(`http://${serverApi}/api/team/${this.state.teamName}`, {
            method: 'GET', // или 'PUT'
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => {
            if (res.status !== 200) {
                return new Promise.reject("error code");
            }
            return res.json();
        }).then(parsedJson => {
            this.setState({workers: parsedJson});
        }).catch(e => {
            console.log(e);
        })
    };

    render() {
        return (
            <main>
                <h2 className={"teamPageHeader"}>{`Team ${this.state.teamName}`}</h2>


                <WorkersTableComponent teamName={this.state.teamName} updateParent={this.fetchContent}
                                       workers={this.state.workers}/>

                <h3 className={"teamPageHeader"}>Managing Panel:</h3>

                <div className={"adminPanel"}>
                    <div>

                        <p>
                            <a className="btn btn-secondary" data-toggle="collapse" role="button"
                               aria-expanded="false" aria-controls="collapseForm"
                               onClick={() => this.setState({openForm: !this.state.openForm})}>
                                Create worker
                            </a>
                        </p>

                        <Collapse in={this.state.openForm}>
                            <div className="collapse" id="collapseForm">
                                <CreateWorkerForm teamName={this.state.teamName}
                                                  updateTable={() => this.fetchContent()}/>

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
                                {/*TODO REFRESH TEAM*/}
                                <button type="button" className="btn btn-primary" onClick={this.refreshTeam}>Refresh
                                    workers
                                </button>
                                <button type="button" className="btn btn-secondary">Secondary</button>
                                <button type="button" className="btn btn-success">Success</button>
                                <button type="button" className="btn btn-danger">Danger</button>
                                <button type="button" className="btn btn-warning">Warning</button>

                            </div>
                        </Collapse>
                    </div>
                </div>

                <section id={"taskResolutionTable"}>

                    <h3> Task resolving</h3>

                    <TasksResolutionTable/>

                </section>
            </main>
        );
    }
}

export default TeamPageComponent;