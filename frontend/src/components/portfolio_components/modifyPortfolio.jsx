import React, { Component } from "react";
import "./modifyPortfolio.css";

class ModifyPortfolio extends Component {
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
    // call function to handle form submission here
  };

  render() {
    return (
      <div className="ModifyPortfolioContainer">
        <h1 className="PortfolioNameModifyPortfolio">
          {localStorage.getItem("selectedChartName")}
        </h1>
        <div className="ModifyPortfolio2">
          <div className="ModifyPortfolioLeft">
            <h1 style={{ fontSize: "3vh" }}>Add Symbol:</h1>
            <form className="searchFieldModifyPortfolio">
              <input
                class="form-control me-2 searchField searchFieldModifyPortfolio"
                type="search"
                placeholder="Search for symbols"
                aria-label="Search"
              ></input>
            </form>
            <div className="AmountModifyPortfolio">
              {/* <h>Amount: </h> */}
              <input
                className="AmountField"
                type="text"
                placeholder="Amount:"
              />
            </div>
            <button className="AddSymbolButton">Add</button>
          </div>
          <div className="ModifyPortfolioRight">
            <h1 style={{ fontSize: "3vh" }}>Remove Symbol:</h1>
            <select className="SelectSymbolModify" name="" id="">
              <option>Hello</option>
            </select>
            <button className="RemoveSymbol">Remove</button>
          </div>
        </div>

        {/* <form onSubmit={this.handleSubmit}>
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
        </form> */}
      </div>
    );
  }
}

export default ModifyPortfolio;
