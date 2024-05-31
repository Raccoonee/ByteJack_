import { useState, useEffect } from "react";
import "./cssfiles/Actions.css";
import { useNavigate } from "react-router-dom";

const Actions = ({ socket, gameState }) => {
  const navigate = useNavigate();
  const [timer, setTimer] = useState(10);

  const handleHit = () => {
    socket.emit("hit");
  };

  const handleStand = () => {
    socket.emit("stand");
  };

  const handleStatus = (data) => {
    console.log(data);
  };

  const handleLeaveGame = () => {
    socket.emit("leaveGame");
    socket.on("status", handleStatus);
    navigate("/lobby");
  };

  useEffect(() => {
    if (gameState?.gameFinished === true) {
      if (timer > 0) {
        setTimeout(() => setTimer(timer - 1), 1000);
      } else {
          handleNextRound();
          setTimer(10)
      }
    }
  }, [gameState, timer]);

  const handleNextRound = () => {
    socket.emit("startNewGame");
  };

  return (
    <>
      <div className="center">
        <button class="button-30" onClick={handleLeaveGame}>
          Leave Game
        </button>
        <span>
          <div className="padding">
            <button class="button-30" onClick={handleHit}>
              Hit
            </button>
            <button class="button-30" onClick={handleStand}>
              Stand
            </button>
          </div>
        </span>
      </div>
      <div className="center">
        {gameState?.gameFinished === true
          ? `Next round starting in ${timer} seconds.`
          : ""}
      </div>
    </>
  );
};

export default Actions;
