from deck import Deck
from hand import Hand

import os
import sys

if os.name == 'nt':
    os.system('chcp 65001')
    sys.stdout.reconfigure(encoding='utf-8')


newDeck = Deck()

newHand = Hand()

for i in range(330):
    newHand.add_card(newDeck.get_card())


# newHand2 = Hand()

# newHand2.add_card(newDeck.get_card())
# newHand2.add_card(newDeck.get_card())
# newHand2.add_card(newDeck.get_card())


print(newHand.get_hand())
print(newHand.get_hand_total())

# print(newHand2.get_hand())
# print(newHand2.get_hand_total())

print(newDeck.get_deck())








