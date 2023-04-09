import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";
import { useNavigate } from "react-router-dom";
import NavBar from "../../components/NavBar/navBar2.jsx";


export default function News() {
  const navigate = useNavigate();

  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css"
  ></link>;

  return (
    <div>
      <NavBar></NavBar>
      <p>News Page</p>
    </div>
  );
}
