import React, { Component } from "react";
import "./addPortfolio.css";
import axios from "axios";

class AddPortfolio extends Component {
  state = {
    name: "",
  };

  handleNameChange = (event) => {
    this.setState({ name: event.target.value });
  };

  handleCurrencyChange = (event) => {
    this.setState({ currency: event.target.value });
  };

  handleSubmit = (event) => {
    const token = localStorage.getItem("userToken");
    event.preventDefault();
    axios
      .post("http://localhost:8000/api/create-portfolio", {
        usertoken: token,
        name: this.state.name,
      })
      .then(function (response) {
        if (response.status === 201) {
          alert("Portfolio Created");
        }
      })
      .catch(function (error) {
        alert("Could not create potfolio please check your inputs");
      })
      .finally((response) => {});
  };

  render() {
    return (
      <div className="add-portfolio-container">
        <form onSubmit={this.handleSubmit}>
          <div className="form-group">
            <label htmlFor="name-input">Name:</label>
            <input
              type="text"
              id="name-input"
              value={this.state.name}
              onChange={this.handleNameChange}
              required
            />
          </div>
          <div className="form-group">
            
          </div>
          <button type="submit" className="submit-button">
            Add Portfolio
          </button>
        </form>
      </div>
    );
  }
}

export default AddPortfolio;
