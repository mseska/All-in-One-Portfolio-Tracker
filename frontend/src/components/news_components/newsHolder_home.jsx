import React, { Component } from "react";
import News from "./news";
import axios from "axios";

class NewsHolderHomePage extends Component {
  state = {
    newsArticles: [],
    count: 0,
  };

  render() {
    return (
      <div className="article-card-container">{this.state.newsArticles}</div>
    );
  }

  componentWillMount() {
    axios.get("http://localhost:8000/api/news_mainpage").then((res) => {
      var articleList2 = res.data.TSLA;
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

    // finalList.push(
    //   <News
    //     newsTitle="Title of news 1"
    //     newsImage="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg"
    //     newsLink="https://www.google.com/search?q=images&sxsrf=APwXEdf-oHAC3cd8cDTejaej2a7GSJe5dw:1681901376891&source=lnms&tbm=isch&sa=X&ved=2ahUKEwifk_fw4rX-AhUtQ_EDHW54DVAQ_AUoAXoECAEQAw&biw=1440&bih=821&dpr=2#imgrc=9SPhZ2nyEGps3M"
    //   />
    // );
    // finalList.push(
    //   <News
    //     newsTitle="Title of news 1"
    //     newsImage="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg"
    //     newsLink="https://www.google.com/search?q=images&sxsrf=APwXEdf-oHAC3cd8cDTejaej2a7GSJe5dw:1681901376891&source=lnms&tbm=isch&sa=X&ved=2ahUKEwifk_fw4rX-AhUtQ_EDHW54DVAQ_AUoAXoECAEQAw&biw=1440&bih=821&dpr=2#imgrc=9SPhZ2nyEGps3M"
    //   />
    // );
    // this.setState({ newsArticles: finalList });
  }
}

export default NewsHolderHomePage;
