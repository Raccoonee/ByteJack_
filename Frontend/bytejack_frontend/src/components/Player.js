import Hand from "./Hand";
import { cardCount } from "../utils/utils";

const Player = ({ name, bet, hand }) => {
  return (
    <div className="padding">
      <span id="name">
        Name: {name}
        <span></span>
      </span>
      <div id="bet">
        Bet: ${bet}
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
