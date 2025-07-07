import itertools
import random
from cpu import CPU
from card import Card

class Player:
    def __init__(self, hand: list, briscola: Card):
        self.hand = hand
        self.briscola = briscola
        self.points = 0
        
    def choose_card(self):
        print(self.hand)
        i = 0
        while i < 1 or i > len(self.hand):
            i = int(input())
        return self.hand.pop(i - 1)

    def get_choosen_card(self, c):
        print("opponent chose {}".format(str(c)))
        return self.choose_card()
        
    def draw(self, card):
        self.hand.append(card)
        
    def win(self, Card1: Card, Card2: Card):
        self.points += Card1.points()
        self.points += Card2.points()

class Virtual_env:
    def __init__(self):
        values = list(range(1, 11))
        suits = ['bastoni', 'coppe', 'danari', 'spade']
        self.deck = list(map(lambda i: Card(*i), itertools.product(values, suits)))
        random.shuffle(self.deck)
        self._used_cards = []
        
    def draw(self):
        return self.deck.pop(0)
    
    def start(self):
        # self.turn = random.randint(0, 1)
        self.turn = 1
        p1_hand = []
        p2_hand = []
        for _ in range(3):
            p1_hand += [self.draw()]
            p2_hand += [self.draw()]
        self.briscola = self.deck[-1]
        self.used_card = []
        self.p1 = Player(p1_hand, self.briscola)
        self.p2 = CPU(p2_hand, self.briscola)
        self.prev_p1: Card = None
        print("comincia {}".format(["p1", "cpu"][self.turn]))
    
        
    def game_turn(self):
        # p1 = player, p2 = cpu
        print('briscola: ', self.briscola)
        print('carte rimaste nel mazzo: ', len(self.deck))
        c1: Card = None
        c2: Card = None
        if self.turn == 0:
            c1 = self.p1.choose_card()
            c2 = self.p2.opponent_card(c1)
        else:
            c1 = self.p2.choose(self.prev_p1)
            c2 = self.p1.get_choosen_card(c1)
        winner = c1.winning_round(c2, self.turn, self.briscola)
        if winner == 0:
            self.p1.win(c1, c2)
            if len(self.deck):
                self.p1.draw(self.draw())
                self.p2.draw(self.draw())
        else:
            self.p2.win(c1, c2)
            if len(self.deck):
                self.p2.draw(self.draw())
                self.p1.draw(self.draw())
        self.prev_p1 = c1
        print(c1, c2, winner)
        self.turn = winner
        print('punteggio', self.p1.points, self.p2.points)
        print('\n\n')