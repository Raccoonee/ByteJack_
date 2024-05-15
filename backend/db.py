import mysql.connector
import random

class DB:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='webapp', password='rotmgbestgame', host="db", database="bytejack")
        self.cursor = self.cnx.cursor(buffered=True)

    def generate_ID(self): #can call an sql query so that no numbers match
        id = random.randint(100000000,999999999)
        return id
    
    def run_insertion(self, query):
        self.cursor.execute(query)
        self.cnx.commit()

    def run_select(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def insert_player(self, username, password): #user, pass
        query = "INSERT into player " + str(self.generate_ID())
        query += ","
        query += username
        query += ","
        query += password
        + ",15000;"
        self.run_insertion(query)

    def get_player(self, username, password):
        query = "SELECT * FROM player WHERE username = "
        query += username
        query += " AND password = "
        query += password
        query += ";"
        return self.run_select(query)

    def insert_hand(self, record): #playerid, roundid, bet, 
        query = "INSERT into hand "


    def insert_round(self, record):
        query = "INSERT into round"
        
