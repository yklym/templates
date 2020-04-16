import React from "react";
import {serverApi} from "../../../config";

class WorkersTableComponent extends React.Component {
    constructor(props) {
        super(props);
    }

    deleteWorker = (teamName, workerName, position)=>{
      fetch(`http://${serverApi}/api/worker/${workerName}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body : JSON.stringify({
                "teamName" : teamName,
                "workerName" : workerName,
                "position" : position,
            })
        }).then(res => {
            if (res.status === 200) {
                this.props.updateParent();
            } else {
                console.log(res);
            }
        }).catch(e => {
            console.log(e);
        })
    };

    createRows = () => {
        return this.props.workers.map(worker => {
            return (
                <tr key={worker.workerName}>
                    <td>
                        {worker.workerName}
                    </td>
                    <td>
                        {worker.position}
                    </td>
                    <td>
                        {worker.experience}
                    </td>
                    <td>
                        {worker.hoursLeft}
                    </td>
                    <td>
                        <button className="btn btn-danger" onClick={() => this.deleteWorker(this.props.teamName, worker.workerName, worker.position )}>Delete</button>
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
                        <td>Worker Name</td>
                        <td>Position</td>
                        <td>Experience</td>
                        <td>Hours left</td>
                        <td>Delete worker</td>
                    </tr>
                    </thead>

                    <tbody>
                    {this.createRows()}
                    </tbody>

                </table>

            </div>);
    }
}

export default WorkersTableComponent;
