from flask import Flask, render_template, session
from flask_socketio import join_room, leave_room, SocketIO, emit
import random
from game import BlackJackGame
from string import ascii_uppercase
import shortuuid
from player import Player

"""
TODO: implement what happens when people leave the game
TODO: streamline logic for 
"""


app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET!"
socketio = SocketIO(app)

games = {} #gameID:BlackJackGame


#what is happening when the game is finally over, we know tthat when the dealer goes, it's finally over.

#i should add a leaving function sort of thing.
#maybe when a player disconnets a new ai player is put there ot finish the game if there are other players
#just an interesting thought
#remember you can remove a player using the remove player funciton.
def leave_bj_room():
    """
    leave_bj_room()
    removes player from the room they are in
    """
    game = session["room"]
    game.remove_player()
    leave_room(game.get_code())

@app.route("/")
def index():
    return("conn!!")


"""
LOGIC:
on connect you just have a player made that connects them to a game/table

then we will get bids and update stuff as things go on. notify all players. 
when we have received a bid from each player, then the actual game starts with the two people dealer thing.
return the new game state plus whose turn it is.

then we have another endpoint event thing that hits or stands for all players. check logic for busted.
"""


#TODO: game already generates its own id that we can ask for...
@socketio.on("connect") #use a queue to do stuff
def connect(data): #idk about the authenticating thing
    #make an id...messed up logic. im pretty sure that the person id should not be
    added = False
    id = shortuuid.uuid() #maybe change this
    player_id = data['player_id']
    while id in games:
        id = shortuuid.uuid()

    #make them a player and try to connect them to existing game
    # for dictkey in dict.keys():  
    #     print(dict[dictkey])
    player = Player(player_id)

    for game in games.values():
        if not game.isFull() and not game.inProgress() and not player_id in game.getPlayers(): #after implementing login, we can assign id to incoming player based on login info
            game.addPlayer(player)
            added = True
            break
    
    #make new game if none available
    if not added:
        newGame = BlackJackGame(id)
        games[id] = newGame
        # session['game'] = newGame
        response_data = {
            "player" : player.getID(),
            "game" : id
        }
        emit("assigned_game", response_data, broadcast = True) #the point is that the players shouls be connected to a game.

#players placing their bets
@socketio.on("place bet")
def placeBet(data):
    #will use sent data to check the game instead of session
    game = games[data['gameID']]
    player = data['player']
    bet = data['bet']

    newState = game.setBet(player, bet)
    # if all bets have been placed then deal cards to players and send back game state and whose turn it is
    if game.allBetsPlaced(): #uh maybe we should do something if this returns false
        newState = game.start()
        emit("game_start", newState) #do we just keep going when someone defines the 
    emit("bet_placed", newState, broadcast=True)

#players take turns and dealer takes turns once everybody has taken a turn
@socketio.on("next turn")
def playerTurn(data):
    action = data['action']
    player = data['player']
    game = games[data['gameID']]
    #based on player and action, perform it and return game state
    newState = game.playerTurn(player, action)
    emit(newState, broadcast = True)


@socketio.on("disconnect") #i think this is 
def disconnect(data):
    leave_bj_room() # maybe replace player with ai player for that round and then take them out when round is done.



if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=8080, debug=True, allow_unsafe_werkzeug=True)