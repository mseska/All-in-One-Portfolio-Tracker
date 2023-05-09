import React, { Component } from "react";
import axios from "axios";
import Piechart from "./piechart";

class PiechartHolder extends Component {
  state = {
    piecharts: [],
    selectedChart: null,
    count: 0,
  };

  handlePiechartClick = (chartId, chartName) => {
    const token = localStorage.getItem("userToken");
    const selectedPortfolio = localStorage.getItem("selectedPortfolio");
    const piecharts = this.state.piecharts;
    const newPiecharts = piecharts.map((piechart) => {
      if (piechart.props.chartID === chartId) {
        return React.cloneElement(piechart, { isSelected: true });
      } else {
        return React.cloneElement(piechart, { isSelected: false });
      }
    });
    // this.state.piecharts = newPiecharts;
    this.state.selectedChart = chartId;
    this.setState({ piecharts: newPiecharts });
    console.log(this.state.selectedChart);
    localStorage.setItem("selectedPortfolio", this.state.selectedChart);
    localStorage.setItem("selectedChartName", chartName);

    axios
      .get("http://localhost:8000/api/portfolio-data", {
        headers: {
          Authorization: `${token}`,
          portfolio: `${selectedPortfolio}`,
        },
      })
      .then((response) => {
        localStorage.setItem("portfolioData", response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  render() {
    return (
      <div style={{ display: "flex" }}>
        <div style={{ display: "flex" }} className="">
          {this.state.piecharts}
        </div>
      </div>
    );
  }
  componentWillMount() {
    axios
      .get("http://localhost:8000/api/get_portfolios/", {
        params: { token: localStorage.getItem("userToken") },
      })
      .then((res) => {
        let piechartList2 = res.data;
        let length = res.data.length;
        localStorage.setItem("piecharts", JSON.stringify(piechartList2));
        let piechartList = JSON.parse(localStorage.getItem("piecharts"));
        let finalList = [];
        for (var i = 0; i < length; i++) {
          console.log(piechartList[i].id);
          let id = piechartList[i].id;
          finalList.push(
            <Piechart
              chartID={piechartList[i].id}
              name={piechartList[i].name}
              data={piechartList[i].data}
              onClick={() => this.handlePiechartClick(id)}
            />
          );
        }
        this.setState({ piecharts: finalList });

        // console.log(res.data);
      });
    let finalList = [];
    // const data = [
    //   { name: "North", value: 100 },
    //   { name: "South", value: 200 },
    //   { name: "East", value: 300 },
    // ];
    // const data2 = [
    //   { name: "North", value: 100 },
    //   { name: "South", value: 200 },
    //   { name: "East", value: 900 },
    // ];
    // const data3 = [
    //   { name: "North", value: 100 },
    //   { name: "South", value: 200 },
    // ];

    // finalList.push(
    //   <Piechart
    //     chartID={1}
    //     // isSelected={1 === this.selectedChart}
    //     name={"Deneme1"}
    //     data={data}
    //     onClick={() => this.handlePiechartClick(1, "Deneme1")}
    //   />
    // );
    // finalList.push(
    //   <Piechart
    //     chartID={2}
    //     // isSelected={2 === this.selectedChart}
    //     name={"Deneme2"}
    //     data={data2}
    //     onClick={() => this.handlePiechartClick(2, "Deneme2")}
    //   />
    // );
    // finalList.push(
    //   <Piechart
    //     chartID={3}
    //     // isSelected={2 === this.selectedChart}
    //     name={"Deneme3"}
    //     data={data2}
    //     onClick={() => this.handlePiechartClick(3, "Deneme3")}
    //   />
    // );
    // finalList.push(
    //   <Piechart
    //     chartID={4}
    //     // isSelected={2 === this.selectedChart}
    //     name={"Deneme4"}
    //     data={data3}
    //     onClick={() => this.handlePiechartClick(4, "Deneme4")}
    //   />
    // );

    // for (var i = 0; i < finalList.length; i++) {
    //   if (finalList[i].isHighlited === true) {
    //     this.state.highlitedKey = finalList[i].key;
    //   }
    // }
  }
}

export default PiechartHolder;
