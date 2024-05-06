from deck import Deck


class Game():
    def __init__(self):
        self.players = [] #list of player objects
        self.dealerHand = [] #list of cards
        self.deck = Deck() #deck to be used in current game
        self.deck.shuffle()
    def add_player(self, player):
        self.players.append(player)
    def remove_player(self, player):
        self.players.remove(player)
    def bet(self, player, amount):
        player.add_bet(amount)
        #we need to check when all bets are placed such that the game starts
    def hit(self, player):
        player.add_to_hand(self.deck.pop())
    def stand(self, player):
        # data = self.get_game_state()
        # turn = data["playerTurn"]
        # if turn[-1] < '5':
        #     data["playerTurn"] = "player" + str(int(turn[-1]) + 1)
        # else:
        #     pass
        pass #TODO: maybe use funtion to manage gamestate from betting phase to hitting phase
    def is_full(self):
        return len(self.players) > 4
    def double(self, player):
        pass #TODO: when the player doubles their bet then they only get one more try
    
    def get_game_state(self):
        data = {
            "gameID": 12345,
            "playerTurn": "player1",
            "Dealer": { "hand": ["K♠", "2♣", "3♦"] },
            "winners": ["player1", "player2"],
            "Players": {
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
        data["Players"] = {}
        for i in range(5):
            id = "player" + str(i+1)
            if i < len(self.players):
                data["Players"][id] = {
                    "name" : self.players[i].get_name(),
                    "chips": self.players[i].get_chips(),
                    "hand": ["A♥", "A♦", "A♠", "2♣"],
                    "bet": 10,
                }

            else:
                data["Players"][id] = {
                     "name": "Matt", "chips": 100, "hand": ["K♠", "A♥"], "bet": 10 
                }
        return data