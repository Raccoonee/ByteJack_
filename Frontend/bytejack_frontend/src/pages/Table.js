import "./Table.css";
import ChipsSection from "../components/ChipsSection.js";
import Actions from "../components/Actions.js";
import React, { useEffect, useState } from "react";
import { testData } from "../utils/testdata.js";
import { socket } from "../utils/socket.js";
import Player from "../components/Player.js";
import Dealer from "../components/Dealer.js";
// import axios from 'axios';

const Table = () => {
  const [gameState, setGameState] = useState(testData);

  useEffect(() => {
    const onUpdate = (value) => {
      setGameState(value);
      console.log(gameState);
      console.log(value);
    };


    socket.on("join", () => {
      socket.send({gameID: "new"})
    })
  }, [gameState]);

  return (
    <>
      <div class="background">
        <div class="parent">
          <div class="div1">
            {gameState !== undefined ? (
              <Player
                name={gameState.Players.player1.name}
                bet={gameState.Players.player1.bet}
                hand={gameState.Players.player1.hand}
                chips={gameState.Players.player1.chips}

              ></Player>
            ) : (
              "Empty"
            )}
          </div>
          <div class="div2">
            {gameState !== undefined ? (
              <Player
                name={gameState.Players.player2.name}
                bet={gameState.Players.player2.bet}
                hand={gameState.Players.player2.hand}
                chips={gameState.Players.player2.chips}

              ></Player>
            ) : (
              "Empty"
            )}
          </div>
          <div class="div3">
            <Actions socket={socket} gameState={gameState}></Actions>
          </div>
          <div class="div4">
            {gameState !== undefined ? (
              <Dealer dealerHand={gameState.Dealer.hand}></Dealer>
            ) : (
              "Empty"
            )}
          </div>
          <div class="div5">
            <ChipsSection socket={socket}></ChipsSection>
          </div>
          <div class="div6">
            {gameState !== undefined ? (
              <Player
                name={gameState.Players.player3.name}
                bet={gameState.Players.player3.bet}
                hand={gameState.Players.player3.hand}
                chips={gameState.Players.player3.chips}
              ></Player>
            ) : (
              "Empty"
            )}
          </div>
          <div class="div7">
            {gameState !== undefined ? (
              <Player
                name={gameState.Players.player4.name}
                bet={gameState.Players.player4.bet}
                hand={gameState.Players.player4.hand}
                chips={gameState.Players.player4.chips}

              ></Player>
            ) : (
              "Empty"
            )}
          </div>
          <div class="div8">
            {gameState !== undefined ? (
              <Player
                name={gameState.Players.player5.name}
                bet={gameState.Players.player5.bet}
                hand={gameState.Players.player5.hand}
                chips={gameState.Players.player5.chips}

              ></Player>
            ) : (
              "Empty"
            )}
          </div>
        </div>
      </div>
    </>
  );
};

export default Table;
