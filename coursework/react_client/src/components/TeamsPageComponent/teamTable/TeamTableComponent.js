import React from "react";
import {serverApi} from "../../../config"
import "./TeamTableComponent.css"
import {Link} from "react-router-dom"

class TeamTableComponent extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            teams: [],
            teamNameInputVal: '',
        };
    }

    componentDidMount() {
        this.fetchContent();
        console.log(this.state);
    }

    handleInputChange = (event) => {
        this.setState({teamNameInputVal: event.target.value});
    };

    fetchContent = () => {
        fetch(`http://${serverApi}/api/team`, {
            method: 'GET', // или 'PUT'
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => {
            return res.json();
        }).then(parsedJson => {
            this.setState({teams: parsedJson});
        }).catch(e => {
            console.log(e);
        })
    };

    createTeam = () => {
        fetch(`http://${serverApi}/api/team`, {
            method: 'POST', // или 'PUT'
            body: JSON.stringify({teamName: this.state.teamNameInputVal}), // данные могут быть 'строкой' или {объектом}!
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => {
            this.fetchContent()
        }).catch(e => {
            console.log(e);
        })
    };

    createRows = () => {
        return this.state.teams.map(teamName => {
            return (
                <tr key={teamName}>
                    <td scope="col">
                        <Link to={`/teams/${teamName}`}>
                            {teamName}
                        </Link>
                    </td>
                </tr>);
        });
    }

    render() {
        return (
            <div id={"teamTable"}>
                <table className="table table-hover">
                    <thead className={"thead-light"}>
                    <tr>
                        <td>Team Name</td>
                    </tr>
                    </thead>

                    <tbody>
                    {this.createRows()}
                    </tbody>

                </table>

                <div id={"createTeamForm"}>
                    <input type={"text"} value={this.state.teamNameInputVal} onChange={this.handleInputChange}/>
                    <button className="btn-primary" onClick={this.createTeam}> Create team</button>
                </div>

            </div>);
    }
}

export default TeamTableComponent;