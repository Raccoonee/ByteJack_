import "./cssfiles/TestTable.css";
import ChipsSection from "./ChipsSection.js";
import Actions from "./Actions.js";
import React, { useEffect, useState } from "react";
import Player from "./Player";
import Dealer from "./Dealer";
import axios from 'axios';

const testData = {
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

const TestTable = ( {socket }) => {
  const [isConnected, setIsConnected] = useState(socket.connected);
  const [gameState, setGameState] = useState(testData);
  
  useEffect(() => {
    // axios.get('/test1')
    // .then(res => {
    //   console.log(res.data)
    // })

    const onConnect=() => {
      setIsConnected(true);
    }
    
    const onUpdate=(value) => {
      setGameState(value);
      console.log(value)
    }

    socket.connect("connect", onUpdate)
    socket.on('update', onUpdate)

  }, []);
  return (
    <>
      <div class="parent">
        <div class="div1">
          <Player
            name={gameState != undefined ? gameState.Players.player1.name : testData.Players.player1.name}
            bet={gameState != undefined ? gameState.Players.player1.bet : testData.Players.player1.bet}
            hand={gameState != undefined ? gameState.Players.player1.hand : testData.Players.player1.hand}
          ></Player>
        </div>
        <div class="div2">
          <Player
            name={gameState != undefined ? gameState.Players.player2.name : testData.Players.player2.name}
            bet={gameState != undefined ? gameState.Players.player2.bet : testData.Players.player2.bet}
            hand={gameState != undefined ? gameState.Players.player2.hand : testData.Players.player2.hand}
          ></Player>
        </div>
        <div class="div3">
          <Actions 
            socket={socket}
            gameState={gameState}
          ></Actions>
        </div>
        <div class="div4">
          <Dealer dealerHand={gameState != undefined ? gameState.Dealer.hand : testData.Dealer.hand}></Dealer>
        </div>
        <div class="div5">
          <ChipsSection></ChipsSection>
        </div>
        <div class="div6">
          <Player
            name={gameState != undefined ? gameState.Players.player3.name : testData.Players.player3.name}
            bet={gameState != undefined ? gameState.Players.player3.bet : testData.Players.player3.bet}
            hand={gameState != undefined ? gameState.Players.player3.hand : testData.Players.player3.hand}
          ></Player>
        </div>
        <div class="div7">
          <Player
            name={gameState != undefined ? gameState.Players.player4.name : testData.Players.player4.name}
            bet={gameState != undefined ? gameState.Players.player4.bet : testData.Players.player4.bet}
            hand={gameState != undefined ? gameState.Players.player4.hand : testData.Players.player4.hand}
          ></Player>
        </div>
        <div class="div8">
          <Player
            name={gameState != undefined ? gameState.Players.player5.name : testData.Players.player5.name}
            bet={gameState != undefined ? gameState.Players.player5.bet : testData.Players.player5.bet}
            hand={gameState != undefined ? gameState.Players.player5.hand : testData.Players.player5.hand}
          ></Player>
        </div>
      </div>
    </>
  );
};

export default TestTable;
