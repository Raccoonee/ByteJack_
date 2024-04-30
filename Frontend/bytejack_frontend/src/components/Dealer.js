import DealerHand from "./DealerHand"

const Dealer = ({dealerHand}) => {

    const cardCount = (cards = []) => {
        let total = 0;
        let value;
        let aceCounter = 0;

        for(let i = 0; i < cards.length; i++)
        {            
            if(cards[i].substring(0, 1) === "J" || cards[i].substring(0, 1) === "Q" || cards[i].substring(0, 1) === "K")
            {
                value = 10;
            }
            else if(cards[i].substring(0, 1) === "A")
            {
                value = 11;
                aceCounter++;
            }
            else
            {
                value = parseInt(cards[i]);
            }
            
            total += value;
        }

        for(let i = 0; i < aceCounter; i++)
        {
            if(total > 21)
            {
                total -= 10;
            }
        }

        return total
    }

    return (
        <>
            <div id="money">
                <span id="cash">Dealer</span>
                <div id="bank">Card Count: {cardCount(dealerHand)}<span></span></div>
                <DealerHand cards={dealerHand}></DealerHand>
            </div>
        </>
    )
}

export default Dealer