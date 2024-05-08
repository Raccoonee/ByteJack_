import './App.css';
import React, { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from "./pages/Home.js"
import Table from "./pages/Table.js"



function App() {

  return (
    <>
      <BrowserRouter>
        <Routes>
            <Route index element={<Home />} />
            <Route path="table" element={<Table></Table>} />
        </Routes>
      </BrowserRouter>
    </>
    
  );
}

export default App;
