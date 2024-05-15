import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from "./pages/Home.js"
import Table from "./pages/Table.js"
import Lobby from './pages/Lobby.js';

function App() {

  return (
    <>
      <BrowserRouter>
        <Routes>
            <Route index element={<Home />} />
            <Route path="table" element={<Table></Table>} />
            <Route path="lobby" element={<Lobby />}/>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
