import React, { useState, useEffect } from "react";
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


  const clearLocalStorage = () => {
    localStorage.clear();
  };

  useEffect(() => {
    // Call the function when the Login page is opened
    clearLocalStorage();
  }, []);


  const [isLoading, setIsLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleEmailChange = (event) => {
    // setMessage(event.target.value);
    // console.log("console log:", event.target.value);
    // axios
    //   .post("http://localhost:8000/api/items/", {
    //     name: message,
    //   })
    //   .then((response) => {
    //     console.log("response get as", response.data);
    //   })
    //   .catch((error) => {
    //     console.log(error);
    //   });

    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  async function handleLogin(event) {
    event.preventDefault();
    setIsLoading(true);

    axios
      .post("http://localhost:8000/api/login/", {
        eMail: email,
        PassWord: password,
      })
      .then((response) => {
        const token = response.data.token;
        // local storageta userId ve userToken tutarsak diğer sayfalarda
        // bunları requestlere ekleyerek o userın datasını getleyebiliriz

        if (response.status === 200) {
          localStorage.setItem("userId", response.data.id);
          localStorage.setItem("userToken", response.data.token);
          console.log(response.data.user_id);
          console.log(response.data.token);
          navigate("home");
        }
      })
      .catch(function (error) {
        alert("The email address you entered could not be validated.");
        // navigate("/home");
        // console.log(email);
        // console.log(password);
        setIsLoading(false);
      })
      .finally((response) => {});
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
                  onChange={handleEmailChange}
                  // value={message}
                />
                <input
                  placeholder="Password"
                  class="passwordInputLogin"
                  type="password"
                  onChange={handlePasswordChange}
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
