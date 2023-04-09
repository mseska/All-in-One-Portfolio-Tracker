import React, { useState } from "react";
import image from "../images/1-cropped.svg";
import "./login.css";
import { Component } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";


export default function Login2() {
  // const [fields, handleFieldChange] = useFormFields({
  //   email: "",
  //   password: ""
  // });
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  

  const handleMessageChange = (event) => {
    // 👇️ access textarea value
    // const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // axios.defaults.xsrfHeaderName = 'X-CSRFToken';
    // axios.defaults.xsrfCookieName = 'csrftoken';
    // axios.defaults.headers.common['X-CSRFToken'] = csrftoken;
    setMessage(event.target.value);
    console.log("console log:",event.target.value);
    axios
      .post("http://localhost:8000/api/items/",{
          name: message
        })
      .then((response) => {
        console.log("response get as",response.data);
      })
      .catch((error) => {
        console.log(error);
      });
    // axios
    //   .get("http://localhost:8000/api/items/",{
    //     params: {
    //       name: message
    //     }})
    //   .then((response) => {
    //     console.log("response get as",response.data);
    //   })
    //   .catch((error) => {
    //     console.log(error);
    //   });
      
  };

  function handleSubmit(event) {
    event.preventDefault();
  }

  
  function handleLogin() {
    
    //alert("after navigation message get in this page is",message);
    navigate("home");
    // alert("You clicked Log in.");
    
  }

  function handleSignUpClick() {
    navigate("register");
  }

  return (
    <div>
      <header>
        <title>AIOPT - Log in</title>
      </header>
      <body>
        <div className="Login">
          <div class="AIOP_symbol">
            <img class="image1" src={image} alt="1.svg" />
          </div>
          <div>
            <h2 class="subTitle">
              AIOP Tracker simplifies your financial tracking, making it easier
              to manage and monitor your investments.
            </h2>
          </div>
          <div class="loginPanel">
            <div>
              <div class="loginToBlock">
                <span class=" loginToSpan">
                  <div class="loginToText"> Login in to AIOP Tracker</div>
                </span>
                <hr
                  style={{
                    backgroundColor: "black",
                    height: "0.5px",
                  }}
                />
              </div>
              <form>
                <input
                  type="text"
                  class="emailInputLogin"
                  placeholder="Email"
                  name="message"
                  onChange={handleMessageChange}
                  // value={message}
                />
                <input
                  placeholder="Password"
                  class="passwordInputLogin"
                  type="password"
                />

                <input
                  onClick={handleLogin}
                  class="loginButton button"
                  type="submit"
                  value="Log in"
                />
              </form>
              <div class="belowLoginButton">
                <div
                  style={{
                    display: "flex",
                    flexDirection: "row",
                    alignItems: "center",
                  }}
                >
                  <div
                    style={{
                      flex: 1,
                      height: "1px",
                      backgroundColor: "black",
                    }}
                  />

                  <div>
                    <p style={{ width: "150px", textAlign: "center" }}>
                      Not registered yet?
                    </p>
                  </div>

                  <div
                    style={{
                      flex: 1,
                      height: "1px",
                      backgroundColor: "black",
                    }}
                  />
                </div>
                <div>
                  <input
                    onClick={handleSignUpClick}
                    class="signUpButton button"
                    type="submit"
                    value="Sign Up"
                  />
                </div>
                <a class="forgetPasswordText" href="">
                  Forget Password?
                </a>
              </div>
            </div>
          </div>
        </div>
        {/* <Home></Home> */}
      </body>
    </div>
  );
}
