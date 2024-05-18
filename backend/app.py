from flask import Flask, session, request
from flask_socketio import join_room, leave_room, SocketIO, emit
import random
from game import Game
from string import ascii_uppercase
from player import Player

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET!"
socketio = SocketIO(app)

logins = [["user1","pass1"], ["user2", "pass2"]]
playersDict = {}
lobbies = {} #gameID:BlackJackGame


def generate_code():
    while True:
        code = ""
        for _ in range(4):
            code += random.choice(ascii_uppercase)
        if code not in lobbies.keys():
            break
    return code

def make_game():
    code = generate_code()
    lobbies[code] = Game(code, 1) #tochange
    return code

def send_update():
    lobbyCode = session["lobby"]
    message = lobbies[lobbyCode].get_game_state()
    emit("update", message, to=lobbyCode)

@app.route("/getLobbies", methods=["GET"])
def get_lobbies():
    lobby = lobbies.keys()
    lobbyList = []
    for lob in lobby:
        lobbyList.append(lob)
    return {"lobbies":lobbyList}#["ABCD", "BCDF"]

@app.route("/makeLobby", methods=["POST"])
def make_lobby():
    make_game()
    return "made lobby"

@app.route("/getUSERS", methods=["get"])
def getUSERS():
    return logins

@app.route("/register/<username>/<password>", methods=["GET", "POST"])
def make_player(username, password):
    logins.append([username, password])
    #database.insert_player(username, password)
    return "successfully inserted"

@app.route("/login/<username>/<password>", methods=["GET"])
def login(username, password):
    for login in logins:
        if username not in login:
            continue
        if password not in login:
            continue
        person = username
        playersDict[username] = Player(username, 1, 15000)
        session["player"] = person
        return "logged in!" + person
    return "account doesn't exist"

@socketio.on("join")
def connect(data):
    lobbyCode = data["lobbyCode"]
    player = playersDict[session.get("player")]
    result = lobbies[lobbyCode].try_add_player(player)
    if result == "success":
        session["lobby"] = lobbyCode
        join_room(lobbyCode)
        send_update()
        data = {"status": lobbyCode}
        emit("status", data = {"status": "success"}, include_self=True) 
    elif result == "full":
        data = {"status": "failed"}
        emit("status", data = {"status": "fail"}, include_self=True) 

# @socketio.on("disconnect")
# def disconnect():
#     lobbyCode = session["lobby"]
#     leave_room(lobbyCode)
#     player = playersDict[session["player"]]
#     lobbies[lobbyCode].remove_player(player)

@socketio.on("bet")
def bet(data):
    betAmount = data["bet"]
    lobbyCode = session["lobby"]
    player = playersDict[session["player"]]
    lobbies[lobbyCode].get_bet(player, betAmount)
    send_update()

@socketio.on("hit")
def hit():
    lobbyCode = session["lobby"]
    player = playersDict[session["player"]]
    lobbies[lobbyCode].player_hit(player)
    send_update()

@socketio.on("stand")
def stand():
    lobbyCode = session["lobby"]
    player = playersDict[session["player"]]
    lobbies[lobbyCode].player_stand(player)
    send_update()

@socketio.on("penis")
def penis():
    lobbyCode = session["lobby"]
    data = lobbies[lobbyCode].get_players()
    emit("penis", data, include_self=True)


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=8080, debug=True, allow_unsafe_werkzeug=True)