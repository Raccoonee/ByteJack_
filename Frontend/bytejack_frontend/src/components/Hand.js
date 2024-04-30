import Card from "./Card"
import React from "react";

const numChecker = (num) => {
    if(num.length > 2)
        return(num.substring(0, 2))
    else
        return(num.substring(0, 1))
}

const suitChecker = (suit) => {
    if(suit === "♠")
    {
        return "spades"
    }

    else if(suit === "♥")
    {
        return "hearts"
    }

    else if(suit === "♦")
    {
        return "diams"
    }

    else if(suit === "♣")
    {
        return "clubs"
    }
}

const Hand = ({cards = []}) => {   
    return(
        <ul class="hand">
            {cards.map(item =>(<li><Card card={"card"} rank={numChecker(item)} suit={suitChecker(item.substring(item.length - 1))}></Card></li>))}
        </ul>
    )
}

export default Hand;