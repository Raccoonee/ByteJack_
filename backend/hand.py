class Hand:
    def __init__(self):
        self.cards = [] #contains "5♥"
    
    def get_hand_total(self):
        total = 0
        for card in self.cards:
            match card[:-1]:
                case "A":
                    total += 11
                case "J":
                    total += 10
                case "Q":
                    total += 10
                case "K":
                    total += 10
                case "10":
                    total += 10
                case _:
                    total += int(card[0])
                    
        if total > 21:
            ace_count = 0
            for card in self.cards:
                if card[0] == "A":
                    ace_count += 1

            while ace_count > 0:
                if total > 21:
                    total -= 10
                ace_count -= 1
                
                
        return total
    

    def add_card(self, card):
        self.cards.append(card)

    def clear_hand(self):
        self.cards = []

    def get_hand(self):
        return self.cards
    
