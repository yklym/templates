import React from "react";
import {serverApi} from "../../../config";
import "./CreateTaskForm.css"

class CreateTaskForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            juniorEst: 5,
            middleEst: 5,
            seniorEst: 5,

            taskName: "",

            accessLevel: "junior",
        }
    }

    handleInputChange = (event) => {
        let newObj = {};
        newObj[event.target.name] = event.target.value;
        this.setState(newObj);
    };

    handleSubmit = (event) => {
        event.preventDefault();
        fetch(`http://${serverApi}/api/task`, {
            method: 'POST',
            body: JSON.stringify(this.state),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => {
            if (res.status === 201) {
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
                    <label htmlFor="taskName">Task Name:</label>
                    <input type="text" className="form-control" id="taskName" name={"taskName"}
                           onChange={this.handleInputChange}
                           placeholder="Enter name" value={this.state.taskName}/>
                    <small className="form-text text-muted">No impact at all)))</small>
                </div>

                <div className="form-group">

                    <label htmlFor={"accessLevel"}> Access level:</label>
                    <br/>
                    <select className="form-control" id={"accessLevel"} value={this.state.accessLevel}
                            onChange={this.handleInputChange} name={"accessLevel"}>
                        <option value={"junior"}>Junior</option>
                        <option value={"middle"}>Middle</option>
                        <option value={"senior"}>Senior</option>
                    </select>
                </div>

                <section>
                    <label htmlFor={"juniorEst"}> Junior estimate:</label>

                    <div className="form-group estimateInputs">

                        <br/>
                        <input value={this.state.juniorEst} onChange={this.handleInputChange} name="juniorEst"
                               type="range"
                               className="custom-range" min="0" max="20" step="1"/>
                        <input value={this.state.juniorEst} onChange={this.handleInputChange} name="juniorEst"
                               type="number"
                               id="juniorEst" min="0" max="20" step="1"/>
                    </div>
                </section>

                <section>
                    <label htmlFor={"middleEst"}> Middle estimate:</label>

                    <div className="form-group estimateInputs">

                        <br/>
                        <input value={this.state.middleEst} onChange={this.handleInputChange} name="middleEst"
                               type="range"
                               className="custom-range"  min="0" max="20" step="1"/>
                        <input value={this.state.middleEst} onChange={this.handleInputChange} name="middleEst"
                               type="number"
                               id="middleEst" min="0" max="20" step="1"/>
                    </div>
                </section>

                <section>
                    <label htmlFor={"seniorEst"}> Senior estimate:</label>

                    <div className="form-group estimateInputs">

                        <br/>
                        <input value={this.state.seniorEst} onChange={this.handleInputChange} name="seniorEst"
                               type="range"
                               className="custom-range" id="customRange1" min={"0"} max={"20"} step={"1"}/>
                        <input value={this.state.seniorEst} onChange={this.handleInputChange} name="seniorEst"
                               type="number"
                               id="seniorEst" min={"0"} max={"20"} step={"1"}/>
                    </div>
                </section>

                <button type="submit" className="btn btn-primary">Create worker</button>
            </form>
        );
    }


}

export default CreateTaskForm;