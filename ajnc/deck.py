import random
from konstante import *

class Deck:
    #pravi se lista self koja je prazna
    def __init__(self):
        self.cards = []
        self.build()
    #u self se dodaju karte
    def build(self):
        for value in RANKS:
            for suit in SUITS:
                self.cards.append((value, suit))
  
    #nasumicno bira karte
    def shuffle(self):
        random.shuffle(self.cards)
        

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop()
            
class Hand(Deck):
    def __init__(self):
        self.cards = []
        self.card_img = []
        self.value = 0 

    def add_card(self, card):
        self.cards.append(card)

    def calc_hand(self):
        #pravi see prazna lista sa i bez ace 
        first_card_index = [a_card[0] for a_card in self.cards]
        non_aces = [c for c in first_card_index if c != 'A']
        aces = [c for c in first_card_index if c == 'A']

        #ako su karte sa listu JQK vrednost je 10
        for card in non_aces:
            if card in 'JQK':
                self.value += 10
            else:
                self.value += int(card)
        #ako je karta ace onda se proverava vrednost
        for card in aces:
            if self.value <= 10:
                self.value += 11
            else:
                self.value += 1


    def display_cards(self):
        for card in self.cards:
            cards = "".join((card[0], card[1]))
            if cards not in self.card_img:
                self.card_img.append(cards)
