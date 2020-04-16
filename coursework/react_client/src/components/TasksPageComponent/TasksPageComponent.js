import React from "react";
import {Collapse} from "react-bootstrap"
import TasksTableComponent from "./TasksTableComponent/TasksTableComponent";
import CreateTaskForm from "./CreateTaskForm/CreateTaskForm";
import {serverApi} from "../../config";


class TasksPageComponent extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            openForm: false,
            openButtons : false,
            tasks : []
        };
        console.log(this.state)
    }
    componentDidMount() {
        this.fetchContent();
    }

     fetchContent = () => {
        fetch(`http://${serverApi}/api/task`, {
            method: 'GET', // или 'PUT'
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => {
            if(res.status !== 200){
                return new Promise.reject("error code");
            }
            return res.json();
        }).then(parsedJson => {
            this.setState({tasks: parsedJson});
        }).catch(e => {
            console.log(e);
        })
    };

    render() {
        return (
            <main>
                <h2 className={"teamPageHeader"}>Tasks</h2>


                <TasksTableComponent tasks={this.state.tasks} updateTable={() => this.fetchContent()}/>

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
                                <CreateTaskForm updateTable={() => this.fetchContent()}/>

                            </div>
                        </Collapse>
                    </div>

                    <div>
                        <p>
                            <a className="btn btn-success" data-toggle="collapse" role="button"
                               aria-expanded="false" aria-controls="collapseButtons" a={""}
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

export default TasksPageComponent;