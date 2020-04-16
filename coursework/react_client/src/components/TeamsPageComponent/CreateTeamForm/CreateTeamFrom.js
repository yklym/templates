import React from "react";

import {serverApi} from "../../../config";
import "./CreateTeamForm.css"

class CreateTeamForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            teamName : "",

        }
    }

    createTeam = (event) => {
        event.preventDefault();
        fetch(`http://${serverApi}/api/team`, {
            method: 'POST',
            body: JSON.stringify({teamName: this.state.teamName}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => {
            if(res.status === 201){
                this.props.updateParent()
            }
        }).catch(e => {
            console.log(e);
        })
    };


    handleInputChange = (event) => {
        let newObj = {};
        newObj[event.target.name] = event.target.value;
        this.setState(newObj);
    };


    render() {
        return (
            <form onSubmit={this.createTeam}>
                <div className="form-group">
                    <div id={"createTeamForm"}>
                        <label htmlFor="teamName">Team Name:</label>
                        <br/>
                        <input type={"text"} value={this.state.teamName} name="teamName" id="teamName"
                               onChange={this.handleInputChange}/>

                        <small className="form-text text-muted">No impact at all)))</small>
                    </div>
                </div>
                <button type="submit" className="btn btn-primary" onClick={this.createTeam}>Create team</button>
            </form>
        );
    }


}

export default CreateTeamForm;