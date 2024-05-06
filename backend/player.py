class Player():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.hand = [] #contains integers
        self.betAmount = 0
        self.hand2total = []
        self.total = 0
    def clear_bet(self):
        self.betAmount = 0
    def add_bet(self, bet):
        self.betAmount += bet
    def get_bet_amount(self):
        return self.betAmount
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
    def get_hand(self):
        return self.hand
    def clear_hand(self):
        self.hand = []
    def add_to_hand(self, card):
        self.hand.append(card)
        # #adds the value of the card that was just added to hand
        det = card[0]
        if det.isdigit():
            val = int(det)
        elif det == "A":
            val = 11
        else:
            val = 10
        self.total += val

        # if total is over 21, check to see if they have an ace and change it
        if self.total > 21:
            for i in len(self.hand2total):
                if self.hand2total[i] == 11:
                    self.hand2total[i] = 1
                    self.total -= 10
        
    def get_total(self):
        return self.total
