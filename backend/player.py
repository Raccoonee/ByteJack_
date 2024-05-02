from deck import Card

#maybe make an interace for all players and implement the actual player and the dealer

# definfing a player
class Player:
    
    def __init__(self, id): # do we want to use player username as id? maybe we want player id ot be a hashed thign of the actual player nam
        self.player_id = id
        self.chips = 3500  #starst with 3500 coins
        self.hand = []
        self.total = 0 #updated as player gets cards
        self.hasNatural = False #do they have a natural
        self.bust = False
        self.bet = 0

        # i know you said you can do the logic in the front end but i think that we would 
        #   need to have the total back here so we can check for a winner or whatever. 
        #       or do you want to implement taht on your own?


    def addChips(self, more_coins: int):
        self.chips += more_coins #increases the number of coins that th eplayer has

    def removeChips(self, less_coins):
        self.chips -= less_coins # reduces the number of coins the the player has

    def addToHand(self, card: Card):
        self.hand.append(card)
        self.total += card.getVal()

    def getHand(self):
        return self.hand
    
    def getID(self):
        return self.player_id
    
    def getTotal(self):
        return self.total
    
    def natural(self):
        self.hasNatural = True

    def getChips(self):
        return self.chips
    
    #both for busting and for dealer beating player
    def lose(self):
        self.chips -= self.bet
        self.bet = 0

    def win(self):
        self.chips += self.bet
        self.bet = 0

    def push(self):
        self.bet = 0

    def getBet(self):
        return self.bet
    
    def setBet(self, bet):
        self.bet = bet

class Dealer:


    def  __init__(self):
        self.id = "dealer"
        self.hand = []
        self.total = 0

    def addToHand(self, card: Card):
        self.hand.append(card)
        self.total += card.getVal()

    def getHand(self):
        return self.hand
    
    def getTotal(self):
        return self.total
    

x = {
    'car':'orange',
    'fsdd':'ecece'
}


for k,v in x.items():
    print(k,v)
