from deck import Deck
from player import Player


class Game():
    def __init__(self, code):
        self.id = code
        self.players = [] #list of player objects
        self.dealer = Player("dealer", "0") #dealer is a dummy player
        self.deck = Deck() #deck to be used in current game
        self.deck.shuffle()
        self.inProgress = False #informs whether or not to add a player becase game has started
        self.data = {
            "gameID": self.id,
            "playerTurn": "",
            "Dealer": { 
                "hand": [],
                "total": 0
                        }, #dealers dummy hand - "K♠", "2♣", "3♦"
            "naturals": [],
            "winners": [], #dummy winners - "player1", "player2"
            "busts": [],
            "losers": [],
            "push": [],
            "Players": { #dummy data that will be changed later with get game state function
                "player1": {
                "name": "Jeremiah",
                "chips": 100,
                "hand": ["A♥", "A♦", "A♠", "2♣"],
                "bet": 10,
                },
                "player2": { "name": "Dexter", "chips": 100, "hand": ["K♠", "10♥"], "bet": 10 },
                "player3": { "name": "Devin", "chips": 100, "hand": ["K♠", "8♥"], "bet": 10 },
                "player4": { "name": "Ethan", "chips": 100, "hand": ["Q♠", "9♥"], "bet": 10 },
                "player5": { "name": "Matt", "chips": 100, "hand": ["K♠", "A♥"], "bet": 10 },
            }
        }
    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def bet(self, player, amount):
        player.add_bet(amount)

    def in_progress(self):
        return self.inProgress
    
    def hit(self, player):
        player.add_to_hand(self.deck.pop())
        if player.get_total() > 21:
            self.stand(player)

    def stand(self, player):
        i = self.players.index(player) + 1
        if player.get_total() > 21:
            self.data["busts"].append("player" + i)
        if i == 0:
            self.data["playerTurn"] = "dealer"
        else:
            self.data["playerTurn"] = "player" + i-1
    
    #deals 2 cards to each player and starts with the player on the right
    def deal(self):
        self.inProgress = True

        for i in range(2):
            for player in self.players:
                player.add_to_hand(self.deck.pop())
                if i == 1 and player.get_total() ==21:
                    self.data["naturals"].append("player" + str(self.players.index(player) + 1)) # if a player gets a natural blackjack
            self.dealer.add_to_hand(self.deck.pop())
        self.data["playerTurn"] = "player" + str(len(self.players) - 1)

    def is_full(self):
        return len(self.players) > 4
    
    def double(self, player):
        pass #TODO: when the player doubles their bet then they only get one more try

    def all_bets_placed(self):
        for p in self.players:
            if p.get_bet_amount() == 0:
                return False
        return True
    
    def dealer_turn(self): #TODO: implement
        while self.dealer.get_total() < 17:
            self.dealer.add_to_hand(self.deck.pop())
        #once dealer total is above 17, dealer must stand
        self.finish_round()

    #calculates winners and losers and pays when necessary
    def finish_round(self):
        bar = self.dealer.get_total()
        if bar <= 21:
            for i, player in enumerate(self.players):
                if player not in self.data["busts"]:
                    if player in self.data["naturals"]:
                        player.natural()
                    elif player.get_total() == bar:
                        self.data["push"].append("player" + str(i+1))
                        player.push()
                    elif player.get_total() < bar:
                        self.data["losers"].append("player" + str(i+1))
                        player.lose()
                    else:
                        self.data["winners"].append("player" + str(i+1))
                        player.win()
        else:
            for player in self.players:
                if player not in self.data["busts"]:
                    if player in self.data["naturals"]:
                        player.natural()
                    else:
                        self.data["winners"].append("player" + str(i+1))
                        player.win()
        self.inProgress = False


    
    def get_game_state(self):
        self.data["Dealer"]["hand"] = self.dealer.get_hand()
        self.data["Dealer"]["total"] = self.dealer.get_total()
        self.data["Players"] = {}
        for i in range(5):
            id = "player" + str(i+1)
            if i < len(self.players):
                self.data["Players"][id] = {
                    "name" : self.players[i].get_name(),
                    "chips": self.players[i].get_chips() - self.players[i].get_bet_amount(), #displays number of chips as what they have - their bet
                    "hand": self.players[i].get_hand(),
                    "bet": self.players[i].get_bet_amount(),
                    "total": self.players[i].get_total()
                }

            else:
                self.data["Players"][id] = {
                     "name": "Matt", "chips": 100, "hand": ["K♠", "A♥"], "bet": 10 
                } #returns an empty dict if player dosn't exist instead of dummy data
        return self.data