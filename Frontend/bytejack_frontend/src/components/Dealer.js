import DealerHand from "./DealerHand";
import { cardCount } from "../utils/utils";

const Dealer = ({ dealerHand, gameID }) => {
  return (
    <>
      <div className="padding">
        <div id="gameID">
          Game: {gameID}
          <span></span>
        </div>
        <div id="dealer">
          Dealer
          <span></span>
        </div>
        <div id="count">
          Card Count: {cardCount(dealerHand)}
          <span></span>
        </div>
        <DealerHand cards={dealerHand}></DealerHand>
      </div>
    </>
  );
};

export default Dealer;
