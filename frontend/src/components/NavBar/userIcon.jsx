import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";
import { useNavigate } from "react-router-dom";
import NavBar from "../../components/NavBar/navBar2.jsx";
import "./userIcon.css";

export default function UserIcon() {
  const navigate = useNavigate();

  function signOut() {
    navigate("/");
  }

  return (
    <div className="user-icon-menu">
      <div className="nameDiv">Tuna Önal</div>
      {/* <div className="signOutButtonDiv"> </div> */}
      <div
                    style={{
                      flex: 1,
                      height: "1px",
                      backgroundColor: "black",
                    }}
                  />
      <button className="userIconMenuButton" onClick={signOut}>
        Sign Out
      </button>
    </div>
  );
}
