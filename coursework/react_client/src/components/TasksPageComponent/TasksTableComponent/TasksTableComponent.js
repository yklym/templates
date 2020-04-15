import React from "react";
import {serverApi} from "../../../config"

class TasksTableComponent extends React.Component{
    constructor(props) {
        super(props);

        this.state={
            tasks : [],
        }
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

    createRows = () => {
        console.log(this.state)
        return this.state.tasks.map(task => {
            return (
                <tr key={task.taskName}>
                    <td scope="col">
                            {task.taskName}
                    </td>
                    <td scope="col">
                            {task.juniorEst}
                    </td>
                    <td scope="col">
                            {task.middleEst}
                    </td>
                    <td scope="col">
                            {task.seniorEst}
                    </td>
                    <td scope="col">
                            {task.accessLevel}
                    </td>
                </tr>);
        });
    }

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
