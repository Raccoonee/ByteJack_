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
    
    def insert_player(self, credentials): #user, pass
        query = "INSERT into player " + str(self.generate_ID())
        query += ","
        query += credentials[0]
        query += ","
        query += credentials[1]
        + ",15000"
        self.run_insertion(query)

    def insert_hand(self, record): #playerid, roundid, bet, 
        query = "INSERT into hand "
        for 

    def insert_round(self, record):
        query = "INSERT into round"
        
