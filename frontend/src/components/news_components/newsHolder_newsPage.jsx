import React, { Component } from "react";
import News from "./news";
import axios from "axios";

class NewsHolderNewsPage extends Component {
  state = {
    newsArticles: [],
    count: 0,
  };

  render() {
    return (
      <div className="NewsMainDiv" style={{ marginTop: "5vh" }}>
        {this.state.newsArticles}
      </div>
    );
  }

  componentWillMount() {
    //this request will changed with "news_newspage"
    axios.get("http://localhost:8000/api/news_mainpage").then((res) => {
      var articleList2 = res.data.news;
      console.log(articleList2);
      localStorage.setItem("articleList", JSON.stringify(articleList2));
      let articleList = JSON.parse(localStorage.getItem("articleList"));

      let finalList = [];

      for (var i = 0; i < articleList.length; i++) {
        finalList.push(
          <News
            newsTitle={articleList[i].title}
            newsPublisher={articleList[i].publisher}
            newsImage={articleList[i].thumbnail}
            newsLink={articleList[i].link}
          />
        );
      }
      this.setState({ newsArticles: finalList });
    });
  }
}

export default NewsHolderNewsPage;
