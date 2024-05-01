import React from "react";
import "./cssfiles/PokerChip.css";

const PokerChip = ({ color }) => {
  return <div class={`pokerchip ${color}`}></div>;
};

export default PokerChip;
