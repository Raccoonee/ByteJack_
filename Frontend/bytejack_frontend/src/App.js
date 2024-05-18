import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useState } from "react";
import Home from "./pages/Home.js";
import Table from "./pages/Table.js";
import Lobby from "./pages/Lobby.js";

function App() {
  const [userData, setUserData] = useState({
    gameID: "",
  });

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route index element={<Home />} />
          <Route path="table" element={<Table userData={userData} setUserData={setUserData} />} />
          <Route path="lobby" element={<Lobby userData={userData} setUserData={setUserData} />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
