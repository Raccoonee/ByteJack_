import React, { useState } from "react";
import "./cssfiles/Actions.css";

const Actions = ({ socket }) => {
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
