// import * as React from "react";
import { React, useState, useEffect } from "react";
import axios from "axios";

import "./home.css";
import NavBar from "../components/NavBar/navBar";

function Home() {
  const [stockData, setStockData] = useState([]);
  //"http://localhost:8000/api"
  useEffect(() => {
    axios
      .get("http://localhost:8000/api/stock-price")
      .then((response) => {
        console.log("response get as", response.data);
        setStockData(response.data);
        console.log("stockData", stockData)
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <NavBar></NavBar>
      <div className="BelowNavBar">
        <div className="NewsDiv">{/* <button>hello</button> */}</div>
        <div className="HomePageTables">
          <section>
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">Symbol</th>
                  <th scope="col">Price</th>
                  <th scope="col">Currency</th>
                </tr>
              </thead>
              <tbody>
                {stockData.map((stock, index) => (
                  <tr key={index}>
                    <td>{stock.symbol}</td>
                    <td>{stock.price}</td>
                    <td>{stock.currency}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </section>
        </div>
      </div>
    </div>
  );
}

export default Home;
