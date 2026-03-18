"use client";

import "../css/Player.css";
import { VisibleCardComponent } from "./Card";
import type { Card } from "../../lib/types";
import { useState } from "react";

function Player() {
  let [cards, setCards] = useState<Array<Card>>([
    { value: 1, suit: "bastoni" },
    { value: 2, suit: "danari" },
    { value: 9, suit: "coppe" },
  ]);
  return (
    <div style={{ display: "flex" }}>
      {cards.map((card) => (
        <VisibleCardComponent card={card} />
      ))}
    </div>
  );
}

export default Player;
