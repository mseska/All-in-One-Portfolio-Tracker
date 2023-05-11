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
    selectedSymbol2: "",
    portfolioSymbols: [],
  };

  handleNameChange = (event) => {
    this.setState({ name: event.target.value });
  };

  handleAmount1Change = (event) => {
    this.setState({ amount1: event.target.value });
  };
  handleAmount2Change = (event) => {
    this.setState({ amount2: event.target.value });
  };

  handleSymbol2Change = (event) => {
    this.setState({ selectedSymbol2: event.target.value });
  };

  handlePlusClick = (event) => {
    event.preventDefault();
    const selectedSymbolToAdjust = this.state.selectedSymbol2;
    const amountToAdjust = this.state.amount2;
    const token = localStorage.getItem("userToken");
    const portfolioId = localStorage.getItem("selectedPortfolio");

    axios
      .post("http://localhost:8000/api/increase-in-portfolio", {
        Token: token,
        PortfolioId: portfolioId,
        amount: amountToAdjust,
        Symbol: selectedSymbolToAdjust,
      })
      .then(function (response) {
        if (response.status === 201) {
          alert(selectedSymbolToAdjust + "added" + amountToAdjust);
        }
      })
      .catch(function (error) {
        alert(selectedSymbolToAdjust + "added" + amountToAdjust);
        // alert("Could not create potfolio please check your inputs");
      })
      .finally((response) => {});
  };

  handleMinusClick = (event) => {
    event.preventDefault();
    const selectedSymbolToAdjust = this.state.selectedSymbol2;
    const amountToAdjust = this.state.amount2;
    const token = localStorage.getItem("userToken");
    const portfolioId = localStorage.getItem("selectedPortfolio");

    axios
      .post("http://localhost:8000/api/decrease-in-portfolio", {
        Token: token,
        PortfolioId: portfolioId,
        amount: amountToAdjust,
        Symbol: selectedSymbolToAdjust,
      })
      .then(function (response) {
        if (response.status === 201) {
          alert(selectedSymbolToAdjust + "decreased" + amountToAdjust);
        }
      })
      .catch(function (error) {
        alert(selectedSymbolToAdjust + "decreased" + amountToAdjust);
        // alert("Could not create potfolio please check your inputs");
      })
      .finally((response) => {});
  };

  handleSubmit = (event) => {
    event.preventDefault();
    const token = localStorage.getItem("userToken");
    const portfolioId = localStorage.getItem("selectedPortfolio");
    const symb = this.state.selectedSymbol;
    localStorage.setItem("selectedSymbol", symb);
    axios
      .post("http://localhost:8000/api/add-to-portfolio", {
        Token: token,
        PortfolioId: portfolioId,
        symbol: this.state.selectedSymbol,
        amount: this.state.amount1,
      })
      .then(function (response) {
        if (response.status === 201) {
          alert(symb + " added to portfolio");
          window.location.reload(true);
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
                      border: "1px",
                      marginRight: "1px",
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
            <select
              className="SelectSymbolModify"
              name=""
              id=""
              onChange={this.handleSymbol2Change}
            >
              {this.state.portfolioSymbols.map((item) => (
                <option key={item.name} value={item.name}>
                  {item.name}
                </option>
              ))}
            </select>
            <div className="AmountModifyPortfolio">
              {/* <h>Amount: </h> */}
              <input
                className="AmountField"
                type="text"
                placeholder="Amount:"
                onChange={this.handleAmount2Change}
              />
            </div>
            <button
              onClick={this.handlePlusClick}
              className="ChangeSymbolButton"
            >
              +
            </button>
            <h1 style={{ fontSize: "2vh" }}>or</h1>
            <button className="RemoveSymbol" onClick={this.handleMinusClick}>
              -
            </button>
          </div>
        </div>
      </div>
    );
  }
  componentWillMount() {
    const selectedPortfolio = localStorage.getItem("selectedPortfolio");
    const token = localStorage.getItem("userToken");
    console.log("hello");
    console.log(selectedPortfolio);
    axios
      .get("http://localhost:8000/api/all-symbols", {})
      .then((response) => {
        localStorage.setItem("allSymbols", response.data.data);
        this.setState({ searchResults: response.data.data });
        console.log(response.data.data);
        // this.searchResults = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
    axios
      .get("http://localhost:8000/api/symbols-of-portfolio", {
        headers: {
          Authorization: `${token}`,
          Portfolio: `${selectedPortfolio}`,
        },
      })
      .then((response) => {
        if (response.status === 201) {
          this.setState({ portfolioSymbols: response.data });
          localStorage.setItem("portfolioSymbols", response.data);
        }
      })
      .catch((error) => {
        console.log(error);
      });
  }
}

export default ModifyPortfolio;
