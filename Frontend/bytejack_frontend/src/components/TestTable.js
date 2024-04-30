import './cssfiles/TestTable.css'
import ChipsSection from './ChipsSection.js'
import Actions from './Actions.js';
import React, { useEffect } from "react";
import Player from "./Player";
import Dealer from "./Dealer"

let test = {
    "gameID": 12345,
    "playerTurn": "player1",
    "Dealer": {"hand": ["A♠", "A♥"]},
    "winners": ["player1", "player2"],
    "Players": {
        "player1": {"name": "Jeremiah", "chips": 100, "hand": ["A♥", "A♦", "A♠", "A♣"], "bet": 10},
        "player2": {"name": "Bob", "chips": 100, "hand": ["K♠", "10♥"], "bet": 10},
        "player3": {"name": "Bob", "chips": 100, "hand": ["K♠", "10♥"], "bet": 10},
        "player4": {"name": "Bob", "chips": 100, "hand": ["K♠", "10♥"], "bet": 10},
        "player5": {"name": "Bob", "chips": 100, "hand": ["K♠", "10♥"], "bet": 10}
    }
}

const TestTable = () => {
    useEffect(() => {
        fetch('http://api:5001/ppp')
        .then(response => response.json())
        .then(data => console.log(data));
    }, []
    );
    return (
        <>
            <div class="parent">
                <div class="div1"> <Player name={test.Players.player1.name} bet={test.Players.player1.bet} hand={test.Players.player1.hand}></Player> </div>
                <div class="div2"> <Player></Player></div>
                <div class="div3"> <Actions></Actions></div>
                <div class="div4"> <Dealer dealerHand={test.Dealer.hand}></Dealer></div>
                <div class="div5"> <ChipsSection></ChipsSection></div>
                <div class="div6"> <Player></Player></div>
                <div class="div7"> <Player></Player></div>
                <div class="div8"> <Player></Player></div>
            </div>
        </>
    );
};

export default TestTable;
