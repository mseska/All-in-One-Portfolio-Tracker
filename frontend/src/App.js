import "./App.css";
import React from "react";
import { Route, Routes } from "react-router-dom";
import Login from "./pages/Login/login2";
import Home from "./pages/home";
import SignUp from "./pages/SignUp/signUp";
import News from "./pages/News/news";
import MyPortfolio from "./pages/MyPortfolio/myPortfolio";
import Crypto from "./pages/Crypto/crypto";
import Forecast from "./pages/Forecast/forecast";
import PrivateRoutes from "./components/PrivateRoutes/privateRoute";

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<SignUp />} />
        <Route element={<PrivateRoutes />}>
          <Route element={<Home />} path="/home" />
          <Route element={<News />} path="/news" />
          <Route element={<MyPortfolio />} path="/myPortfolio" />
          <Route element={<Crypto />} path="/crypto" />
          <Route element={<Forecast />} path="/forecast" />
        </Route>
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
