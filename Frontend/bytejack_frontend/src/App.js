import './App.css';
import Table from './components/Table.js'
import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from "./pages/Home.js"
import Table from "./pages/Table.js"



function App() {

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />
            <Route path="table" element={<Table></Table>} />
          </Route>
        </Routes>
      </BrowserRouter>
    </>
    
  );
}

export default App;
