import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import Predict from "./pages/Predict";
import Upload from "./pages/Upload";
import History from "./pages/History";

const App = () => {
  return (
    <Router>
      <nav className="bg-blue-600 text-white p-4 flex justify-center gap-6 text-lg font-semibold">
        <Link to="/">Home</Link>
        <Link to="/predict">Predict</Link>
        <Link to="/upload">Upload</Link>
        <Link to="/history">History</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/predict" element={<Predict />} />
        <Route path="/upload" element={<Upload />} />
        <Route path="/history" element={<History />} />
      </Routes>
    </Router>
  );
};

export default App;
