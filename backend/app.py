# https://flask-socketio.readthedocs.io/en/latest/index.html


from flask import Flask, session, request
from flask_socketio import join_room, leave_room, SocketIO, emit
import random
from game2 import Game
from string import ascii_uppercase
from player import Player
try:
    import db
except:
    pass

"""
TODO: implement what happens when people leave the game
TODO: streamline logic for 
"""

try:
    database = db.DB()
except:
    pass
app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET!"
socketio = SocketIO(app)

rooms = {} #gameID:BlackJackGame


#what is happening when the game is finally over, we know tthat when the dealer goes, it's finally over.

#i should add a leaving function sort of thing.
#maybe when a player disconnets a new ai player is put there ot finish the game if there are other players
#just an interesting thought
#remember you can remove a player using the remove player funciton.

"""
LOGIC:
on connect you just have a player made that connects them to a game/table

then we will get bids and update stuff as things go on. notify all players. 
when we have received a bid from each player, then the actual game starts with the two people dealer thing.
return the new game state plus whose turn it is.

then we have another endpoint event thing that hits or stands for all players. check logic for busted.
"""
def join_game():
    code = session["room"]
    player = session["player"]
    rooms[code].add_player(player)

def leave_game():
    code = session["room"]
    player = session["player"]
    rooms[code].remove_player(player)

def generate_code():
    while True:
        code = ""
        for _ in range(4):
            code += random.choice(ascii_uppercase)
        if code not in rooms:
            break
    return code

def make_game():
    code = generate_code()
    rooms[code] = Game(code, database)
    lobby_message()
    return code

def get_code():
    for code in rooms.keys():
        if not rooms[code].is_full() and not rooms[code].in_progress():
            return code
    return make_game()
        
def get_name():
    name = ""
    for _ in range(10):
        name += random.choice(ascii_uppercase)
    return name

@app.route("/register/<username>/<password>")
def make_player(username, password):
    database.insert_player(username, password)
    return "successfully inserted"

@app.route("/login/<username>/<password>")
def login(username, password):
    player = database.get_player(username, password)
    if player is None:
        return "account doesn't exist"
    else:
        session["player"] = Player(player[0]["playerID"], player[0]["username"])
        join_lobby()
        return "connected!"


# @socketio.on("login")
# def connect(data):
#     player = database.get_player(data["username"], data["password"])
#     if player is None:
#         emit("failed login", data, include_self=True)
#     else:
#         emit("connected", data, include_self=True)
#         session["player"] = Player(player[0]["playerID"], player[0]["username"])
#         join_lobby()

def join_lobby():
    lobby = "AAAA"
    join_room(lobby)
    session["room"] = lobby
    lobby_message()

def lobby_message():
    information = {"games":[]}
    for key in rooms.keys():
        information["games"].append(rooms[key])
    emit("lobby", information, to="AAAA")

# def join_game(data):
#     code = 1
#     name = player["username"]
#     # id = request.sid
#     session["room"] = data["code"]
#     join_game())
#     join_room(code)

def change_room(room):
    leave_room(session["room"])
    session["room"] = room
    join_room(room)
    rooms[room].add_player(session["player"])



@socketio.on("join")
def join(data):
    code = data["gameID"]
    if code == "new":
        code = make_game()
    join_room(code)
    change_room(code)
    message = rooms[code].get_game_state()
    emit("join", message, to=code)

@socketio.on("disconnect")
def disconnect():
    code = session["room"]
    leave_game()
    leave_room(code)
    emit("disconnect", to=code)

@socketio.on("bet")
def bet(data):
    code = session["room"]
    rooms[code].bet(session["player"], data["bet"]) #should send 
    message = rooms[code].get_game_state()
    message["rooms"] = list(rooms.keys())
    emit("update", message, to=code)


    ##move this to the backend
    if rooms[code].all_bets_placed():
        rooms[code].deal()
        message2 = rooms[code].get_game_state()
        message["rooms"] = list(rooms.keys())
        emit("update", message2, to=code)


@socketio.on("hit")
def hit():
    code = session["room"]
    rooms[code].hit(session["player"])
    message = rooms[code].get_game_state()
    message["rooms"] = list(rooms.keys())
    emit("update", message, to=code)

@socketio.on("double")
def double():
    code = session["room"]
    rooms[code].double(session["player"])
    message = rooms[code].get_game_state()
    message["rooms"] = list(rooms.keys())
    emit("update", message, to=code)

@socketio.on("stand")
def stand():
    code = session["room"]
    rooms[code].stand(session["player"])
    message = rooms[code].get_game_state()
    message["rooms"] = list(rooms.keys())
    emit("update", message, to=code)

# #TODO: game already generates its own id that we can ask for...
# @socketio.on("connect") #use a queue to do stuff
# def connect(data): #idk about the authenticating thing
#     testData = {
#   "gameID": 12345,
#   "playerTurn": "player1",
#   "Dealer": { "hand": ["K♠", "2♣", "3♦"] },
#   "winners": ["player1", "player2"],
#   "Players": {
#     "player1": {
#       "name": "Jeremiah",
#       "chips": 100,
#       "hand": ["A♥", "A♦", "A♠", "2♣"],
#       "bet": 10,
#     },
#     "player2": { "name": "Dexter", "chips": 100, "hand": ["K♠", "10♥"], "bet": 10 },
#     "player3": { "name": "Devin", "chips": 100, "hand": ["K♠", "8♥"], "bet": 10 },
#     "player4": { "name": "Ethan", "chips": 100, "hand": ["Q♠", "9♥"], "bet": 10 },
#     "player5": { "name": "Rajeera", "chips": 100, "hand": ["K♠", "A♥"], "bet": 10 },
#   }
# }
#     emit("fooEvent", testData) 
 


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=8080, debug=True, allow_unsafe_werkzeug=True)