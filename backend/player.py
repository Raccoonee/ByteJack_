from hand import Hand

class Player():
    def __init__(self, name, id, chips):
        self.name = name
        self.id = id
        self.hand = Hand()
        self.bet = 0
        self.chips = chips

    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id

    def get_bet(self):
        return self.bet
    
    def set_bet(self, amount):
        if type(amount) == type("example"):
            amount = int(amount)
        self.bet = amount
    
    def get_chips(self):
        return self.chips
    
    def hand_total(self):
        return self.hand.get_hand_total()
        
    def get_hand(self):
        return self.hand.get_hand()
    
    def add_card(self, card):
        self.hand.add_card(card)

    def clear_hand(self):
        self.hand.clear_hand()

    def subtract_chips(self, num):
        newNum = int(num)
        self.chips -= newNum

    def add_chips(self, num):
        newNum = int(num)
        self.chips += newNum #new amoiunt in front of old amount
        print(self.chips)