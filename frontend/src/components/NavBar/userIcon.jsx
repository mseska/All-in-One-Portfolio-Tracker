import React, { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.css";
import { useNavigate } from "react-router-dom";
import "./userIcon.css";
import axios from "axios";

export default function UserIcon() {
  const navigate = useNavigate();
  const [name, setName] = useState("");
  const [surname, setSurname] = useState("");
  const [email, setEmail] = useState("");


  useEffect(() => {
    axios
      .get("http://localhost:8000/api/get-user-info-user-icon", {
        params: { id: localStorage.getItem("userId") },
      })
      .then((res) => {
        // Update name and email state with the response data
        setName(res.data.first_name);
        setSurname(res.data.last_name);
        setEmail(res.data.email);
        console.log(res);
        localStorage.setItem("userName", res.data.name);
        localStorage.setItem("email", res.data.email);
      })
      .catch((err) => {
        setName("error");
        console.error(err);
      });
  }, []);

  function signOut() {
    localStorage.clear();
    navigate("/");
  }

  return (
    <div className="user-icon-menu">
      <div className="nameDiv">
        {name} {surname} {email}
      </div>
      {/* <div className="signOutButtonDiv"> </div> */}
      <div
        style={{
          flex: 1,
          height: "1px",
          backgroundColor: "black",
        }}
      />
      <div className="userIconMenuButtonDiv">
        <button className="userIconMenuButton" onClick={signOut}>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            className="bi bi-box-arrow-right aa"
            viewBox="0 0 16 16"
          >
            <path
              fill-rule="evenodd"
              d="M10 12.5a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v2a.5.5 0 0 0 1 0v-2A1.5 1.5 0 0 0 9.5 2h-8A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-2a.5.5 0 0 0-1 0v2z"
            />
            <path
              fill-rule="evenodd"
              d="M15.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708.708L14.293 7.5H5.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z"
            />
          </svg>
          Sign Out
        </button>
      </div>
    </div>
  );
}
