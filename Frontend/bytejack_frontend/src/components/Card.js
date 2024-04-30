
const Card = ({card, rank, suit}) => {
    
    const SelectSuit = ({suitType}) =>
    {
        if(suitType === "spades")
        {
            return (<span class="suit">&spades;</span>)
        }

        else if(suitType === "clubs")
        {
            return(<span class="suit">&clubs;</span>)
        }

        else if(suitType === "diams")
        {
            return(<span class="suit">&diams;</span>)
        }

        else if(suitType === "hearts")
        {
            return(<span class="suit">&hearts;</span>)
        }
    }
    
    return(
        <div class= {card + " rank-" + rank + " " + suit}>
            <span class="rank">{rank}</span>
            <SelectSuit suitType = {suit}></SelectSuit>
        </div>
    )
    
}

//"card rank-7 spades"
export default Card;