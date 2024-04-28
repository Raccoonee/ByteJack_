import Hand from "./Hand"

const Player = () => {

    return (
        <>
            <div id="money">
                <span id="name">Name: <span></span></span>
                <div id="bet">Bet: $<span></span></div>
                <div id="count">Card Count: <span></span></div>
            </div>
            <Hand></Hand>
        </>
    )
}

export default Player