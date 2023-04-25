import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";
import { useNavigate } from "react-router-dom";
import NavBar from "../../components/NavBar/navBar2.jsx";
import NewsPageNewsHolder from "../../components/news_components/newsHolder_newsPage";



export default function News() {
  const navigate = useNavigate();

  

  return (
    <div>
      <NavBar></NavBar>
      <NewsPageNewsHolder></NewsPageNewsHolder>
      {/* <p>News Page</p> */}
    </div>
  );
}
