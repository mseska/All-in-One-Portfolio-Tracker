import React, { Component } from "react";
import axios from "axios";
import Piechart from "./piechart";

class PiechartHolder extends Component {
  state = {
    piecharts: [],
    count: 0,
  };

  

  render() {
    return (
      <div style={{display: "flex",}}>
        <Piechart></Piechart>
        <Piechart></Piechart>
        <Piechart></Piechart>
        <Piechart></Piechart>
        <Piechart></Piechart>
        <Piechart></Piechart>
        <Piechart></Piechart>

        
      </div>
    );
  }
  componentWillMount() {
    axios.get("http://localhost:8000/api/get_portfolios").then((res) => {
        params: { id: localStorage.getItem("userToken") }

    });

    
  }
  
}

export default PiechartHolder;
