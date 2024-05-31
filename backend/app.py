from flask import Flask, session, request
from flask_socketio import join_room, leave_room, SocketIO, emit
import random
from game import Game
from string import ascii_uppercase
from player import Player
import time as t
from db import DB


app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET!"
socketio = SocketIO(app)

playersDict = {}
lobbies = {} #gameID:BlackJackGame
availableGames = []

db = None

def connect_db():
    global db
    while True:
        try:
            db = DB()
            print("CONNECTED")
            break
        except:
            pass

def generate_code():
    while True:
        code = ""
        for _ in range(4):
            code += random.choice(ascii_uppercase)
        if code not in lobbies.keys():
            break
    return code

def make_game():
    if db == None:
        connect_db()
    code = generate_code()
    lobbies[code] = Game(code, db)
    availableGames.append(code)
    send_lobbies()
    return code

def send_update():
    lobbyCode = session["lobby"]
    message = lobbies[lobbyCode].get_game_state()
    emit("update", message, to=lobbyCode)

def send_lobbies():
    lobbyList = []
    for lobby in lobbies.keys():
        lobbyList.append(lobby) #mayb delete bcoz we added availabel games
    emit("lobbies", {"lobbies":availableGames}, to="AAAA", include_self=True)

@socketio.on("makeLobby")
def make_lobby():
    make_game()
    emit("status", {"message": "created lobby"}, include_self=True)

@socketio.on("joinLobbyRoom")
def join_lobby_room():
    print("PLAYER JOINED LOBBY ROOM")
    join_room("AAAA")
    session["lobby"] = "AAAA"
    response = {"message": "joined lobby room"}
    emit("status", response, include_self=True)

@socketio.on("lobbies")
def lobbiesMessage():
    currentRoom = session.get("lobby")
    if currentRoom is not None:
        leave_room(currentRoom)
    join_room("AAAA")
    send_lobbies()

@socketio.on("refreshLobbies")
def refreshLobbies():
    send_lobbies()
    emit("status", {"message":"sent lobby data"}, include_self=True)
    
@socketio.on("register")
def make_player(data):
    print("ATTEMPING TO REGISTER")
    if db == None:
        connect_db()
    username = data["username"]
    password = data["password"]
    print(db.insert_player(username, password))
    response = {"message" : "registered"}
    emit("status", response, include_self=True)

@socketio.on("login")
def login(data):
    if db == None:
        connect_db()
    username = data["username"]
    password = data["password"]
    playerInformation = db.get_player(username, password)

    print(playerInformation)
    if playerInformation == None:
        response = {"message" : "failed to log in"}
        emit("status", response, include_self=True)
    else:
        session["playerID"] = playerInformation[0] #TODO: set to right indexing method
        session["player"] = username #do i need this anymore?
        playersDict[playerInformation[0]] = Player(playerInformation[1], playerInformation[0], playerInformation[3])
        response = {"message" : "logged in"}
        emit("status", response, include_self=True)

#This is old code for testing Please delete. Code above is current
# @socketio.on("login")
# def login(data):
#     username = data["username"]
#     password = data["password"]
#     for login in logins:
#         if username not in login:
#             continue
#         person = username
#         playersDict[username] = Player(username, 1, 15000)
#         session["player"] = person
#         response = {"message" : "logged in"}
#         emit("status", response, include_self=True)
#         return
#     response = {"message" : "failed to log in"}
#     emit("status", response, include_self=True)

@socketio.on("join")
def connect(data):
    lobbyCode = data["lobbyCode"]
    player = playersDict[session.get("playerID")]
    result = lobbies[lobbyCode].try_add_player(player)
    if result == "success":
        leave_room(session["lobby"])
        session["lobby"] = lobbyCode
        join_room(lobbyCode)
        send_update()
        data = {"status": lobbyCode}
        emit("status", data = {"status": "success"}, include_self=True) 
    elif result == "full": #let devin know that they need to call join lbby instead
        data = {"status": "failed"}
        emit("status", data = {"status": "fail"}, include_self=True) 
    if lobbies[lobbyCode].is_not_full() == False:
        try:   
            availableGames.remove(lobbyCode)
        except:
            pass

@socketio.on("leaveGame")
def leaveGame():
    lobbyCode = session["lobby"]
    person = session["playerID"]
    playersDict[person].clear_hand()
    lobbies[lobbyCode].remove_player(playersDict[person])
    send_update()
    leave_room(lobbyCode)
    session["lobby"] = "AAAA"
    join_room("AAAA")
    emit("status", {"message": "left game and rejoined lobby"}, include_self=True)


@socketio.on("disconnect")
def disconnect():
    print("DISCONNECTED")
    lobbyCode = session.get("lobby")
    if lobbyCode != None:
        leave_room(lobbyCode)
    player = playersDict[session["playerID"]]
    print(player.get_chips())
    db.update(player)
    if lobbyCode != "AAAA" and lobbyCode != "":
        lobbies[lobbyCode].remove_player(player)
    session["lobby"] = ""

@socketio.on("bet")
def bet(data):
    betAmount = int(data["bet"])
    lobbyCode = session["lobby"]
    player = playersDict[session["playerID"]]
    result = lobbies[lobbyCode].get_bet(player, betAmount)
    if result == "game started":
        try:   
            availableGames.remove(lobbyCode)
        except:
            pass
    send_update()

@socketio.on("hit")
def hit():
    lobbyCode = session["lobby"]
    player = playersDict[session["playerID"]]
    lobbies[lobbyCode].player_hit(player)
    send_update()

@socketio.on("stand")
def stand():
    lobbyCode = session["lobby"]
    player = playersDict[session["playerID"]]
    result = lobbies[lobbyCode].player_stand(player)
    send_update() #win game data
    if result == "game is over":
        pass
        #maybe use

@socketio.on("startNewGame")
def refreshGame():
    print("asked for newgame refresh")
    lobbyCode = session["lobby"]
    lobbies[lobbyCode].restart_game()
    if lobbies[lobbyCode].is_not_full():
        availableGames.append(lobbyCode)
    send_update()

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=8080, debug=True, allow_unsafe_werkzeug=True)