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
            <h1 style={{ fontSize: "3vh" }}>Add New Symbol:</h1>
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
          <div className="separator"></div>
          <div className="ModifyPortfolioRight">
            <h1 style={{ fontSize: "3vh" }}>+/- Symbol:</h1>
            <select className="SelectSymbolModify" name="" id="">
              <option>Hello</option>
            </select>
            <div className="AmountModifyPortfolio">
              {/* <h>Amount: </h> */}
              <input
                className="AmountField"
                type="text"
                placeholder="Amount:"
              />
            </div>
            <button className="ChangeSymbolButton">+</button>
            <h1 style={{fontSize: "2vh"}}>or</h1>
            <button className="RemoveSymbol">-</button>

          </div>
        </div>
      </div>
    );
  }
}

export default ModifyPortfolio;
