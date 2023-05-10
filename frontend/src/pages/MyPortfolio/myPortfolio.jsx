import { React, useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.css";
import { useNavigate } from "react-router-dom";
import NavBar from "../../components/NavBar/navBar2.jsx";
import "./myPortfolio.css";
import PiechartHolder from "../../components/portfolio_components/piechartHolder.jsx";
import axios from "axios";
import AddPortfolio from "../../components/portfolio_components/addPortfolio";
import ModifyPortfolio from "../../components/portfolio_components/modifyPortfolio";
import styled from "styled-components";

export default function MyPortfolio() {
  const [selectedPortfolio, setselectedPortfolio] = useState([]);
  const [portfolioData, setportfolioData] = useState([]);
  // let portfolioData = [];

  const [showAddPortfolio, setshowAddPortfolio] = useState(false);
  const [showModifyPortfolio, setshowModifyPortfolio] = useState(false);

  function handleClick() {
    setselectedPortfolio(localStorage.getItem("selectedPortfolio"));
  }

  function handleClickAddPortfolio() {
    setshowAddPortfolio(true);
    // window.body.classList.add("darken");
  }

  function handleClickModifyPortfolio() {
    setshowModifyPortfolio(true);
  }

  function removeAddPortfolio() {
    setshowAddPortfolio(false);
    removeModifyPortfolio();
  }

  function removeModifyPortfolio() {
    setshowModifyPortfolio(false);
  }

  function getPortfolioData() {
    const token = localStorage.getItem("userToken");
    const selectedPortfolio = localStorage.getItem("selectedPortfolio");
    axios
      .get("http://localhost:8000/api/portfolio-data/", {
        headers: {
          Authorization: `${token}`,
          portfolio: `${selectedPortfolio}`,
        },
      })
      .then((response) => {
        setportfolioData(response.data.data);
        // console.log(response.data)
        localStorage.setItem("portfolioData", response.data.data);
        // console.log();
      })
      .catch((error) => {
        console.log(error);
      });
  }

  useEffect(() => {
    setselectedPortfolio(1);
    // localStorage.setItem("selectedPortfolio", 1);
    const token = localStorage.getItem("userToken");
    const selectedPortfolio = localStorage.getItem("selectedPortfolio");
    // portfolioData = localStorage.getItem("portfolioData");
    // axios
    //   .get("http://localhost:8000/api/portfolio-data/", {
    //     headers: {
    //       Authorization: `${token}`,
    //       portfolio: `${selectedPortfolio}`,
    //     },
    //   })
    //   .then((response) => {
    //     setportfolioData(response.data.data);
    //     // console.log(response.data)
    //     localStorage.setItem("portfolioData", response.data.data);
    //     // console.log();
    //   })
    //   .catch((error) => {
    //     console.log(error);
    //   });
    // setportfolioData(localStorage.getItem("portfolioData"));
  }, []);

  return (
    <div>
      <NavBar></NavBar>
      <div className="MainPortfolioDiv" onClick={handleClick}>
        <div className="First" onClick={getPortfolioData}>
          <div className="AddModifyButtonDiv">
            {showAddPortfolio && <AddPortfolio></AddPortfolio>}
            {showModifyPortfolio && <ModifyPortfolio></ModifyPortfolio>}
            <div className="MyPortfoliosText">My Portfolios</div>
            <div className="MyPortfolioIconsDiv">
              <svg
                onClick={handleClickAddPortfolio}
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-plus-square-fill MyPortfolioIcons"
                viewBox="0 0 16 16"
              >
                <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3a.5.5 0 0 1 1 0z" />
              </svg>

              <svg
                onClick={handleClickModifyPortfolio}
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-pencil-square MyPortfolioIcons"
                viewBox="0 0 16 16"
              >
                <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z" />
                <path
                  fill-rule="evenodd"
                  d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"
                />
              </svg>
            </div>
          </div>
          <div
            className="Second scrollable-areaPie"
            onClick={removeAddPortfolio}
          >
            <PiechartHolder></PiechartHolder>
          </div>
        </div>
        <div className="OtherPortfolioDataDiv"></div>
        <div className="TableDiv">
          <table class="table table-hover table-bordered">
            <thead>
              <tr>
                <th scope="col">Symbol</th>
                <th scope="col">Value</th>
              </tr>
            </thead>
            <tbody>
              {/* {selectedPortfolio} */}
              {portfolioData.map((stock, index) => (
                <tr>
                  <td>{stock.name}</td>
                  <td>{stock.value}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
