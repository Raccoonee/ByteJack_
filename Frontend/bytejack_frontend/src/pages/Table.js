import "./Table.css";
import ChipsSection from "../components/ChipsSection.js";
import Actions from "../components/Actions.js";
import React, { useEffect, useState } from "react";
import { socket } from "../utils/socket.js";
import Player from "../components/Player.js";
import Dealer from "../components/Dealer.js";

const Table = ({ userData }) => {
  const [gameState, setGameState] = useState(undefined);

  const handleUpdate = (data) => {
    setGameState(data);
    console.log(data);
  };

  const handleStatus = (data) => {
    console.log(data);
  };

  useEffect(() => {
    socket.emit("join", { lobbyCode: userData.gameID });

    socket.on("update", handleUpdate);
    socket.on("status", handleStatus);

    console.log(gameState);
  }, [gameState]);

  return (
    <>
      <div class="background">
        <div class="parent">
          <div
            class={
              gameState?.playerTurn === "player1" ? "div1 current-turn" : "div1"
            }
          >
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
          <div
            class={
              gameState?.playerTurn === "player2" ? "div2 current-turn" : "div2"
            }
          >
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
              <Dealer
                dealerHand={gameState.dealer.hand}
                gameID={userData.gameID}
              ></Dealer>
            ) : (
              "Empty"
            )}
          </div>
          <div class="div5">
            <ChipsSection socket={socket}></ChipsSection>
          </div>
          <div
            class={
              gameState?.playerTurn === "player3" ? "div6 current-turn" : "div6"
            }
          >
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
          <div
            class={
              gameState?.playerTurn === "player4" ? "div7 current-turn" : "div7"
            }
          >
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
          <div
            class={
              gameState?.playerTurn === "player5" ? "div8 current-turn" : "div8"
            }
          >
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
