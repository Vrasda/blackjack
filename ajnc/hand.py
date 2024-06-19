from deck import *

deck = Deck()
deck.shuffle()

player = Hand()
dealer = Hand()
#deli karte
for i in range(2):
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())

print(player.cards)
print(dealer.cards)


player.add_card(deck.deal())

print(player.cards)
#racuna vrednost od igraca i dilera
player.calc_hand()
dealer.calc_hand()



