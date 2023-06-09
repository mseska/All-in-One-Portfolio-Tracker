// import * as React from "react";
import { React, useState, useEffect } from "react";
// import { Link } from "react-router-dom";
import axios from "axios";

import "./home.css";
import NavBar from "../components/NavBar/navBar2";
// import News from "../components/news_components/news";
import HomePageNewsHolder from "../components/news_components/newsHolder_home";

function Home() {
  const [stockData, setStockData] = useState([]);
  const [cryptoData, setCryptoData] = useState([]);
  const [myAssetsData, setmyAssetsData] = useState([]);
  const [commodityData, setCommodityData] = useState([]);

  function getClassNameForPrice(change) {
    if (change > 0) {
      return "green";
    } else if (change < 0) {
      return "red";
    } else {
      return "";
    }
  }

  useEffect(() => {
    const token = localStorage.getItem("userToken");
    axios
      .get("http://localhost:8000/api/myasset-price", {
        headers: {
          Authorization: `${token}`,
        },
      })
      .then((response) => {
        console.log("response get as", response.data);
        setmyAssetsData(response.data);
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
      .get("http://localhost:8000/api/stock-price")
      .then((response) => {
        setStockData(response.data);
        // console.log("response get as", response.data);
        // console.log("currencyData", currencyData);
      })
      .catch((error) => {
        console.log(error);
      });
    axios
      .get("http://localhost:8000/api/commodity-price")
      .then((response) => {
        console.log("response get as", response.data);
        setCommodityData(response.data);
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
        <div className="NewsDiv">
          <HomePageNewsHolder></HomePageNewsHolder>
        </div>
        <div className="HomePageTables scrollable-area">
          <section>
            <p className="HomePageTableNames"> My Assets</p>
            <table class="table table-hover table-bordered">
              <thead>
                <tr>
                  <th scope="col">Symbol</th>
                  <th scope="col">Price</th>
                  <th scope="col">Change</th>
                </tr>
              </thead>
              <tbody>
                {myAssetsData.map((stock, index) => (
                  <tr key={index}>
                    <td>
                      <a
                        className="HomePageStockNames"
                        href=""
                        onClick={() =>
                          window.open(
                            `https://www.google.com/search?q=${stock.symbol}+stock`,
                            "_blank"
                          )
                        }
                      >
                        {stock.symbol}
                      </a>
                    </td>
                    <td>{stock.price}</td>
                    <td className={getClassNameForPrice(stock.change)}>
                      {" "}
                      % {stock.change}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </section>
          <section>
            <p className="HomePageTableNames">Crypto</p>
            <table class="table table-hover table-bordered">
              <thead>
                <tr>
                  <th scope="col">Symbol</th>
                  <th scope="col">Price</th>
                  <th scope="col">Change</th>
                </tr>
              </thead>
              <tbody>
                {cryptoData.map((crypto, index) => (
                  <tr key={index}>
                    <td>
                      <a
                        className="HomePageStockNames"
                        href=""
                        onClick={() =>
                          window.open(
                            `https://www.google.com/search?q=${crypto.symbol}`,
                            "_blank"
                          )
                        }
                      >
                        {crypto.symbol}
                      </a>
                    </td>
                    <td>{crypto.price}</td>
                    <td className={getClassNameForPrice(crypto.change)}>
                      {" "}
                      % {crypto.change}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </section>
          <section>
            <p className="HomePageTableNames">Stock</p>
            <table class="table table-hover table-bordered">
              <thead>
                <tr>
                  <th scope="col">Symbol</th>
                  <th scope="col">Price</th>
                  <th scope="col">Change</th>
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
                            `https://www.google.com/search?q=${stock.symbol}`,
                            "_blank"
                          )
                        }
                      >
                        {stock.symbol}
                      </a>
                    </td>
                    <td>{stock.price}</td>
                    <td className={getClassNameForPrice(stock.change)}>
                      {" "}
                      % {stock.change}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </section>
          <section>
            <p className="HomePageTableNames">Commodity</p>
            <table class="table table-hover table-bordered">
              <thead>
                <tr>
                  <th scope="col">Symbol</th>
                  <th scope="col">Price</th>
                  <th scope="col">Change</th>
                </tr>
              </thead>
              <tbody>
                {commodityData.map((commodity, index) => (
                  <tr key={index}>
                    <td>
                      <a
                        className="HomePageStockNames"
                        href=""
                        onClick={() =>
                          window.open(
                            `https://www.google.com/search?q=${commodity.symbol} +price`,
                            "_blank"
                          )
                        }
                      >
                        {commodity.symbol}
                      </a>
                    </td>
                    <td>{commodity.price}</td>
                    <td className={getClassNameForPrice(commodity.change)}>
                      {" "}
                      % {commodity.change}
                    </td>
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
