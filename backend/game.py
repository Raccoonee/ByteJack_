from deck import Deck
from player import Player


class Game():
    def __init__(self, roomCode, database):
        self.database = database
        self.roomCode = roomCode
        self.betList = []
        self.winnerList = []
        self.players = []
        self.playerOrder = {
            "player1": None,
            "player2": None,
            "player3": None,
            "player4": None,
            "player5": None,
        }
        self.currentTurn = 1
        self.dealer = Player("dealer", 0, 0)
        self.deck = Deck()
        self.deck.shuffle()
        self.isBetPhase = True

    def get_phase(self):
        return self.isBetPhase

    def start_game(self):
        self.isBetPhase = False
        self.dealer.add_card(self.deck.get_card())
        for i in range(2):
            for player in self.players:
                player.add_card(self.deck.get_card())

    def get_game_state(self):
        data = {}
        data["players"] = self.get_players()
        data["winners"] = self.get_winners()
        data["dealer"] = self.get_dealer()
        data["gameID"] = self.roomCode
        data["playerTurn"] = "player" + str(self.currentTurn)
        return data

    def get_dealer(self):
        data = {}
        data["hand"] = self.dealer.get_hand()
        return data

    def dealer_play(self):
        while self.dealer.hand_total() <= 17:
            print(self.dealer.hand_total())
            self.dealer.add_card(self.deck.get_card())

    def get_winners(self):
        data = []
        for i in range(1, 6):
            key = "player" + str(i)
            if self.playerOrder[key] in self.winnerList:
                data.append(key)
        return data

    def get_empty_player(self):
        return {"name": "", "chips": 0, "hand": [], "bet": 0}

    def get_existing_player(self, player):
        data = {}
        data["name"] = player.get_name()
        data["chips"] = player.get_chips()
        data["hand"] = player.get_hand()
        data["bet"] = player.get_bet()
        return data

    def get_players(self):
        getPlayers = {}
        for i in range(1, 6):
            key = "player" + str(i)
            if self.playerOrder[key] == None:
                getPlayers[key] = self.get_empty_player()
            else:
                getPlayers[key] = self.get_existing_player(
                    self.playerOrder[key])
        return getPlayers
    
    def player_stand(self, player):
        if self.isBetPhase:
            return
        if self.next() == "done":
            return
        current = self.playerOrder["player"+str(self.currentTurn)]
        if current != player:
            return
        self.currentTurn += 1
        if self.currentTurn == 6:
            self.finish_game()
            return
        self.next()

    def player_hit(self, player):
        if self.isBetPhase:
            return
        self.next()
        current = self.playerOrder["player"+str(self.currentTurn)]
        if current != player:
            return
        player.add_card(self.deck.get_card())

    def try_add_player(self, player):
        if self.isBetPhase == False:
            return "game in progress"
        if player in self.players:
            return "fail"
        for i in range(1, 6):
            key = "player" + str(i)
            if self.playerOrder[key] == None:
                self.playerOrder[key] = player
                self.players.append(player)
                return "success"
        return "full"

    def remove_player(self, player):
        for i in range(1, 6):
            key = "player" + str(i)
            if self.playerOrder[key] == player:
                self.playerOrder[key] = None
        self.players.remove(player)

    def get_bet(self, player, amount):  # TODO: database interaction
        if self.isBetPhase == False:
            return
        player.set_bet(amount)
        self.betList.append(player)
        if self.all_bets_in():
            self.start_game()

    def all_bets_in(self):
        for player in self.players:
            if player not in self.betList:
                return False
        return True

    def next(self):
        cont = True
        while cont:
            current = self.playerOrder["player"+str(self.currentTurn)]
            if current != None:
                return
            self.currentTurn += 1
            if self.currentTurn == 6:
                self.finish_game()
                return "done"

    def finish_game(self):  # TODO: update db
        self.dealer_play()
        for player in self.players:
            total = player.hand_total()
            if total > self.dealer.hand_total() and total < 22:
                self.winnerList.append(player)

        print("game finished!")
