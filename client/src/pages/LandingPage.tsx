import React from "react";

import Navbar from "../components/Navbar";
import CheckPhishPage from "./Check";

const LandingPage = () => {
  return (
      <div>
        <Navbar></Navbar>
        <div>
          <CheckPhishPage></CheckPhishPage>
        </div>
      </div>
  );
};

export default LandingPage;