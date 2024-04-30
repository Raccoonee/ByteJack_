import React from "react";
import './cssfiles/ChipsSection.css'
import PokerChip from "./PokerChip";

const ChipsSection = () => {
    return (
        <div>
            <PokerChip color={"blue"}></PokerChip>
            <PokerChip color={"green"}></PokerChip>
            <PokerChip color={"black"}></PokerChip>
            <div id="money">
                <span id="cash">Cash: $<span></span></span>
                <div id="bank">Winnings: $<span></span></div>
            </div>
        </div>
    )
}

export default ChipsSection