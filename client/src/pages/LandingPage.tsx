import React from "react";

import Navbar from "../components/Navbar";
import CheckPhishPage from "./Check";

const LandingPage = () => {
  return (
    <div>
        <Navbar></Navbar>
        <CheckPhishPage></CheckPhishPage>
    </div>
  );
};

export default LandingPage;