// import * as React from "react";
import { React, useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

import "./home.css";
import NavBar from "../components/NavBar/navBar2";

function Home() {
  const [stockData, setStockData] = useState([]);
  const [cryptoData, setCryptoData] = useState([]);
  const [currencyData, setCurrencyData] = useState([]);
  const [commodityData, setCommodityData] = useState([]);

  //"http://localhost:8000/api"
  useEffect(() => {
    axios
      .get("http://localhost:8000/api/stock-price")
      .then((response) => {
        console.log("response get as", response.data);
        setStockData(response.data);
        console.log("stockData", stockData);
      })
      .catch((error) => {
        console.log(error);
      });
    axios
      .get("http://localhost:8000/api/crypto-price")
      .then((response) => {
        console.log("response get as", response.data);
        setCryptoData(response.data);
        console.log("cryptoData", cryptoData);
      })
      .catch((error) => {
        console.log(error);
      });
    axios
      .get("http://localhost:8000/api/currency-price")
      .then((response) => {
        console.log("response get as", response.data);
        setCryptoData(response.data);    //HATA VAR SANIRIM, COPY PASTE SETCRYPTODATA DİYOR BU SATIRDA SETCURRENCYDATA DİYE DEĞİŞTİR
        console.log("currencyData", currencyData);
      })
      .catch((error) => {
        console.log(error);
      });
    axios
      .get("http://localhost:8000/api/commodity-price")
      .then((response) => {
        console.log("response get as", response.data);
        setCryptoData(response.data);  //HATA VAR SANIRIM, COPY PASTE SETCRYPTODATA DİYOR BU SATIRDA SETCOMMODITYDATA DİYE DEĞİŞTİR
        console.log("commodityData", commodityData);
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
        <div className="HomePageTables scrollable-area">
          <section>
            <p className="HomePageTableNames"> Top Rated Stocks:</p>
            <table class="table table-hover table-bordered">
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
                    <td>
                      <a
                      className="HomePageStockNames"
                        href=""
                        onClick={() =>
                          window.open(
                            `https://www.google.com/search?q=${stock.symbol}+stock`,
                            "_blank",
                            
                          )
                        }
                      >
                        {stock.symbol}
                      </a>
                    </td>
                    <td>{stock.price}</td>
                    <td>{stock.currency}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </section>
          <section>
            <p className="HomePageTableNames">Crypto:</p>
            <table class="table table-hover table-bordered">
              <thead>
                <tr>
                  <th scope="col">Symbol</th>
                  <th scope="col">Price</th>
                  <th scope="col">Currency</th>
                </tr>
              </thead>
              <tbody>
                {cryptoData.map((stock, index) => (
                  <tr key={index}>
                    <td>{stock.symbol}</td>
                    <td>{stock.price}</td>
                    <td>{stock.currency}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </section>
          <section>
            <p className="HomePageTableNames">Currency:</p>
            <table class="table table-hover table-bordered">
              <thead>
                <tr>
                  <th scope="col">Symbol</th>
                  <th scope="col">Price</th>
                  <th scope="col">Currency</th>
                </tr>
              </thead>
              <tbody>
                {currencyData.map((stock, index) => (
                  <tr key={index}>
                    <td>{stock.symbol}</td>
                    <td>{stock.price}</td>
                    <td>{stock.currency}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </section>
          <section>
            <p className="HomePageTableNames">Commodities:</p>
            <table class="table table-hover table-bordered">
              <thead>
                <tr>
                  <th scope="col">Symbol</th>
                  <th scope="col">Price</th>
                  <th scope="col">Currency</th>
                </tr>
              </thead>
              <tbody>
                {commodityData.map((stock, index) => (
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
