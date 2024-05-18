#card codes from: https://symbl.cc/en/unicode/blocks/playing-cards/
import random

DECK = ["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠",
        "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦",
        "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣",
        "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥"]

class Deck:
    def __init__(self):
        self.deck = DECK
        self.shuffle()

    def get_deck(self):
        return self.deck

    def get_card(self):
        if len(self.deck) < 1:
            self.deck = DECK
            self.shuffle()
            card = self.deck.pop()
            return card
        else:
            card = self.deck.pop()
            return card

    def shuffle(self):
        random.shuffle(self.deck)

