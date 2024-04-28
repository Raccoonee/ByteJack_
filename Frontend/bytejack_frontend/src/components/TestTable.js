import './cssfiles/TestTable.css'
import ChipsSection from './ChipsSection.js'
import Actions from './Actions.js';
import React from "react";
import Dealer from './Dealer.js';
import Player from './Player.js';

const TestTable = () => {
    return (
        <>
            <div class="parent">
                <div class="div1"> <Player></Player> </div>
                <div class="div2"> <Player></Player></div>
                <div class="div3"> <Actions></Actions></div>
                <div class="div4"> <Dealer></Dealer></div>
                <div class="div5"> <ChipsSection></ChipsSection></div>
                <div class="div6"> <Player></Player></div>
                <div class="div7"> <Player></Player></div>
                <div class="div8"> <Player></Player></div>
            </div>
        </>
    );
};

export default TestTable;
