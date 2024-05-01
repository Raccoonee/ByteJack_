import React, { useState } from "react";
import "./cssfiles/Actions.css";

const Actions = () => {
  const [formData, setFormData] = useState("");

  const handleChange = (event) => {
    setFormData(event.target.value);
  };

  const handleBet = (event) => {
    event.preventDefault();
    // api socket call to send user bet
    alert(`${formData}`);
  };

  return (
    <div className="center">
      <span>
        <div className="padding">
          <button class="button-30" role="button">
            Hit
          </button>
          <button class="button-30" role="button">
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
