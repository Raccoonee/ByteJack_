import DealerHand from "./DealerHand";
import { cardCount } from "../utils/utils";

const Dealer = ({ dealerHand }) => {
  return (
    <>
      <div className=" padding">
        <span id="deler">Dealer</span>
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
