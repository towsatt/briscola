import {VisibleCardComponent} from "./Card"
import type {Card} from "../../lib/types"

function Briscola(){
    const card: Card = {value: 5, suit: "coppe"}

    return <VisibleCardComponent card={card}/>
}

export default Briscola