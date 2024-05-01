import "./cssfiles/TestTable.css";
import ChipsSection from "./ChipsSection.js";
import Actions from "./Actions.js";
import React, { useEffect } from "react";
import Player from "./Player";
import Dealer from "./Dealer";

const test = {
  gameID: 12345,
  playerTurn: "player1",
  Dealer: { hand: ["K♠", "2♣", "3♦"] },
  winners: ["player1", "player2"],
  Players: {
    player1: {
      name: "Jeremiah",
      chips: 100,
      hand: ["A♥", "A♦", "A♠", "2♣"],
      bet: 10,
    },
    player2: { name: "Joe", chips: 100, hand: ["K♠", "10♥"], bet: 10 },
    player3: { name: "Bob", chips: 100, hand: ["K♠", "8♥"], bet: 10 },
    player4: { name: "John", chips: 100, hand: ["Q♠", "9♥"], bet: 10 },
    player5: { name: "Matt", chips: 100, hand: ["K♠", "A♥"], bet: 10 },
  },
};

const TestTable = () => {
  useEffect(() => {
    // fetch('http://api:5001/ppp')
    // .then(response => response.json())
    // .then(data => console.log(data));
  }, []);
  return (
    <>
      <div class="parent">
        <div class="div1">
          <Player
            name={test.Players.player1.name}
            bet={test.Players.player1.bet}
            hand={test.Players.player1.hand}
          ></Player>
        </div>
        <div class="div2">
          <Player
            name={test.Players.player2.name}
            bet={test.Players.player2.bet}
            hand={test.Players.player2.hand}
          ></Player>
        </div>
        <div class="div3">
          <Actions></Actions>
        </div>
        <div class="div4">
          <Dealer dealerHand={test.Dealer.hand}></Dealer>
        </div>
        <div class="div5">
          <ChipsSection data={test.Players}></ChipsSection>
        </div>
        <div class="div6">
          <Player
            name={test.Players.player3.name}
            bet={test.Players.player3.bet}
            hand={test.Players.player3.hand}
          ></Player>
        </div>
        <div class="div7">
          <Player
            name={test.Players.player4.name}
            bet={test.Players.player4.bet}
            hand={test.Players.player4.hand}
          ></Player>
        </div>
        <div class="div8">
          <Player
            name={test.Players.player5.name}
            bet={test.Players.player5.bet}
            hand={test.Players.player5.hand}
          ></Player>
        </div>
      </div>
    </>
  );
};

export default TestTable;
