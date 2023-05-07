import React, { Component } from "react";
import "./addPortfolio.css"
import axios from "axios";

class AddPortfolio extends Component {
  state = {
    name: "",
    currency: "",
  };

  handleNameChange = (event) => {
    this.setState({ name: event.target.value });
  };

  handleCurrencyChange = (event) => {
    this.setState({ currency: event.target.value });
  };

  handleSubmit = (event) => {
    event.preventDefault();
    axios
      .post("http://localhost:8000/api/create-portfolio", {
        name: this.state.name,
        currency: this.state.currency
       
      })
      .then(function (response) {
        if(response.status === 201) {

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
            <label htmlFor="currency-input">Currency:</label>
            <input
              type="text"
              id="currency-input"
              value={this.state.currency}
              onChange={this.handleCurrencyChange}
              required
            />
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
