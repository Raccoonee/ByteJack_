import Card from "./Card";
import { numChecker, suitChecker } from "../utils/utils";

const Hand = ({ cards }) => {
  return (
    <>
      <div class="playingCards simpleCards ">
        <ul class="hand">
          {cards.map((item) => (
            <li>
              <Card
                card={"card"}
                rank={numChecker(item)}
                suit={suitChecker(item.substring(item.length - 1))}
              ></Card>
            </li>
          ))}
        </ul>
      </div>
    </>
  );
};

export default Hand;
