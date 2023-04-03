import "./App.css";
import React, { Component } from "react";
// import { Route } from "react-router-dom";
import Login from "./pages/Login/login";
import Home from "./pages/home";
import SignUp from "./pages/SignUp/signUp";

function App() {
  return (
    <div className="App">
      {/* <Home></Home> */}
      {/* <Login></Login>
      <SignUp></SignUp> */}
      <Login></Login>
    </div>
  );
}

export default App;
