import React from "react";
import { Routes, Route, BrowserRouter } from "react-router-dom";

import LandingPage from "./pages/LandingPage";

const App = () => {
  return (
    <>
      <BrowserRouter>
              <Routes>
                <Route path="/" element={<LandingPage></LandingPage>} />
              </Routes>
      </BrowserRouter>
    </>
  );
};

export default App;
