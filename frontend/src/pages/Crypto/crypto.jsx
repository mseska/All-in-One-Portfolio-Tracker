import { React, useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.css";
import { useNavigate } from "react-router-dom";
import NavBar from "../../components/NavBar/navBar2.jsx";
import "./crypto.css"; // CSS file for styling
import axios from "axios";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";

function PortfolioTimeline() {
  const navigate = useNavigate();
  const [portfolioNames, setPortfolioNames] = useState([]);
  const [weeklyData, setWeeklyData] = useState([]);
  const [monthlyData, setMonthlyData] = useState([]);
  const [yearlyData, setYearlyData] = useState([]);

  const [assetNames, setAssetNames] = useState([]);
  const [weeklyAssetData, setWeeklyAssetData] = useState([]);
  const [monthlyAssetData, setMonthlAssetData] = useState([]);
  const [yearlyAssetData, setYearlyAssetData] = useState([]);

  const [selectedPortfolio, setSelectedPortfolio] = useState([]);

  function selectChange2(event) {
    const token = localStorage.getItem("userToken");
    const assetName = event.target.value;

    axios
      .get("http://localhost:8000/api/get-weekly-data-asset", {
        headers: {
          Authorization: `${token}`,
          assetName: `${assetName}`,
        },
      })
      .then((response) => {
        setWeeklyAssetData(response.data.data);
      })
      .catch((error) => {
        console.log(error);
      });

    // axios
    //   .get("http://localhost:8000/api/get-monthly-data-asset", {
    //     headers: {
    //       Authorization: `${token}`,
    //       assetName: `${assetName}`,
    //     },
    //   })
    //   .then((response) => {
    //     setMonthlAssetData(response.data);
    //   })
    //   .catch((error) => {
    //     console.log(error);
    //   });

    // axios
    //   .get("http://localhost:8000/api/get-yearly-data-asset", {
    //     headers: {
    //       Authorization: `${token}`,
    //       assetName: `${assetName}`,
    //     },
    //   })
    //   .then((response) => {
    //     setYearlyAssetData(response.data);
    //   })
    //   .catch((error) => {
    //     console.log(error);
    //   });
  }

  function selectChange1(event) {
    const portfolioName = event.target.value;
    const token = localStorage.getItem("userToken");

    axios
      .get("http://localhost:8000/api/get-weekly-data-portfolio", {
        headers: {
          Authorization: `${token}`,
          Portfolio: `${portfolioName}`,
        },
      })
      .then((response) => {
        console.log(response.data, "response.data totaaaaallllll");
        setWeeklyData(response.data.data);
      })
      .catch((error) => {
        console.log(error);
      });
    // axios
    //   .get("http://localhost:8000/api/get-monthly-data-portfolio", {
    //     headers: {
    //       Authorization: `${token}`,
    //       PortfolioName: `${portfolioName}`,
    //     },
    //   })
    //   .then((response) => {
    //     // setMonthlyData(response.data);
    //   })
    //   .catch((error) => {
    //     console.log(error);
    //   });
    // axios
    //   .get("http://localhost:8000/api/get-yearly-data-portfolio", {
    //     headers: {
    //       Authorization: `${token}`,
    //       PortfolioName: `${portfolioName}`,
    //     },
    //   })
    //   .then((response) => {
    //     // setYearlyData(response.data);
    //   })
    //   .catch((error) => {
    //     console.log(error);
    //   });
  }

  useEffect(() => {
    const token = localStorage.getItem("userToken");
    let portNames = [];
    let assNames = [];

    axios
      .get("http://localhost:8000/api/get-portfolio-names", {
        headers: {
          Authorization: `${token}`,
        },
      })
      .then((response) => {
        portNames = response.data.names;
        setPortfolioNames(response.data.names);
        return axios.get("http://localhost:8000/api/get-asset-names", {
          headers: {
            Authorization: `${token}`,
          },
        });
      })
      .then((response) => {
        assNames = response.data.names;
        setAssetNames(response.data.names);
        return axios.get(
          "http://localhost:8000/api/get-weekly-data-portfolio",
          {
            headers: {
              Authorization: `${token}`,
              Portfolio: `${portNames[0]}`,
            },
          }
        );
      })
      .then((response) => {
        setWeeklyData(response.data.data);
        setSelectedPortfolio(portNames[0]);
      })
      .catch((error) => {
        console.log(error);
      });

    // axios
    //   .get("http://localhost:8000/api/get-monthly-data-portfolio", {
    //     headers: {
    //       Authorization: `${token}`,
    //       PorfolioName: `${portNames[0]}`,
    //     },
    //   })
    //   .then((response) => {
    //     setMonthlyData(response.data);
    //   })
    //   .catch((error) => {
    //     console.log(error);
    //   });

    // axios
    //   .get("http://localhost:8000/api/get-yearly-data-portfolio", {
    //     headers: {
    //       Authorization: `${token}`,
    //       PorfolioName: `${portNames[0]}`,
    //     },
    //   })
    //   .then((response) => {
    //     setYearlyData(response.data);
    //   })
    //   .catch((error) => {
    //     console.log(error);
    //   });

    axios
      .get("http://localhost:8000/api/get-weekly-data-asset", {
        headers: {
          Authorization: `${token}`,
          AssetName: `${assNames[0]}`,
        },
      })
      .then((response) => {
        setWeeklyAssetData(response.data.data);
      })
      .catch((error) => {
        console.log(error);
      });

    // axios
    //   .get("http://localhost:8000/api/get-monthly-data-asset", {
    //     headers: {
    //       Authorization: `${token}`,
    //       AssetName: `${assNames[0]}`,
    //     },
    //   })
    //   .then((response) => {
    //     setMonthlAssetData(response.data.data);
    //   })
    //   .catch((error) => {
    //     console.log(error);
    //   });

    // axios
    //   .get("http://localhost:8000/api/get-yearly-data-asset", {
    //     headers: {
    //       Authorization: `${token}`,
    //       AssetName: `${assNames[0]}`,
    //     },
    //   })
    //   .then((response) => {
    //     setYearlyAssetData(response.data.data);
    //   })
    //   .catch((error) => {
    //     console.log(error);
    //   });
  }, []);

  return (
    <div className="timeline-page">
      <NavBar></NavBar>
      <div className="timeline-container">
        <div className="left-column">
          <p style={{ color: "purple", fontWeight: "bolder", fontSize: "3vh" }}>
            Portfolios Timeline
          </p>
          <select
            className="timeline-select"
            name=""
            id=""
            onChange={selectChange1}
          >
            {portfolioNames.map((item) => (
              <option key={item} value={item}>
                {item}
              </option>
            ))}
          </select>
          <p
            style={{
              color: "purple",
              fontWeight: "bolder",
              alignItems: "center",
            }}
          >
            Weekly:
          </p>

          <div className="line-chart">
            <LineChart width={400} height={300} data={weeklyData}>
              <XAxis dataKey="name" />
              <YAxis />
              <CartesianGrid stroke="#eee" />
              <Line type="monotone" dataKey="value" stroke="#8884d8" />
              <Tooltip />
              <Legend />
            </LineChart>
          </div>
          <p style={{ color: "purple", fontWeight: "bolder" }}>Monthly:</p>

          <div className="line-chart">
            <LineChart width={400} height={300} data={monthlyData}>
              <XAxis dataKey="name" />
              <YAxis />
              <CartesianGrid stroke="#eee" />
              <Line type="monotone" dataKey="value" stroke="#8884d8" />
              <Tooltip />
              <Legend />
            </LineChart>
          </div>
          <p style={{ color: "purple", fontWeight: "bolder" }}>Yearly:</p>

          <div className="line-chart">
            <LineChart width={400} height={300} data={yearlyData}>
              <XAxis dataKey="name" />
              <YAxis />
              <CartesianGrid stroke="#eee" />
              <Line type="monotone" dataKey="value" stroke="#8884d8" />
              <Tooltip />
              <Legend />
            </LineChart>
          </div>
        </div>
        <hr className="vertical-line"></hr>
        <div className="right-column">
          <p style={{ color: "purple", fontWeight: "bolder", fontSize: "3vh" }}>
            Assets Timeline
          </p>
          <select
            className="timeline-select"
            name=""
            id=""
            onChange={selectChange2}
          >
            {assetNames.map((item) => (
              <option key={item} value={item}>
                {item}
              </option>
            ))}
          </select>
          <p style={{ color: "purple", fontWeight: "bolder" }}>Weekly:</p>

          <div className="line-chart">
            <LineChart width={400} height={300} data={weeklyAssetData}>
              <XAxis dataKey="name" />
              <YAxis />
              <CartesianGrid stroke="#eee" />
              <Line type="monotone" dataKey="value" stroke="#8884d8" />
              <Tooltip />
              <Legend />
            </LineChart>
          </div>
          <p style={{ color: "purple", fontWeight: "bolder" }}>Monthly:</p>

          <div className="line-chart">
            <LineChart width={400} height={300} data={monthlyAssetData}>
              <XAxis dataKey="name" />
              <YAxis />
              <CartesianGrid stroke="#eee" />
              <Line type="monotone" dataKey="value" stroke="#8884d8" />
              <Tooltip />
              <Legend />
            </LineChart>
          </div>
          <p style={{ color: "purple", fontWeight: "bolder" }}>Yearly:</p>

          <div className="line-chart">
            <LineChart width={400} height={300} data={yearlyAssetData}>
              <XAxis dataKey="name" />
              <YAxis />
              <CartesianGrid stroke="#eee" />
              <Line type="monotone" dataKey="value" stroke="#8884d8" />
              <Tooltip />
              <Legend />
            </LineChart>
          </div>
        </div>
      </div>
    </div>
  );
}

export default PortfolioTimeline;
