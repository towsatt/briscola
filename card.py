class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        d = {
            1: "Asso",
            2: "Due",
            3: "Tre",
            4: "Quattro",
            5: "Cinque",
            6: "Sei",
            7: "Sette",
            8: "Fante",
            9: "Cavallo",
            10: "Re"
        }
        return "{} di {}".format(d[self.value], self.suit)
    
    def __gt__(self, other):
        return self.eval() > other.eval()
    
    def eval(self):
        return self.value - 1 + 10*['bastoni', 'coppe', 'danari', 'spade'].index(self.suit)
    
    def points(self):
        d = {1: 11, 3: 10, 8: 2, 9: 3, 10: 4}
        return d[self.value] if self.value in d else 0
    
    def val(self):
        d = {
            1: 9,
            2: 0,
            3: 8,
            4: 1,
            5: 2,
            6: 3,
            7: 4,
            8: 5,
            9: 6,
            10: 7
        }
        return d[self.value]
    
    def __repr__(self):
        return self.__str__()
    
    def winning_round(self, p2c, turn, briscola):
        if self.suit == p2c.suit:
            if self.val() > p2c.val():
                return turn
            else:
                return 1 - turn
        else:
            if self.suit == briscola.suit: return turn
            elif p2c.suit == briscola.suit: return 1 - turn
            else: return turn