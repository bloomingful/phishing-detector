import React from "react";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

interface Props {
  children: React.ReactNode;
}
const BasePage = (props: Props) => {
  return (
    <nav>
      <Navbar></Navbar>
      <Footer></Footer>
    </nav>
  );
};

export default BasePage;