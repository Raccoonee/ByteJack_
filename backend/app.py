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
    if db == None:
        connect_db()
    username = data["username"]
    password = data["password"]
    db.insert_player(username, password)
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
        session["playerID"] = playerInformation #TODO: set to right indexing method
        session["player"] = username #do i need this anymore?
        playersDict[playerInformation] = Player(playerInformation)
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
    player = playersDict[session.get("player")]
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

@socketio.on("leaveGame")
def leaveGame():
    lobbyCode = session["lobby"]
    person = session["player"]
    playersDict[person].clear_hand()
    lobbies[lobbyCode].remove_player(playersDict[person])
    send_update()
    leave_room(lobbyCode)
    session["lobby"] = "AAAA"
    join_room("AAAA")
    emit("status", {"message": "left game and rejoined lobby"}, include_self=True)


@socketio.on("disconnect")
def disconnect():
    lobbyCode = session["lobby"]
    leave_room(lobbyCode)
    player = playersDict[session["player"]]
    db.update(playersDict[session["playerID"]]) #I should porbbaly go with id
    if lobbyCode != "AAAA":
        lobbies[lobbyCode].remove_player(player)

@socketio.on("bet")
def bet(data):
    betAmount = data["bet"]
    lobbyCode = session["lobby"]
    player = playersDict[session["player"]]
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
    player = playersDict[session["player"]]
    lobbies[lobbyCode].player_hit(player)
    send_update()

@socketio.on("stand")
def stand():
    lobbyCode = session["lobby"]
    player = playersDict[session["player"]]
    result = lobbies[lobbyCode].player_stand(player)
    if result == "game is over":
        newGameCode = make_game()
        message = newGameCode
        emit("newGameId", message, to=lobbyCode)
        
    send_update()

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=8080, debug=True, allow_unsafe_werkzeug=True)