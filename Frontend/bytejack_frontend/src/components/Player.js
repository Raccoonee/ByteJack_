import Hand from "./Hand"

const Player = ({name, bet, hand}) => {

    const cardCount = (cards = []) => {
        let total = 0;
        let value;
        let aceCounter = 0;

        for(let i = 0; i < cards.length; i++)
        {
            console.log(cards[i].substring(0,1));
            
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
                <span id="name">Name: {name}<span></span></span>
                <div id="bet">Bet: ${bet}<span></span></div>
                <div id="count">Card Count: {cardCount(hand)}<span></span></div>
            </div>
            <Hand cards={hand}></Hand>
        </>
    )
}

export default Player