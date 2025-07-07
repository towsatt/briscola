import itertools
import random
import math
from card import Card

class CPU:
    def __init__(self, hand: list, briscola: Card):
        self.hand: list[Card] = hand
        self.briscola: Card = briscola
        self.points = 0
        values = list(range(1, 11))
        suits = ['bastoni', 'coppe', 'danari', 'spade']
        self.deck = list(map(lambda i: Card(*i), itertools.product(values, suits)))
        self.used_cards: set[Card] = set()
    
    # def choose(self):
    #     return self.hand.pop(random.randint(0, len(self.hand) - 1))
    
    # def opponent_card(self, opp_card):
    #     return self.choose()

    def l_r(self, val):
        return 1/(1 + math.e**(val))
    
    def choose(self, prev_turn_opp_card):
        if prev_turn_opp_card: self.used_cards.add(prev_turn_opp_card)
        choices: dict[Card : float] = {}
        for h in self.hand: choices[h] = 0
        for c in self.hand:
            po, pr, avg = self.est_points(c)
            est = self.l_r(avg) - (0.25 if c.suit == self.briscola and sum(self.hand, lambda i: i.suit==self.briscola.suit) == 1 else 0) - 0.0024*(c.points()**2)
            # print('est', c, po, pr, avg, est)
            choices[c] += est
        # print(choices)
        choice = max(choices, key=lambda i: choices[i])
        # print('cc', choice)
        self.hand.remove(choice)
        return choice
        
    
    def opponent_card(self, opp_card):
        choice: tuple[Card, int] = (None, -1)
        c, _ = self.best_choice(opp_card)
        self.used_cards.add(c)
        self.used_cards.add(opp_card)
        print(self.hand, c)
        self.hand.remove(c)
        return c

    def best_choice(self, opp_card):
        choice: tuple[Card, int] = (None, -math.inf)
        for c in self.hand:
            po, pr = self.est_points(opp_card, c)
            est = - po - (0.1 if c.suit == self.briscola else 0)
            if est > choice[1]:
                choice = (c, est)
        return choice
        
    def draw(self, card):
        self.hand.append(card)
        
    def win(self, Card1: Card, Card2: Card):
        self.points += Card1.points()
        self.points += Card2.points()
        
    def est_points(self, card: Card, CardPlayed: Card = None) -> tuple[int, float]: # coppia punti, probabilita
        if CardPlayed:
            return (card.points() + CardPlayed.points(), 1.0) if card.winning_round(CardPlayed, 1, self.briscola) else (-(card.points() + CardPlayed.points()), 1.0)
        l = 0
        wins = 0
        avg = 0.0
        for c in set(self.deck) - (self.used_cards | set(self.hand)):
            wins += card.winning_round(c, 1, self.briscola)
            l += 1
            avg += (card.points() + c.points()) * (1 if card.winning_round(c, 1, self.briscola) else -1)
        # print("wins", card, wins/l)
        return (card.points(), wins/l, avg/l)