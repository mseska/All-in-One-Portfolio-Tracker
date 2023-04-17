import "./App.css";
import React, { Component } from "react";
import { Route, Routes } from "react-router-dom";
import Login from "./pages/Login/login2";
import Home from "./pages/home";
import SignUp from "./pages/SignUp/signUp";
import News from "./pages/News/news";
import MyPortfolio from "./pages/MyPortfolio/myPortfolio";
import Crypto from "./pages/Crypto/crypto";
import Forecast from "./pages/Forecast/forecast";

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<SignUp />} />
        <Route path="/home" element={<Home />} />
        <Route path="/news" element={<News />} />
        <Route path="/myPortfolio" element={<MyPortfolio />} />
        <Route path="/crypto" element={<Crypto />} />
        <Route path="/forecast" element={<Forecast />} />
      </Routes>
    </>
    // <div className="App">
    //   {/* <Home></Home> */}
    //   {/* <Login></Login>
    //   <SignUp></SignUp> */}
    //   <Login></Login>
    // </div>
  );
}

export default App;
