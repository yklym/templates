import React from "react";
import {Collapse} from "react-bootstrap"
import TasksTableComponent from "./TasksTableComponent/TasksTableComponent";

class TasksPageComponent extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            openForm: false,
        };
        console.log(this.state)
    }

    render() {
        return (
            <main>
                <h2 className={"teamPageHeader"}>Tasks</h2>


                <TasksTableComponent/>

                <h3 className={"teamPageHeader"}>Managing Panel:</h3>

                <div className={"adminPanel"}>
                    {/*<div>*/}
                    {/*    <p>*/}
                    {/*        <a className="btn btn-secondary" data-toggle="collapse" href="#collapseForm" role="button"*/}
                    {/*           aria-expanded="false" aria-controls="collapseForm"*/}
                    {/*           onClick={() => this.setState({openForm: !this.state.openForm})}>*/}
                    {/*            Create worker*/}
                    {/*        </a>*/}
                    {/*    </p>*/}

                    {/*    <Collapse in={this.state.openForm}>*/}
                    {/*        <div className="collapse" id="collapseForm">*/}
                    {/*            <CreateWorkerForm teamName={this.state.teamName}*/}
                    {/*                              updateTable={() => this.setState({"upd": true})}/>*/}

                    {/*        </div>*/}
                    {/*    </Collapse>*/}
                    {/*</div>*/}

                </div>
            </main>
        );
    }
}

export default TasksPageComponent;