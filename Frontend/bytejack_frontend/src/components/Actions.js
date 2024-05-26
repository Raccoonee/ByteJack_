import "./cssfiles/Actions.css";
import { useNavigate } from "react-router-dom";

const Actions = ({ socket }) => {
  const navigate = useNavigate();

  const handleHit = () => {
    socket.emit("hit")

  }

  const handleStand = () => {
    socket.emit("stand")
  }

  const handleStatus = (data) => {
    console.log(data)
  }

  const handleLeaveGame = () => {
    socket.emit("leaveGame")
    socket.on("status", handleStatus)
    navigate("/lobby");
  }


  return (
    <div className="center">
      <button class="button-30" onClick={handleLeaveGame}>Leave Game</button>
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
  );
};

export default Actions;
