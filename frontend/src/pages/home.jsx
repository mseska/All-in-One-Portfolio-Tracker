import * as React from "react";

// import IconButton from "@mui/material/IconButton";
// import Typography from "@mui/material/Typography";

// import Container from "@mui/material/Container";
// import Avatar from "@mui/material/Avatar";
// import Button from "@mui/material/Button";

import "./home.css";
import NavBar from "../components/NavBar/navBar";

const pages = ["Products", "Pricing", "Blog"];
const settings = ["Profile", "Account", "Dashboard", "Logout"];

function ResponsiveAppBar() {
  return (
    <div>
      <NavBar></NavBar>
      <div className="BelowNavBar">
        <div className="NewsDiv">{/* <button>hello</button> */}</div>
        <div className="HomePageTables">
          <section>
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">Symbol</th>
                  <th scope="col">Last Price</th>
                  <th scope="col">Change</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Mark</td>
                  <td>Otto</td>
                  <td>@mdo</td>
                </tr>
                <tr>
                  <td>Jacob</td>
                  <td>Thornton</td>
                  <td>@fat</td>
                </tr>
                <tr>
                  <td colspan="2">Larry the Bird</td>
                  <td>@twitter</td>
                </tr>
              </tbody>
            </table>
          </section>
        </div>
      </div>
    </div>
  );
}

export default ResponsiveAppBar;
