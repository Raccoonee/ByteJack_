#card codes from: https://symbl.cc/en/unicode/blocks/playing-cards/
import random

class Card:

    def __init__(self, face):
        self.card = face

        #handle the logic that assigns the card a value based on unicode strigns
        det = face[-1]

        if det.isdigit():
            self.val = int(det)
        elif det in ["A", "B", "D", "E"]:
            self.val = 10

    def getCard(self):
        return self.card
    
    def getVal(self):
        return self.val



class Deck:
    
    def __init__(self):
        #card unicodes are U + string
        self.deck = ["1FOA1", "1FOA2", "1FOA3", "1FOA4", "1FOA5", "1FOA6", "1FOA7", "1FOA8", "1FOA9", "1FOAA",
                     "1FOAB", "1FOAD", "1FOAE", "1FOB1", "1FOB2", "1FOB3", "1FOB4", "1FOB5", "1FOB6", "1FOB7",
                     "1FOB8", "1FOB9", "1FOBA", "1FOBB", "1FOBD", "1FOBE", "1FOC1", "1FOC2", "1FOC3", "1FOC4",
                     "1FOC5", "1FOC6", "1FOC7", "1FOC8", "1FOC9", "1FOCA", "1FOCB", "1FOCD", "1FOCE", "1FOD1",
                     "1FOD2", "1FOD3", "1FOD4", "1FOD5", "1FOD6", "1FOD7", "1FOD8", "1FOD9", "1FODA", "1FODB",
                     "1FODD", "1FODE"]

        for i in range(len(self.deck)):
            self.deck[i] = Card(self.deck[i])
        # i think we should load a deck everytime we need to


    def shuffle(self):
        random.shuffle(self.deck)

    def pop(self):
        if len(self.deck) >= 1:
            return self.deck.pop()
        
    def addDeck(self, i):
        self.deck = self.deck*(i+1)




# used to generate the above list of all cards.
'''
cards = []

for beg in ["1FOA", "1FOB", "1FOC", "1FOD"]:
    for end in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "D", "E"]:
        cards.append(beg+end)

print(cards)
'''

cr = [1, 2, 34, 5]

v = cr.pop()

ri = "jkhyi"

print(ri[-1])