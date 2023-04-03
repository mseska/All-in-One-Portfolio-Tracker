import React from "react";
import { Component } from "react";
import logo from "./navBarLogo.svg";
import "bootstrap/dist/css/bootstrap.css";
import "./navBar.css";

class NavBar extends Component {
  state = {};

  searchFunc() {
    alert("You searched for something");
  }

  logoFunc() {
    alert("hola");
  }

  render() {
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css"
    ></link>;

    return (
      <div className="NavBar">
        <div className="Navbar1">
          <img
            class="NavBarLogo"
            src={logo}
            style={{ height: 100, width: 100 }}
            alt="website logo"
            onClick={this.logoFunc}
          />
          <form className="searchField" onSubmit={this.searchFunc}>
            <input
              class="form-control me-2 searchField"
              type="search"
              placeholder="Search for stocks, symbols or news"
              aria-label="Search"
            ></input>
          </form>
          <button class="btn btn-outline-success searchButton" type="submit">
            Search
          </button>

          <div className="NavBar1_Icons ">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="25"
              height="25"
              fill="currentColor"
              class="bi bi-person-circle NavBarIcon"
              viewBox="0 0 16 16"
            >
              <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" />
              <path
                fill-rule="evenodd"
                d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"
              />
            </svg>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="25"
              height="25"
              fill="currentColor"
              class="bi bi-person-circle NavBarIcon"
              viewBox="0 0 16 16"
            >
              <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" />
              <path
                fill-rule="evenodd"
                d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"
              />
            </svg>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="25"
              height="25"
              fill="currentColor"
              class="bi bi-person-circle NavBarIcon"
              viewBox="0 0 16 16"
            >
              <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" />
              <path
                fill-rule="evenodd"
                d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"
              />
            </svg>
          </div>
        </div>
        <div className="NavBar2">
          <button type="button" class="btn btn-primary navBarButtons">
            Home
          </button>
          <button type="button" class="btn btn-primary navBarButtons">
            News
          </button>
          <button type="button" class="btn btn-primary navBarButtons">
            MyPortfolio
          </button>
          <button type="button" class="btn btn-primary navBarButtons">
            Crypto
          </button>
          <button type="button" class="btn btn-primary navBarButtons">
            Forecast
          </button>
        </div>
      </div>
    );
  }
}

export default NavBar;
