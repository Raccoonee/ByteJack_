from deck import Deck
from player import Player


class Game():
    def __init__(self, roomCode, database):
        self.database = database
        self.roomCode = roomCode
        self.betList = []
        self.winnerList = []
        self.naturalList = []
        self.bustList = []
        self.pushList =[]
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
        self.isGameOver = False

    def is_not_full(self):
        if len(self.players) < 5:
            return True
        return False

    def get_phase(self):
        return self.isBetPhase

    def start_game(self):
        """
        deals out cards to all players including dealer
        checks to see if the player has a natural
        """
        self.isBetPhase = False
        self.dealer.add_card(self.deck.get_card())
        for i in range(2):
            for player in self.players:
                player.add_card(self.deck.get_card())
                if i == 1 and player.hand_total() == 21:
                    for k,v in self.playerOrder.items():
                        if v == player:
                            self.naturalList.append()
    
    def restart_game(self):
        """
        resets most game information
        """
        self.betList = []
        self.winnerList = []
        self.naturalList = []
        self.bustList = []
        self.pushList = []
        self.currentTurn = 1
        self.dealer = Player("dealer", 0, 0)
        self.deck = Deck()
        self.deck.shuffle()
        self.isBetPhase = True
        self.isGameOver = False
        for player in self.players:
            player.set_bet(0)
            player.clear_hand()
        return "game is restarted"

    def get_game_state(self):
        """
        populates dict containing information about gamestate and returns it
        """
        data = {}
        data["players"] = self.get_players()
        data["winners"] = self.get_winners()
        data["dealer"] = self.get_dealer()
        data["naturals"] = self.get_naturals()
        data["gameID"] = self.roomCode
        data["playerTurn"] = "player" + str(self.currentTurn)
        data["gameFinished"] = self.isGameOver
        return data

    def get_dealer(self):
        """
        returns dealer information
        """
        data = {}
        data["hand"] = self.dealer.get_hand()
        return data

    def dealer_play(self):
        """
        function called after players stand
        follows simple logic for the dealer to use
        """
        while self.dealer.hand_total() <= 17:
            print(self.dealer.hand_total())
            self.dealer.add_card(self.deck.get_card())

    def get_winners(self):
        """
        returns a list of winners to be returned in game state
        """
        print(self.winnerList)
        data = []
        for i in range(1, 6):
            key = "player" + str(i)
            if self.playerOrder[key] in self.winnerList:
                data.append(key)
        return data
    
    def get_naturals(self):
        """
        returns a list of players who have naturals to be returned in game state
        """
        data = []
        for i in range(1, 6):
            key = "player" + str(i)
            if self.playerOrder[key] in self.naturalList:
                data.append(key)
        return data

    def get_empty_player(self):
        """
        data formatting for when player does not exist to be returned in get_players
        """
        return {"name": "", "chips": 0, "hand": [], "bet": 0}

    def get_existing_player(self, player):
        """
        data formatting for an existing player to be returned in get_players
        """
        data = {}
        data["name"] = player.get_name()
        data["chips"] = player.get_chips()
        data["hand"] = player.get_hand()
        data["bet"] = player.get_bet()
        #ethan
        if self.isGameOver == True:
            if player in self.winnerList:
                data["state"] = "win"
            elif player in self.bustList:
                data["state"] = "bust"
            elif player in self.pushList:
                data["state"] = "push"
            else:
                data["state"] = "lose"
        else:
            data["state"] = ""
        return data

    def get_players(self):
        """
        data formatting for the player list to be returned in game state
        """
        winners = self.get_winners()
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
        """
        game logic for standing
        will not run if the game is in bet phase or if it not the correct players turn
        will check to see if the current standing player is the last player in the game
        and if they are, then the function will call finish_game
        """
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
            return "game is over"
        if self.next() == "done":
            return "game is over"

    def did_bust(self, player) -> bool:
        """
        logic to see if the player busted
        """
        if player.hand_total() > 21:
            return True
        return False

    def player_hit(self, player):
        """
        game logic for player hitting
        if the player busted, then they will stand automatically
        """
        if self.isBetPhase:
            return
        self.next()
        current = self.playerOrder["player"+str(self.currentTurn)]
        if current != player:
            return
        player.add_card(self.deck.get_card())
        if self.did_bust(player): #forces a stand is a player busts
            self.player_stand(player)

    def try_add_player(self, player):
        """
        attempts to add in a player
        if the game is already full, it will fail
        if the game is past bet phase, it will fail
        """
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
        """
        will remove player from the game
        """
        for i in range(1, 6):
            key = "player" + str(i)
            if self.playerOrder[key] == player:
                self.playerOrder[key] = None
        self.players.remove(player)

    def get_bet(self, player, amount):
        """
        gets a bet using the runtime data stored in player object
        stores bet and subtracts bet from player total money
        """
        if self.isBetPhase == False:
            return
        player.set_bet(amount)
        player.subtract_chips(amount)
        self.betList.append(player)
        if self.all_bets_in():
            self.start_game()
            return "game started"

    def all_bets_in(self):
        """
        checks to see if all bets are placed
        """
        for player in self.players:
            if player not in self.betList:
                return False
        return True

    def next(self):
        """
        attempts to reach the next player
        this facilitates playing when there is a player on seat 5 and seat 1 and none inbetween
        """
        cont = True
        while cont:
            current = self.playerOrder["player"+str(self.currentTurn)]
            if current != None:
                return
            self.currentTurn += 1
            if self.currentTurn == 6:
                self.finish_game()
                return "done"

    def finish_game(self):
        """
        game logic for finishing game
        checks to see results for each player and assigns money based on it
        """
        self.dealer_play()
        for player in self.players:
            total = player.hand_total()
            if total > 21: #checks if player busted
                self.bustList.append(player)
                continue
            if self.dealer.hand_total() > 21: #automatically wins if dealer busted
                self.winnerList.append(player)
            elif total == self.dealer.hand_total(): #adds to push list if dealer and player tie
                self.pushList.append(player)
            elif total > self.dealer.hand_total(): #wins if player has more than dealer
                self.winnerList.append(player)

        for player in self.winnerList:
            player.add_chips(player.get_bet()*2)
        for player in self.pushList:
            player.add_chips(player.get_bet())
        self.isGameOver = True
        print("game finished!")
