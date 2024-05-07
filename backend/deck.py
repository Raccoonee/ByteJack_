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
        #self.deck = [num for num in range(52)]
        self.deck = ["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠",
                     "J♠", "Q♠", "K♠", "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦",
                     "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦", "A♣", "2♣", "3♣", "4♣",
                     "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "J♥",
                     "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥",
                     "Q♥", "K♥"]
        self.shuffle()

        for i in range(len(self.deck)):
            self.deck[i] = Card(self.deck[i])
        # i think we should load a deck everytime we need to

    def get_string(self, cardNum): #get string format
        #return self.cardToString[cardNum]
        pass

    def get_suit(self, cardNum): # clubs or spades ::: maybe we won't use this often
        pass

    def get_value(self, cardNum): #gets smth like Queen or 3
        val = cardNum//13
        if val == 1:
            return 11 #unless like the total of the players
        elif val < 10:
            return val
        else:
            return 10

    def shuffle(self):
        random.shuffle(self.deck)

    def pop(self):
        if len(self.deck) >= 1:
            return self.deck.pop()
        else:
            self.addDeck(1)
            self.shuffle()
            return self.deck.pop()
        
    def addDeck(self, i):
        self.deck = self.deck*(i+1)




cr = [1, 2, 34, 5]

v = cr.pop()

ri = "jkhyi"

print(ri[-1])