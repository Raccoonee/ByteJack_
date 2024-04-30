import './cards.css';
import React from "react";
import Card from "./Card";
import Hand from "./Hand";
import Player from "./Player";
import DealerHand from "./DealerHand"
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
    return (
        <>
            <div style={{
                position: "absolute",
                top: "50%",
                left: "50%",
                transform: "translate(-50%, -50%)",
                height: "100%",
                margin: 0,
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
            }}>
                <div class="playingCards faceImages simpleCards ">
                    <div style={{
                        width: "20vh",
                        display: "inline-block",
                    }}>
                        <Dealer dealerHand={test.Dealer.hand}></Dealer>
                    </div>
                    <div style={{
                        width: "20vh",
                        display: "inline-block",
                    }}>
                        <ul class="table">
                            <li>
                                <div class="card rank-A clubs">
                                    <span class="rank">A</span>
                                    <span class="suit">&clubs;</span>
                                </div>
                            </li>
                            <li>
                                <div class="card rank-k spades">
                                    <span class="rank">K</span>
                                    <span class="suit">&spades;</span>
                                </div>
                            </li>
                        </ul>
                    </div>
                    <div style={{
                        width: "20vh",
                        display: "inline-block",
                    }}>
                        <Player name={test.Players.player1.name} bet={test.Players.player1.bet} hand={test.Players.player1.hand}></Player>
                    </div>
                    <div style={{
                        width: "20vh",
                        display: "inline-block",
                    }}>
                        <ul class="hand">
                            <li>
                                <div class="card rank-A hearts">
                                    <span class="rank">A</span>
                                    <span class="suit">&spades;</span>
                                </div>
                            </li>
                            <li>
                                <div class="card rank-k spades">
                                    <span class="rank">K</span>
                                    <span class="suit">&spades;</span>
                                </div>
                            </li>
                        </ul>
                    </div>
                    <div style={{
                        width: "20vh",
                        display: "inline-block",
                    }}>
                        <ul class="hand">
                            <li>
                                <div class="card rank-A hearts">
                                    <span class="rank">A</span>
                                    <span class="suit">&spades;</span>
                                </div>
                            </li>
                            <li>
                                <div class="card rank-k spades">
                                    <span class="rank">K</span>
                                    <span class="suit">&spades;</span>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div >
        </>
    );
};

export default TestTable;
