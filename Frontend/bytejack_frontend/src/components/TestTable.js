import './cards.css';
import React from "react";

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
                        <ul class="table">
                            <li>
                                <div class="card rank-10 spades">
                                    <span class="rank">10</span>
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
