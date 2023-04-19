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
    alert("You Clicked news image");
  };

  render() {
    return (
      <div className="news-container">
        <img
          src={this.props.newsImage}
          alt="News"
          className="news-image"
          onClick={this.handleClick}
        />
        <h3 className="news-title">{this.props.newsTitle}</h3>
        <h3 className="news-publisher">{this.props.newsPublisher}</h3>
      </div>
    );
  }
}

export default News;
