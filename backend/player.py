class Player():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.hand = [] #contains integers
        self.betAmount = 0
        self.handVal = [] # contains integers
        self.total = 0
        self.chips = 2500
    def clear_bet(self):
        self.betAmount = 0
    def add_bet(self, bet):
        self.betAmount += bet
    def get_bet_amount(self):
        return self.betAmount
    def get_name(self):
        return self.name
    def get_chips(self):
        return self.chips
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
        self.handVal.append(val)

        # if total is over 21, check to see if they have an ace and change it
        if self.total > 21:
            for value in self.handVal:
                if value == 11:
                    self.handVal.remove(11)
                    self.handVal.append(1)
                    self.total -= 10
                    return

            # for i in len(self.handVal):
            #     if self.handVal[i] == 11:
            #         self.handVal[i] = 1
            #         self.total -= 10
        
    def get_total(self):
        return self.total
    
    def win(self):
        self.chips += self.betAmount
        self.betAmount = 0
    def lose(self):
        self.chips -= self.betAmount
        self.betAmount = 0
    def natural(self):
        self.chips += 1.5 * self.betAmount
        self.betAmount = 0
    def push(self):
        self.betAmount = 0

