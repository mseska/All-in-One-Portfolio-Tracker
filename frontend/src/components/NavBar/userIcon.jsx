import React, { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.css";
import { useNavigate } from "react-router-dom";
import NavBar from "../../components/NavBar/navBar2.jsx";
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
        localStorage.setItem("userName",res.data.name);
        localStorage.setItem("email", res.data.email);
      })
      .catch((err) => {
        setName("error");
        console.error(err);
      });
  }, []);

  function signOut() {
    navigate("/");
  }

  return (
    <div className="user-icon-menu">
      <div className="nameDiv">{name}  {surname} {email}</div>
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
