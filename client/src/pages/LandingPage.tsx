import React from "react";

import Navbar from "../components/Navbar";
import CheckPhishPage from "./Check";
import Footer from "../components/Footer";

const LandingPage = () => {
  return (
    <div>
      <Navbar></Navbar>
        <CheckPhishPage></CheckPhishPage>
        <Footer></Footer>
    </div>
  );
};

export default LandingPage;