from flask import Flask, render_template, session
from flask_socketio import join_room, leave_room, SocketIO, emit
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config["SECRET_KEY"] = "CHANGE THIS LATER"
socketio = SocketIO(app)

games = [] #gameID:BlackJackGame

class BlackJackGame:
    """
    Blackjack game class
    """
    def __init__(self):
        self.players = []
        self.code = self.generate_code()
        pass
    def add_player(self):
        pass
    def remove_player(self):
        pass
    def isFull(self):
        return False
    def get_code(self):
        return self.code
    def generate_code(self):
        while True:
            code = ""
            for _ in range(4):
                code += random.choice(ascii_uppercase)
            if code not in games:
                break
            return code
    
def create_game():
    """
    create_game() 
    creates a new blackjack game and adds it to a list of running games
    """
    newGame = BlackJackGame()
    games.append(newGame)
    return newGame

def join_fill_room():
    """
    join_fill_room()
    filler function that adds player to room that is not full
    """
    for game in games:
        if not game.isFull():
            session["room"] = game
            join_room(session["room"].get_code())
            game.add_player()
            return
    newGame = create_game()
    session["room"] = newGame
    join_room(session["room"].get_code())
    newGame.add_player()

def join_bj_room(roomCode):
    """
    join_bj_room()
    adds player to a room given a roomCode
    """
    #TODO: write this function which will join a room given a code
    
    pass

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
    session.clear()
    return render_template("index.html")

@socketio.on("connect")
def connect(auth):
    join_fill_room()

@socketio.on("disconnect")
def disconnect():
    leave_bj_room()

"""
CODE HERREEEEE
"""
@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    data = {
        "example":222,
        "pfffs":123
    }
    room = session.get("room")
    emit("message", data, to=room, include_self=True) 


if __name__ == "__main__":
    socketio.run(app)