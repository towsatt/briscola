"use client"

import "../css/Opponent.css";
import { HiddenCardComponent } from "./Card";
import type { Card } from "../../lib/types";
import { useState } from "react";

function Opponent() {
  let [cards, setCards] = useState<Array<Card>>([
    { value: 1, suit: "bastoni" },
    { value: 2, suit: "danari" },
    { value: 9, suit: "coppe" },
  ]);
  return (
    <div style={{display: "flex"}}>
      {cards.map((_) => (
        <HiddenCardComponent />
      ))}
    </div>
  );
}

export default Opponent;
