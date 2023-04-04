import React, { Component } from "react";
import image from "../images/1-cropped.svg";
import "./signUp.css";

class signUp extends Component {
  state = {};
  render() {
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
                  placeholder="Mobile Number or Email"
                  name="message"
                />
                <input
                  type="text"
                  class="emailInput"
                  placeholder="Name"
                  name="message"
                />
                <input
                  type="text"
                  class="emailInput"
                  placeholder="Surname"
                  name="message"
                />
                <input
                  type="password"
                  class="emailInput"
                  placeholder="Password"
                  name="message"
                />
                <form onSubmit={this.handleLogin}>
                  <input
                    class="signUpButton button"
                    type="submit"
                    value="SIGN UP"
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
}

export default signUp;
