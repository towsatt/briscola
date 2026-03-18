export type Suit = 'bastoni' | 'coppe' | 'danari' | 'spade'

export interface Card {
  value: number
  suit: Suit
}