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
      var articleList2 = res.data.news;
      localStorage.setItem("articleList", JSON.stringify(articleList2));
      let articleList = JSON.parse(localStorage.getItem("articleList"));

      let finalList = [];

      for (var i = 0; i < articleList.length; i++) {
        finalList.push(
          <Piechart
            newsTitle={articleList[i].title}
            newsPublisher={articleList[i].publisher}
            newsImage={articleList[i].thumbnail}
            newsLink={articleList[i].link}
          />
        );
      }
      this.setState({ newsArticles: finalList });
    });

    
    // this.setState({ newsArticles: finalList });
  }
  
}

export default PiechartHolder;
