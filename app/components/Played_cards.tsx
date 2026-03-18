import { useState } from "react";
import type { Card } from "../../lib/types";
import { VisibleCardComponent } from "./Card";

function PlayedCards() {
  const [card, setCard] = useState<Card>();
  return (
    <div>
      {card && (
        <VisibleCardComponent card={card} />
      )}
    </div>
  );
}

export default PlayedCards;
