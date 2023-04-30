import { React, useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.css";
import { useNavigate } from "react-router-dom";
import NavBar from "../../components/NavBar/navBar2.jsx";
import "./myPortfolio.css";
import PiechartHolder from "../../components/portfolio_components/piechartHolder.jsx";
import axios from "axios";


export default function MyPortfolio() {
  const [selectedPortfolio, setselectedPortfolio] = useState([]);
  const [portfolioData, setportfolioData] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem("userToken");
    const selectedPortfolio = localStorage.getItem("selectedPortfolio");
    axios
      .get("http://localhost:8000/api/crypto-price", {
        headers: {
          Authorization: `${token}`,
          // portfolio: `${selectedPortfolio}`,
        },
      })
      .then((response) => {
        setportfolioData(response.data);
        
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <NavBar></NavBar>
      <div className="MainPortfolioDiv">
        <div className="First">
          <div className="AddModifyButtonDiv">
            <div className="MyPortfoliosText">My Portfolios</div>
            <div className="MyPortfolioIconsDiv">
              <svg
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
          <div className="Second scrollable-areaPie">
            <PiechartHolder></PiechartHolder>
          </div>
        </div>
        <div className="OtherPortfolioDataDiv"></div>
        <div className="TableDiv">
        <table class="table table-hover table-bordered">
              <thead>
                <tr>
                  <th scope="col">Symbol</th>
                  <th scope="col">Price</th>
                  <th scope="col">Currency</th>
                </tr>
              </thead>
              <tbody>
                {portfolioData.map((stock, index) => (
                  <tr key={index}>
                    <td>{stock.symbol}</td>
                    <td>{stock.price}</td>
                    <td>{stock.currency}</td>
                  </tr>
                ))}
              </tbody>
            </table>
        </div>
      </div>
    </div>
  );
}
