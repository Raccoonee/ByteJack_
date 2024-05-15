import "./cssfiles/ChipsSection.css";
import PokerChip from "./PokerChip";
import { useState } from "react";

const ChipsSection = ({ socket }) => {
  const [formData, setFormData] = useState("");

  const handleChange = (event) => {
    setFormData(event.target.value);
  };

  const handleBet = (event) => {
    if(Number.isInteger(event) && event > 0) {
      socket.emit("bet", {bet: event})
    }
  };

  return (
    <div>
      <PokerChip color={"blue"}></PokerChip>
      <PokerChip color={"green"}></PokerChip>
      <PokerChip color={"black"}></PokerChip>
      <div id="money">
        <>
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
            <button class="button-30" type="submit">
              Submit
            </button>
          </form>
        </>
      </div>
    </div>
  );
};

export default ChipsSection;
