import "./cssfiles/ChipsSection.css";
import PokerChip from "./PokerChip";
import { useState } from "react";

const ChipsSection = ({ socket }) => {
  const [formData, setFormData] = useState("");

  const handleChange = (event) => {
    setFormData(event.target.value);
  };

  const handleBet = (event) => {
    event.preventDefault();
    if (Number.isInteger(Number.parseInt(formData)) && formData > 0) {
      console.log(formData)
      socket.emit("bet", { bet: formData });
    }
  };

  return (
    <div id="parent">
      <div class="child">
        <PokerChip color={"blue"}></PokerChip>
        <PokerChip color={"green"}></PokerChip>
        <PokerChip color={"black"}></PokerChip>
      </div>
      <div class="child container">
        <form onSubmit={handleBet}>
          <label htmlFor="Wager">Wager:</label>
          <input
            className="input item"
            type="text"
            id="wager"
            name="wager"
            value={formData}
            onChange={handleChange}
          />
          <button class="button-30 item" type="submit">
            Submit
          </button>
        </form>
      </div>
    </div>
  );
};

export default ChipsSection;
