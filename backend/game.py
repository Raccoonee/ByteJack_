# blackjack game class
import random
from player import Dealer, Player
from deck import Deck, Card


class BlackJackGame:
    """
    Blackjack game class
    """
    def __init__(self, code):
        self.inProgress = False
        self.players = {}
        self.player_info = {} # all players and their information
        self.code = code
        self.dealer = Dealer()
        self.deck = Deck() # the deck to be used
        self.deck.shuffle()

        self.gameState = {
            "gameID": self.code,
            "playerTurn": "", #starts with the right most player
            "dealer": {"hand": []},
            "winners": [],
            "losers": [],
            "naturals": [],
            "players": self.player_info
        }

        """
        player_info looks like this:
        {"gameID": 12345,
        "playerTurn": "player1",
        "Dealer": {"hand": ["K♠", "10♥"]},
        "winners": ["player1", "player2"],
        "Players": {
            "player1": {"name": "Bob", "chips": 100, "hand": ["K♠", "10♥"], "bet": 10},
            "player2": {"name": "Bob", "chips": 100, "hand": ["K♠", "10♥"], "bet": 10},
            "player3": {"name": "Bob", "chips": 100, "hand": ["K♠", "10♥"], "bet": 10},
            "player4": {"name": "Bob", "chips": 100, "hand": ["K♠", "10♥"], "bet": 10},
            "player5": {"name": "Bob", "chips": 100, "hand": ["K♠", "10♥"], "bet": 10}
        }
        """

    #sets the bet for each player to what client specified. --does not check to see if bet is possible
    def setBet(self, player,  bet):
        self.player_info[player]["bet"] = bet
        self.updateState()
        return self.gameState


    #checks to see if all players have placed their bets.
    def allBetsPlaced(self):
        for player in self.player_info.values():
            if player["bet"] == 0:
                return False
            
        #if all players have bets more than 0 (have actually placed their bets)
        return True

    #deals 2 cards to each player including the dealer
    def start(self):
        self.inProgress = True #game has started
        for i in range(2):
            #deal a card to each player + dealer
            for player_num, player in self.players.items():
                self.deal(player, self.deck.pop())

                #checks if players hand is 21
                if player.getTotal() == 21:
                    player.natural()
                    #player.addChips(1.5*their bet)
            self.deal(self.dealer, self.deck.pop())

        self.updateState()
        self.gameState["playerTurn"] = self.players.keys()[-1]

        return self.gameState
            #handle logic for when someone's connection rtimes out

    #handles a player's turn
    #remember to update the state as youo go along.
    def playerTurn(self, player_num, action):  #expects player1, player2 etc.
        player = self.players[player_num]
        if action == "hit":
            self.deal(player, self.deck.pop())
            if player.getTotal() > 21:
                player.bust()
                self.gameState["losers"].append(player)
                #next players turn
            self.updateState()
        elif action == "stand":
            i = self.players.index(player_num)
            if i > 0:
                self.gameState["playerTurn"] = self.players[i-1]
            self.gameState["playerTurn"] = "dealer"
            
        return self.gameState

    def dealerTurn(self):
        while self.dealer.getTotal() < 16:
            self.deal(self.dealer, self.deck.pop())

        dealer_total = self.dealer.getTotal()
        #now the dealer must stand.
        if dealer_total > 21:
            losers = self.gameState["losers"]
            for player_num, player in self.players.items():
                if player_num not in losers:
                    player.addChips(int(self.gameState["players"]["player_num"]["bet"])) #win paid

        #dealer has a blackjack so all players without one lose and those with one push
        elif dealer_total == 21:
            losers = self.gameState["losers"]
            for player_num, player in self.players.items():
                if player_num not in losers:
                    if player.getTotal() != 21:
                        player.removeChips(int(self.gameState["players"]["player_num"]["bet"])) #lose bet
        elif dealer_total < 21:
            for player in self.players.values():
                player_total = player.getTotal()
                if player_total < dealer_total:
                    #they lose chips
                    pass
                elif player_total > dealer_total:
                    #they win chips
                    pass
                else:
                    #push
                    pass
        
        #return the new game state.. which is a game that has ended

        
    def updateState(self):
        for player_num, player in self.players.items():
            self.player_info[player_num]["chips"] = player.getChips()
            self.player_info[player_num]["hand"] = player.getHand()

        self.gameState["dealer"]["hand"] = self.dealer.getHand()
        self.gameState["players"] = self.player_info


    #adds a player to the tabel/game if the game is not already full
    def addPlayer(self, player: Player):
        player_num = "player" + str(len(self.player_info.keys()) + 1)
        self.player_info[player_num] = {"name": player.getID(), "chips": player.getChips(), "hand": [], "bet": 0}
        self.players[player_num] = player
        
    #removes a player form the game
    def removePlayer(self, player): # should take in remove "player1"
        if player in self.player_info:
            self.player_info.pop(player, None)
            self.players.pop(player, None)
        else:
            #maybe throw an error or somehting
            pass

    #returns true if a game has 5 players. no logic for in case game has more than  
    def isFull(self):
        if len(self.players) == 5:
            return True

    #returns the game code
    def getCode(self):
        return self.code
    

    # #fix this man
    # def generate_code(self, games):
    #     while True:
    #         code = ""
    #         for _ in range(4):
    #             code += random.choice(ascii_uppercase)
    #         if code not in games:
    #             break
    #         return code
        
    #deals cards to the specicfied player
    def deal(self, player):
        card = self.deck.pop()
        if type(player) == Dealer or type(player) == Player:
            player.addToHand(card) #change this to only show the face
        else:
            pass #do something, maybe raise an error?

    def getPlayers(self):
        return self.players
    
    def getplayer_info(self):
        return self.player_info
    

    def inProgress(self):
        return self.inProgress
    


"""
p = Player('gas')
q = Player('has')
r = Player('pas')


b = BlackJackGame('dfdfdf')
b.addPlayer(p)
print(b.getplayer_info())

b.addPlayer(q)
print(b.getplayer_info())

b.addPlayer(r)
print(b.getplayer_info())

r.addChips(3000)
b.updateState()

p.addToHand(Card("1FODD"))
b.updateState()

print(b.getplayer_info())
print(r.getChips())
"""

