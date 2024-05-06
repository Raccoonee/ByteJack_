import './App.css';
import Table from './components/Table.js'
import { socket } from './utils/socket.js'
import React, { useEffect, useState } from "react";


function App() {
  const [joinedGame, setJoinedGame] = useState(false)

  const handleJoin = () => {
    setJoinedGame(true)
  }

  return (
    <>
      {joinedGame === true ? <Table socket={socket} setJoinedGame={setJoinedGame}></Table> :
       <button onClick={handleJoin}>
       join
      </button> }
    </>
    
  );
}

export default App;
