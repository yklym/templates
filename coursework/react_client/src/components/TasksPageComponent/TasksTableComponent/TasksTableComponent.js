import React from "react";
import {serverApi} from "../../../config"

class TasksTableComponent extends React.Component{
    constructor(props) {
        super(props);
    }
    deleteTask = (taskName)=>{
        fetch(`http://${serverApi}/api/task/${taskName}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => {
            if (res.status === 200) {
                this.props.updateTable();
            } else {
                console.log(res);
            }
        }).catch(e => {
            console.log(e);
        })
    };

    createRows = () => {
        return this.props.tasks.map(task => {
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
                            <button className="btn btn-danger" onClick={()=>this.deleteTask(task.taskName)}>Delete task</button>
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
                        <td>Delete task</td>
                    </tr>
                    </thead>

                    <tbody>
                        {this.createRows()}
                    </tbody>

                </table>

            </div>);
    }
}

export default TasksTableComponent;
