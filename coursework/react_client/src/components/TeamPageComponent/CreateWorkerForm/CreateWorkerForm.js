import React from "react";
import {serverApi} from "../../../config";

class CreateWorkerForm extends React.Component{
    constructor(props) {
        super(props);
        this.state={
            workerPosition: "junior",
            workerName:"",
            teamName : this.props.teamName,
        }
    }
    handleInputChange = (event)=> {
        let newObj = {};
        newObj[event.target.name] = event.target.value;
        this.setState(newObj);
    };

    handleSubmit = (event)=>{
        event.preventDefault();
      fetch(`http://${serverApi}/api/worker`, {
            method: 'POST', // или 'PUT'
            body: JSON.stringify(this.state), // данные могут быть 'строкой' или {объектом}!
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => {
            if (res.status === 201){
                //IF All good
                console.log(this.props)
                this.props.updateTable();
            }
        }).catch(e => {
            console.log(e);
        })
    };

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <div className="form-group">
                    <label htmlFor="workerName">Worker Name:</label>
                    <input type="text" className="form-control" id="workerName" name={"workerName"} onChange={this.handleInputChange}
                           placeholder="Enter name" value={this.state.workerName} />
                        <small id="emailHelp" className="form-text text-muted">No impact at all)))</small>
                </div>

                <select className="form-control" value={this.state.workerPosition} onChange={this.handleInputChange} name={"workerPosition"}>
                    <option value={"Junior"}>Junior</option>
                    <option value={"Middle"}>Middle</option>
                    <option value={"Senior"}>Senior</option>
                </select>

                <button type="submit" className="btn btn-primary">Create worker</button>
            </form>
        );
    }


}

export default CreateWorkerForm;