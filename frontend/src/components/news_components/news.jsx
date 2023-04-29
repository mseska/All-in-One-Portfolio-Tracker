import React, { Component } from "react";
import axios from "axios";
import "./news.css";
import { Navigate, useHref } from "react-router-dom";

class News extends Component {
  state = {
    newsTitle: "",
    newsImage: "",
    newsLink: "",
    newsPublisher: "",
  };

  handleClick = () => {
    alert(this.props.newsTitle);
    window.open(
      `https://www.google.com/search?q=${this.props.newsPublisher} + ${this.props.newsTitle}`,
      "_blank"
    );
  };

  render() {
    return (
      <div className="news-container ">
        <div className="t1">
          <img src={this.props.newsImage} alt="News" className="news-image" />
        </div>
        <div>
          <h3 className="news-title">{this.props.newsTitle}</h3>
          <a onClick={this.handleClick} className="news-publisher">
            {this.props.newsPublisher}{" "}
          </a>
        </div>
      </div>
    );
  }
}

export default News;
