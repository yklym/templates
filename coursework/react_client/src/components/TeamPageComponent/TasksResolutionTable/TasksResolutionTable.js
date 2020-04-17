import React from "react";

import {serverApi} from "../../../config"
import {Button, Modal} from "react-bootstrap";

class TasksResolutionTable extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            tasks: [],
            targetTask: this.createTaskExample(),
            showModal: false,
            resolutionMode: "fast",
        }
    }

    createTaskExample = () => {
        return {
            juniorEst: "1",
            middleEst: "2",
            seniorEst: "3",
            taskName: "Task Example"
        }
    };

    componentDidMount() {
        this.fetchTasks();
    };

    handleInputChange = (event) => {
        let newObj = {};
        newObj[event.target.name] = event.target.value;
        this.setState(newObj);
    };

    fetchTasks = () => {
        fetch(`http://${serverApi}/api/task`, {
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
            this.setState({tasks: parsedJson});
            console.log(parsedJson);
        }).catch(e => {
            console.log(e);
        })
    };

    createRows = () => {
        return this.state.tasks.map(task => {
            return (
                <tr key={task.taskName}>
                    <td>
                        {task.taskName}
                    </td>
                    <td>
                        {task.juniorEst}
                    </td>
                    <td>
                        {task.middleEst}
                    </td>
                    <td>
                        {task.seniorEst}
                    </td>
                    <td>
                        {task.accessLevel}
                    </td>
                    <td>
                        {/*ONCLICK*/}
                        <button className="btn btn-warning" onClick={() => this.showModal(task)}>Resolve task</button>
                    </td>
                </tr>);
        });
    };

    //Modal part
    showModal = (targetTask) => {
        if (!targetTask.log){
            targetTask.log = "";
        };
        this.setState({
            targetTask: targetTask,
            showModal: true,
        });
    };

    closeModal = () => {
        //    Handling errors
        this.setState({
            targetTask: this.createTaskExample(),
            showModal: false,
        })
    };

    submitModal = () => {

        fetch(`http://${serverApi}/api/resolveTask/${this.state.targetTask.taskName}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                    mode: this.state.resolutionMode,
                    team: this.props.teamName,
                }
            ),
        }).then(res => {
            console.log(res);
            if (res.status !== 200) {
                return Promise.reject("error code");
            } else {
                return res.json()
            }
        }).then(parsedRes => {
            console.log(parsedRes);
            if (parsedRes.err) {
                alert(`Fault!\n ${parsedRes.err}`);
            } else if (parsedRes.log) {
                alert(`Success!\n ${parsedRes.log}`);
            }
            this.closeModal();
            this.fetchTasks();
            this.props.updateParent();
        }).catch(e => {
            console.log(e);
        })
    };

    render() {
        return (
            <div id={"workersTable"}>
                <table className="table table-hover">
                    <thead className={"thead-light"}>
                    <tr>
                        <td>Name</td>
                        <td>Junior Estimate</td>
                        <td>Middle Estimate</td>
                        <td>Senior Estimate</td>
                        <td>Access level</td>
                        <td>Resolve task</td>
                    </tr>
                    </thead>

                    <tbody>
                    {this.createRows()}
                    </tbody>

                </table>

                <Modal show={this.state.showModal} onHide={this.closeModal}>
                    <Modal.Header closeButton>
                        <Modal.Title>{`Resolving ${this.state.targetTask.taskName}`}</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <p>{`Junior estimate left: [${this.state.targetTask.juniorEst}]`} </p>
                        <p>{`Middle estimate left: [${this.state.targetTask.middleEst}]`} </p>
                        <p>{`Senior estimate left: [${this.state.targetTask.seniorEst}]`} </p>

                        <Button variant="secondary">
                            Get task log
                        </Button>
                        <h5>Task log</h5>
                        <pre>{this.state.targetTask.log}</pre>
                        <br/>
                    </Modal.Body>
                    <Modal.Footer>

                        {/*onClick={}*/}
                        <p>Resolve it:</p>
                        <select className="form-control" value={this.state.resolutionMode}
                                onChange={this.handleInputChange} name={"resolutionMode"}>
                            <option value={"fast"}>as fast as possible</option>
                            <option value={"cheap"}>as cheap as possible</option>
                            <option value={"optimal"}>by fresh workers</option>
                            <option value={"tired"}>by tired workers</option>
                            <option value={"favourite"}>by more experienced workers</option>
                            <option value={"equal"}>by less experienced workers</option>
                        </select>

                        <Button variant="danger" onClick={this.closeModal}>
                            Cancel
                        </Button>

                        <Button variant="primary" onClick={() => {
                            this.submitModal();
                        }}>
                            {`Resolve by ${this.props.teamName}`}
                        </Button>
                    </Modal.Footer>
                </Modal>

            </div>);
    }
}

export default TasksResolutionTable;