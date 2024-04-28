import './cssfiles/cards.css'
import Card from './Card'

const Hand = () => {

    return (
        <>
            <div class="playingCards">
                <ul class="hand">
                    <li> <Card></Card></li>
                    <li> <Card></Card></li>
                </ul>
            </div>
        </>
    )
}

export default Hand