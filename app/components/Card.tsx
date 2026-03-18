"use client"

import type { Card } from "../../lib/types";
import "../css/Card.css";

interface CardProps {
  card: Card;
}

export function VisibleCardComponent({ card }: CardProps) {
  const imgSrc = `./${card.suit}${card.value}.png`;

  return (
    <img src={imgSrc} alt={`${card.value} of ${card.suit}`} className="card" />
  );
}

export function HiddenCardComponent() {
  const imgSrc = `./retro.jpg`;

  return <img src={imgSrc} className="card" />;
}
