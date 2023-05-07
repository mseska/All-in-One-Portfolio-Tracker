import React, { useState } from "react";
import logo from "./navBarLogo.svg";
import "bootstrap/dist/css/bootstrap.css";
import { useNavigate } from "react-router-dom";
import "./navBar.css";
import UserIcon from "./userIcon";
// import "./userIcon.css";

export default function NavBar2() {
  const navigate = useNavigate();

  const [showUserPopUp, setShowUserPopUp] = useState(false);

  function handleMouseEnterUserIcon() {
    setShowUserPopUp(true);
  }

  function handleMouseLeave() {
    setShowUserPopUp(false);
  }

  function searchFunc() {
    alert("You searched for something");
  }

  function logoFunc() {
    // alert("hola");
    if (window.location.pathname == "/home") {
      navigate(0);
    }
    navigate("/home");
  }

  function newsFunc() {
    navigate("/news");
  }

  function myPortfolioButtonFunc() {
    navigate("/myPortfolio");
  }

  function homeButtonFunc() {
    navigate("/home");
  }

  function cryptoButtonFunc() {
    navigate("/crypto");
  }

  function forecastButtonFunc() {
    navigate("/forecast");
  }

 

  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css"
  ></link>;

  return (
    <div className="NavBar" onMouseLeave={handleMouseLeave}>
      <div className="Navbar1">
        <img
          class="NavBarLogo"
          src={logo}
          // style={{ height: 100, width: 100 }}
          alt="website logo"
          onClick={logoFunc}
        />
        <form className="searchField" onSubmit={searchFunc}>
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
            onMouseEnter={handleMouseEnterUserIcon}
            // onMouseLeave={handleMouseLeave}
          >
            <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" />
            <path
              fill-rule="evenodd"
              d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"
            />
          </svg>
          {showUserPopUp && (
            <UserIcon  >
              
            </UserIcon>
          )}
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="25"
            height="25"
            fill="currentColor"
            class="bi bi-envelope NavBarIcon"
            viewBox="0 0 16 16"
          >
            <path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2Zm13 2.383-4.708 2.825L15 11.105V5.383Zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741ZM1 11.105l4.708-2.897L1 5.383v5.722Z" />
          </svg>

          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-bell-fill NavBarIcon"
            viewBox="0 0 16 16"
          >
            <path d="M8 16a2 2 0 0 0 2-2H6a2 2 0 0 0 2 2zm.995-14.901a1 1 0 1 0-1.99 0A5.002 5.002 0 0 0 3 6c0 1.098-.5 6-2 7h14c-1.5-1-2-5.902-2-7 0-2.42-1.72-4.44-4.005-4.901z" />
          </svg>
        </div>
      </div>
      <div className="NavBar2">
        <button
          type="button"
          class="btn btn-primary navBarButtons"
          onClick={homeButtonFunc}
        >
          Home
        </button>
        <button
          type="button"
          class="btn btn-primary navBarButtons"
          onClick={newsFunc}
        >
          MyNews
        </button>
        <button
          type="button"
          class="btn btn-primary navBarButtons"
          onClick={myPortfolioButtonFunc}
        >
          MyPortfolio
        </button>
        <button
          type="button"
          class="btn btn-primary navBarButtons"
          onClick={cryptoButtonFunc}
        >
          Timeline
        </button>
        <button
          type="button"
          class="btn btn-primary navBarButtons"
          onClick={forecastButtonFunc}
        >
          Forecast
        </button>
      </div>
    </div>
  );
}
