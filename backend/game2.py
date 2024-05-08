from deck import Deck
from player import Player
from queue import Queue


class Game():
    def __init__(self, code):
        self.id = code
        self.playerTurn = Queue(maxsize=5) #we will popo from this so we know whose turn it is
        self.currentPlayer = ""
        self.players = {"player1":None, "player2":None, "player3":None, "player4":None, "player5":None} #list of player objects
        self.dealer = Player("dealer", "0") #dealer is a dummy player
        self.deck = Deck() #deck to be used in current game
        self.deck.shuffle()
        self.isBetPhase = True #informs whether or not to add a player becase game has started
        self.data = { #change this stuff later
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
    def get_current_player(self):
        return self.currentPlayer

    def add_player(self, player):
        self.players["player" + str(len(self.players) + 1)] = player

    def remove_player(self, player):
        self.players.remove(player)
        #self.players[player] = None

    def bet(self, player, amount):
        player.add_bet(amount)

    def in_progress(self): #necessary?
        return self.isBetPhase
    
    def hit(self, player):
        if self.isBetPhase() or player != self.get_current_player():
            return
        player.add_to_hand(self.deck.pop())
        if player.get_total() > 21:
            self.stand(player)

    def stand(self, player):
        i = self.players.index(player) + 1
        if player.get_total() > 21:
            self.data["busts"].append("player" + str(i))
        self.next_turn()
    
    #deals 2 cards to each player and starts with the player on the right
    def deal(self):
        self.isBetPhase = True

        for i in range(2):
            for p in self.players.keys():
                if self.players[p]["name"] != "":
                    self.players[p].add_to_hand(self.deck.pop())
                # if i == 1:
                #     self.playerTurn.put(player)
                #     if player.get_total() == 21:
                #         self.data["naturals"].append("player" + str(self.players.index(player) + 1)) # if a player gets a natural blackjack
            self.dealer.add_to_hand(self.deck.pop())
        self.next_turn()
    
    def has_natural(self):#TODO: for now this adds to the naturals list eg. "player1", but change it later so that we can remove self.data
        for p in self.players.keys():
            if self.players[p].get_total() == 21:
                self.data["naturals"].append(p)

    def setup(self):
        self.deal()
        self.has_natural()
        #TODO: make queue too
        for i in range(5,0,-1):
            self.playerTurn.put("player" + str(i))



    def is_full(self):
        return self.playerTurn.full()
    
    def double(self, player):
        pass #TODO: when the player doubles their bet then they only get one more try

    def all_bets_placed(self):
        for p in self.players.values():
            if p.get_bet_amount() == 0:
                return False
        return True
    
    def dealer_turn(self): #TODO: implement
        while self.dealer.get_total() < 17:
            self.dealer.add_to_hand(self.deck.pop())
        #once dealer total is above 17, dealer must stand
        self.finish_round()

    def next_turn(self):
        if self.playerTurn.empty():
            self.currentPlayer = "dealer"
            self.data["playerTurn"] = "dealer"
        else:
            p = self.playerTurn.get()
            while self.players[p] == None:
                p = self.playerTurn.get()
            self.data["playerTurn"] = p
            self.currentPlayer = p


    #calculates winners and losers and pays when necessary
    def finish_round(self):
        bar = self.dealer.get_total()
        if bar <= 21:
            for id, player in self.players.items():
                if player not in self.data["busts"]:
                    if player in self.data["naturals"]:
                        player.natural()
                    elif player.get_total() == bar:
                        self.data["push"].append(id)
                        player.push()
                    elif player.get_total() < bar:
                        self.data["losers"].append(id)
                        player.lose()
                    else:
                        self.data["winners"].append(id)
                        player.win()
        else:
            for id, player in self.players.items():
                if player not in self.data["busts"]:
                    if player in self.data["naturals"]:
                        player.natural()
                    else:
                        self.data["winners"].append(id)
                        player.win()
        self.isBetPhase = False


    
    def get_game_state(self):
        
        self.data["Dealer"]["hand"] = self.dealer.get_hand()
        self.data["Dealer"]["total"] = self.dealer.get_total()
        self.data["Players"] = {}
        i = 0
        for id, player in self.players.items():
            self.data["Players"][id] = {
                "name" : player.get_name(),
                "chips": player.get_chips() - player.get_bet_amount(), #displays number of chips as what they have - their bet
                "hand": player.get_hand(),
                "bet": player.get_bet_amount(),
                "total": player.get_total()
            }
            i += 1

        while i < 5:
            self.data["Players"]["player" + str(i)] = {
                    "name": "", "chips": 0, "hand": [], "bet": 0
            } #returns an empty dict if player dosn't exist instead of dummy data
            i += 1
        return self.data