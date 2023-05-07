import React, { Component } from "react";
import "./modifyPortfolio.css";
import axios from "axios";

class ModifyPortfolio extends Component {
  state = {
    searchTerm: "",
    amount1: "",
    amount2: "",
    searchResults: [],
    selectedSymbol: "",
  };

  handleNameChange = (event) => {
    this.setState({ name: event.target.value });
  };

  handleAmount1Change = (event) => {
    this.setState({ amount1: event.target.value });
  };

  handleSubmit = (event) => {
    event.preventDefault();
    axios
      .post("http://localhost:8000/api/add-to-portfolio", {
        symbol: this.state.selectedSymbol,
        amount: this.state.amount1,
      })
      .then(function (response) {
        if (response.status === 201) {
          alert(localStorage.getItem("selectedSymbol") + "added to portfolio");
        }
      })
      .catch(function (error) {
        alert("Could not create potfolio please check your inputs");
      })
      .finally((response) => {});

    // call function to handle form submission here
  };

  render() {
    const possibleItems = [
      { name: "TSLA" },
      { name: "MSLA" },
      { name: "TSLB" },
      { name: "TSGA" },
    ];
    let filteredItems = possibleItems;
    if (this.state.searchTerm) {
      filteredItems = possibleItems.filter((item) =>
        item.name.toLowerCase().startsWith(this.state.searchTerm.toLowerCase())
      );
    }
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
                onChange={(event) =>
                  this.setState({ searchTerm: event.target.value })
                }
              ></input>
              {this.state.searchTerm &&
                filteredItems.map((item) => (
                  <button
                    style={{
                      borderRadius: "10px",
                      color: "white",
                      backgroundColor: "#7498da",
                    }}
                    onClick={(event) => {
                      event.preventDefault();
                      this.setState({ selectedSymbol: item.name });
                      // localStorage.setItem("selectedSymbol",item.name);
                      this.setState({ searchTerm: item.name });
                    }}
                  >
                    {item.name}
                  </button>
                ))}
            </form>
            <div className="AmountModifyPortfolio">
              {/* <h>Amount: </h> */}
              <input
                className="AmountField"
                type="text"
                placeholder="Amount:"
                onChange={this.handleAmount1Change}
              />
            </div>
            <button onClick={this.handleSubmit} className="AddSymbolButton">
              Add
            </button>
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
            <h1 style={{ fontSize: "2vh" }}>or</h1>
            <button className="RemoveSymbol">-</button>
          </div>
        </div>
      </div>
    );
  }
  componentWillMount() {
    axios
      .get("http://localhost:8000/api/all-symbols", {})
      .then((response) => {
        localStorage.setItem("allSymbols", response.data);
        this.searchResults = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  }
}

export default ModifyPortfolio;
