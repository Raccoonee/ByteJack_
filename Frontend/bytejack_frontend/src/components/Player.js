import Hand from "./Hand";
import { cardCount } from "../utils/utils";

const Player = ({ name, bet, hand, chips, state}) => {
  return (
    <div className="padding">
       <div id="bet">
        {state}
        <span></span>
      </div>
      <span id="name">
        Name: {name}
        <span></span>
      </span>
      <div id="bet">
        Bet: ${bet}
        <span></span>
      </div>
      <div id="bet">
        Chips: ${chips}
        <span></span>
      </div>
      <div id="count">
        Card Count: {cardCount(hand)}
        <span></span>
      </div>
      <Hand cards={hand}></Hand>
    </div>
  );
};

export default Player;
