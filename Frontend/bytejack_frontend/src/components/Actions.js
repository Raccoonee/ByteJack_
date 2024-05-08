import React, { useState, useEffect } from "react";

import "./cssfiles/Actions.css";

const Actions = ({ socket, gameState }) => {
  const [formData, setFormData] = useState("");

  const handleChange = (event) => {
    setFormData(event.target.value);
  };

  const handleBet = (event) => {
    if(Number.isInteger(event) && event > 0) {
      socket.emit("bet", event)
      event.preventDefault();
    }
  };


  const handleHit = () => {
    socket.emit("hit")

  }

  const handleStand = () => {
    socket.emit("stand")
  }

  return (
    <div className="center">
      <span>
        <div className="padding">
          <button class="button-30" role="button" onClick={handleHit}>
            Hit
          </button>
          <button class="button-30" role="button" onClick={handleStand}>
            Stand
          </button>
        </div>
        <form onSubmit={handleBet}>
          <label htmlFor="Wager">Wager:</label>
          <input
            className="input"
            type="text"
            id="wager"
            name="wager"
            value={formData}
            onChange={handleChange}
          />
          <button class="button-30" type="submit">Submit</button>
        </form>
      </span>
    </div>
  );
};

export default Actions;
