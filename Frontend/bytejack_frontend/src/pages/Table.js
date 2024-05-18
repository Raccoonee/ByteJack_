import "./Table.css";
import ChipsSection from "../components/ChipsSection.js";
import Actions from "../components/Actions.js";
import React, { useEffect, useState } from "react";
import { testData } from "../utils/testdata.js";
import { socket } from "../utils/socket.js";
import Player from "../components/Player.js";
import Dealer from "../components/Dealer.js";

const Table = ({ userData }) => {
  const [gameState, setGameState] = useState(undefined);

  const handleUpdate = (data) => {
    setGameState(data)
  }

  const handleStatus = (data) => {
    console.log(data)
  }

  const handleThisDick = (data) => {
    console.log(data)
  }

  useEffect(() => {
    socket.emit("join", {lobbyCode: userData.gameID})
    socket.emit("penis")

    socket.on("update", handleUpdate)
    socket.on("status", handleStatus)
    socket.on("penis", handleThisDick)
    console.log(gameState)
  }, []);

  return (
    <>
      <div class="background">
        <div class="parent">
          <div class="div1">
            {gameState !== undefined ? (
              <Player
                name={gameState.players.player1.name}
                bet={gameState.players.player1.bet}
                hand={gameState.players.player1.hand}
                chips={gameState.players.player1.chips}
              ></Player>
            ) : (
              "Empty"
            )}
          </div>
          <div class="div2">
            {gameState !== undefined ? (
              <Player
                name={gameState.players.player2.name}
                bet={gameState.players.player2.bet}
                hand={gameState.players.player2.hand}
                chips={gameState.players.player2.chips}
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
              <Dealer dealerHand={gameState.dealer.hand}></Dealer>
            ) : (
              "Empty"
            )}
            {userData.gameID}
          </div>
          <div class="div5">
            <ChipsSection socket={socket}></ChipsSection>
          </div>
          <div class="div6">
            {gameState !== undefined ? (
              <Player
                name={gameState.players.player3.name}
                bet={gameState.players.player3.bet}
                hand={gameState.players.player3.hand}
                chips={gameState.players.player3.chips}
              ></Player>
            ) : (
              "Empty"
            )}
          </div>
          <div class="div7">
            {gameState !== undefined ? (
              <Player
                name={gameState.players.player4.name}
                bet={gameState.players.player4.bet}
                hand={gameState.players.player4.hand}
                chips={gameState.players.player4.chips}
              ></Player>
            ) : (
              "Empty"
            )}
          </div>
          <div class="div8">
            {gameState !== undefined ? (
              <Player
                name={gameState.players.player5.name}
                bet={gameState.players.player5.bet}
                hand={gameState.players.player5.hand}
                chips={gameState.players.player5.chips}
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
