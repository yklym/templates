import React from "react";
import {serverApi} from "../../../config"

class WorkersTableComponent extends React.Component{
    constructor(props) {
        super(props);

        this.state={
            workers : [],
        }
    }

    componentDidMount() {
        this.fetchContent();
    }

     fetchContent = () => {
        fetch(`http://${serverApi}/api/team/${this.props.teamName}`, {
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
            this.setState({workers: parsedJson});
        }).catch(e => {
            console.log(e);
        })
    };

    createRows = () => {
        console.log(this.state)
        return this.state.workers.map(worker => {
            return (
                <tr key={worker.workerName}>
                    <td scope="col">
                            {worker.workerName}
                    </td>
                    <td scope="col">
                            {worker.position}
                    </td>
                    <td scope="col">
                            {worker.hoursLeft}
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
                        <td>Hours left</td>
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
