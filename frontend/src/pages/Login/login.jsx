import React, { useState } from "react";
import image from "../images/1-cropped.svg";
import "./login.css";
import { Component } from "react";

class Login extends Component {
  // constructor() {
  //   super();
  // }

  handleLogin(e) {
    e.preventDefault();

    alert("You clicked Log in.");
  }

  handleSignUpClick() {
    alert("You clicked Sign Up");
  }

  render() {
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
                AIOP Tracker simplifies your financial tracking, making it
                easier to manage and monitor your investments.
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
                <form onSubmit={this.handleLogin}>
                  <input
                    type="text"
                    class="emailInputLogin"
                    placeholder="Email"
                    name="message"
                    // onChange={handleChange}
                    // value={message}
                  />
                  <input
                    placeholder="Password"
                    class="passwordInputLogin"
                    type="password"
                  />

                  <input
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
                      onClick={this.handleSignUpClick}
                      class="signUpButton button"
                      type="submit"
                      value="Sign Up"
                    />
                  </div>
                  <a class="forgetPasswordText" href="/register">
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
}

export default Login;
