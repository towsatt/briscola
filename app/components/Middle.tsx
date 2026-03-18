"use client"

import Deck from "./Deck"
import PlayedCards from "./Played_cards"
import Briscola from "./Briscola"

function Opponent() {
  return (
    <div style={{display: "flex"}}>
        <Deck />
        <Briscola />
        <PlayedCards />
    </div>
  );
}

export default Opponent;
