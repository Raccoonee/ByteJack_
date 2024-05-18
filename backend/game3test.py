from game import Game
from player import Player

import os
import sys

if os.name == 'nt':
    os.system('chcp 65001')
    sys.stdout.reconfigure(encoding='utf-8')

newPlayer1 = Player("penis", 111, 111)
newPlayer2 = Player("raccooonee", 2231, 111)
newPlayer3 = Player("kat", 10000, 1000)
newGame = Game("ABCD", 1)

newGame.try_add_player(newPlayer1)
newGame.try_add_player(newPlayer2)
newGame.try_add_player(newPlayer3)


newGame.remove_player(newPlayer2)

print(newGame.get_game_state())

newGame.get_bet(newPlayer1, 100)
newGame.get_bet(newPlayer3, 1000)

print(newGame.get_phase())
print(newGame.get_game_state())

newGame.player_hit(newPlayer1)
newGame.player_hit(newPlayer3)

print(newGame.get_game_state())
print("\n\n")

newGame.player_stand(newPlayer1)
newGame.player_hit(newPlayer3)
newGame.player_hit(newPlayer3)
newGame.player_hit(newPlayer3)

print(newGame.get_game_state())

newGame.player_stand(newPlayer3)

print("\n\n")
print(newGame.get_game_state())