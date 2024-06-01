from flask import Flask, session, request
from flask_socketio import join_room, leave_room, SocketIO, emit
import random
from game import Game
from string import ascii_uppercase
from player import Player
import time as t
from db import DB

"""
initial setup
"""
app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET!"
socketio = SocketIO(app)

playersDict = {}
lobbies = {} #gameID:BlackJackGame
availableGames = []

db = None

def connect_db():
    """
    connect_db initializes the connection between the backend and the database
    this function is called whenever the database is needed and there is no prior connection established
    """
    global db
    while True:
        try:
            db = DB()
            print("CONNECTED")
            break
        except:
            pass

def generate_code():
    """
    generate_code generates a 4 digit code made of uppercase english letters
    this function is called during make game
    """
    while True:
        code = ""
        for _ in range(4):
            code += random.choice(ascii_uppercase)
        if code not in lobbies.keys():
            break
    return code

def make_game():
    """
    make_game creates a new game and returns the code for that game
    this function is called in the make lobby socket route
    """
    if db == None:
        connect_db()
    code = generate_code()
    lobbies[code] = Game(code, db)
    availableGames.append(code)
    send_lobbies()
    return code

def send_update():
    """
    send_update reads session data and then sends the game information to everyone in it
    """
    lobbyCode = session["lobby"]
    message = lobbies[lobbyCode].get_game_state()
    emit("update", message, to=lobbyCode)

def send_lobbies():
    """
    send_lobbies sends a list of all lobbies to people who are on the lobby waiting page
    """
    lobbyList = []
    for lobby in lobbies.keys():
        lobbyList.append(lobby) #mayb delete bcoz we added availabel games
    emit("lobbies", {"lobbies":availableGames}, to="AAAA", include_self=True)

@socketio.on("makeLobby")
def make_lobby():
    """
    make_lobby creates a new game
    """
    make_game()
    emit("status", {"message": "created lobby"}, include_self=True)

@socketio.on("joinLobbyRoom")
def join_lobby_room():
    """
    join_lobby_room puts the player into the lobby room and leaves a room if they are already in one
    """
    print("PLAYER JOINED LOBBY ROOM")
    current_room = session.get("lobby")
    if current_room != None:
        leave_room(current_room)
    join_room("AAAA")
    session["lobby"] = "AAAA"
    response = {"message": "joined lobby room"}
    emit("status", response, include_self=True)

@socketio.on("lobbies")
def lobbiesMessage():
    """
    lobbiesMessage sends out a message to everyone in the lobby room containing a list of all lobbies
    it also checks to make sure the user is in the lobby, and if not, puts the user in the lobby
    """
    currentRoom = session.get("lobby")
    if currentRoom != "AAAA":
        leave_room(currentRoom)
    join_room("AAAA")
    send_lobbies()

@socketio.on("refreshLobbies")
def refreshLobbies():
    """
    refreshLobbies is a basic function which sends out a list of all lobbies
    """
    send_lobbies()
    emit("status", {"message":"sent lobby data"}, include_self=True)
    
@socketio.on("register")
def make_player(data):
    """
    make_player is called whenever a user wants to register a new account
    it calls the database and inserts a new player into the player relation
    """
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
    """
    login checks the database to see if the account exists
    if the account exists, then it creates the player object and assigns it to the session data
    otherwise it sends a failed message
    """
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
        session["playerID"] = playerInformation[0]
        playersDict[playerInformation[0]] = Player(playerInformation[1], playerInformation[0], playerInformation[3])
        response = {"message" : "logged in"}
        emit("status", response, include_self=True)


@socketio.on("join")
def connect(data):
    """
    connect handles the join functionality when entering a room
    updates the session data and attempts to enter a room
    if the room is full, then the room is removed from the list of available games
    """
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
    """
    leaveGame handles the player leaving functionality
    it updates the session information
    """
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
    """
    disconnect handles the player disconnect by leaving any room and game 
    the player might be in and also updates the player information in the database
    """
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
    """
    bet handles the be functionality
    it calls the get_bet function in the game class and checks if the game
    is in the next phase, if it is, then it removes the game from the available game list
    """
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
    """
    hit handles the hit functionality by calling the hit function in the game class
    """
    lobbyCode = session["lobby"]
    player = playersDict[session["playerID"]]
    lobbies[lobbyCode].player_hit(player)
    send_update()

@socketio.on("stand")
def stand():
    """
    stand handles the player stand functionality
    it has an open if, for future changes if something should happen if the game ends
    """
    lobbyCode = session["lobby"]
    player = playersDict[session["playerID"]]
    result = lobbies[lobbyCode].player_stand(player)
    send_update()
    if result == "game is over":
        pass
        
@socketio.on("startNewGame")
def refreshGame():
    """
    refreshGame creates a new game for players to reenter into
    """
    print("asked for newgame refresh")
    lobbyCode = session["lobby"]
    lobbies[lobbyCode].restart_game()
    if lobbies[lobbyCode].is_not_full():
        availableGames.append(lobbyCode)
    send_update()

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=8080, debug=True, allow_unsafe_werkzeug=True)