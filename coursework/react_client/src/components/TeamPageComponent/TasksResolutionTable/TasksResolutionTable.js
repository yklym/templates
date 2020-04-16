import React from "react";

import {serverApi} from "../../../config"

class TasksResolutionTable extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            tasks : []
        }
    }

    componentDidMount() {
        this.fetchTasks();
    }

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
                        <button className="btn btn-warning">Resolve task</button>
                    </td>
                </tr>);
        });
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

            </div>);
    }
}

export default TasksResolutionTable;