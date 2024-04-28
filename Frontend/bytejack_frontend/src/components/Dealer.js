import DealerHand from "./DealerHand"
const Dealer = () => {

    return (
        <>
            <div id="money">
                <span id="cash">Dealer</span>
                <div id="bank">Card Count: 16<span></span></div>
            </div>
            <DealerHand></DealerHand>
        </>
    )
}

export default Dealer