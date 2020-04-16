import React from "react";
import {serverApi} from "../../../config"
import "./TeamsTableComponent.css"
import {Link} from "react-router-dom"

class TeamsTableComponent extends React.Component {

    constructor(props) {
        super(props);

    }

    deleteTeam = (teamName) => {
        fetch(`http://${serverApi}/api/team/${teamName}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
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
        return this.props.teams.map(team => {
            return (
                <tr key={team.teamName}>
                    <td scope="col">
                        <Link to={`/teams/${team.teamName}`}>
                            {team.teamName}
                        </Link>
                    </td>

                    <td>
                        {team.workersCount}
                    </td>


                    <td>
                        <button className="btn btn-danger" onClick={() => this.deleteTeam(team.teamName)}>Delete
                            Team
                        </button>
                    </td>

                </tr>);
        });
    }

    render() {
        return (
            <div id={"TeamTable"}>
                <table className="table table-hover">
                    <thead className={"thead-light"}>
                    <tr>
                        <td>Team Name</td>
                        <td>Workers Count</td>
                        <td>Delete button</td>
                    </tr>
                    </thead>

                    <tbody>
                    {this.createRows()}
                    </tbody>

                </table>

            </div>);
    }
}

export default TeamsTableComponent;