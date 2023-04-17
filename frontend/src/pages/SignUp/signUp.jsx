import React, { useState } from "react";
import { Component } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import image from "../images/1-cropped.svg";
import "./signUp.css";

export default function SignUp() {
  const [name, setName] = useState("");
  const [surname, setSurname] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [isLoading, setIsLoading] = useState(false);

  const navigate = useNavigate();

  const handleNameChange = (event) => {
    setName(event.target.value);
  };
  const handleSurnameChange = (event) => {
    setSurname(event.target.value);
  };
  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };
  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  async function handleSignUp(event) {
    event.preventDefault();
    setIsLoading(true);

    axios
      .post("http://localhost:8000/api/signUp/", {
        name: name,
        surname: surname,
        email: email,
        password: password,
      })
      .then(function (response) {
        alert("sign-up successful");
        navigate("/");
      })
      .catch(function (error) {
        alert("Could not signUp");
        navigate("/");
        console.log(name);
        console.log(surname);
        console.log(email);
        console.log(password);
        setIsLoading(false);
      })
      .finally((response) => {});
  }

  return (
    <div>
      <header>
        <title>AIOPT - Sign Up</title>
      </header>
      <body>
        <div className="signUp">
          <div>
            <img class="signUpLogo" src={image} alt="logo1.svg" />
          </div>
          <div>
            <h2 class="subTitle">
              Welcome to AIOP Tracker. You are just one step away from your
              unique financial tracking application.
            </h2>
          </div>
          <div class="signUpPanel">
            <div class="signUpTextBlock">
              <p class="signUpText">
                {" "}
                Sign Up to start managing your financial portfolio.
              </p>
              {/* </span> */}
              <hr
                style={{
                  backgroundColor: "black",
                  height: "0.5px",
                }}
              />
            </div>
            <div class="signUpButtonsDiv">
              <input
                type="text"
                class="emailInput"
                placeholder="Name"
                name="message"
                onChange={handleNameChange}
              />
              <input
                type="text"
                class="emailInput"
                placeholder="Surname"
                name="message"
                onChange={handleSurnameChange}
              />
              <input
                type="text"
                class="emailInput"
                placeholder="Email"
                name="message"
                onChange={handleEmailChange}
              />
              <input
                type="password"
                class="emailInput"
                placeholder="Password"
                name="message"
                onChange={handlePasswordChange}
              />
              <form>
                <input
                  class="signUpButton button"
                  type="submit"
                  value="SIGN UP"
                  onClick={handleSignUp}
                />
              </form>
              <div
                style={{
                  display: "flex",
                  flexDirection: "row",
                  alignItems: "center",
                }}
              ></div>
            </div>
            <div className="belowSignUp">
              <hr
                style={{
                  backgroundColor: "black",
                  height: "0.5px",
                }}
              />
              <p
                style={{
                  color: "black",
                  alignSelf: "center",
                  display: "inline-block",
                  marginRight: "10px",
                  marginTop: "10px",
                  marginBottom: "20px",
                }}
              >
                Already have an account?
              </p>

              <a className="goToLoginPage" href="/">
                Log in
              </a>
            </div>
          </div>
        </div>
      </body>
    </div>
  );
}
