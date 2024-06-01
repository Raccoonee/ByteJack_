import mysql.connector
import random

class DB:
    def __init__(self):
        """
        sets up database connection
        resets the database for the session
        adds test data
        """
        self.cnx = mysql.connector.connect(user='root', password='rotmgbestgame', host="db", database="bytejack")
        self.cursor = self.cnx.cursor(buffered=True)
        self.reset()
        self.add_test()

    def insert_player(self, username, password):
        """
        attempts to insert a new player into the database
        """
        try:
            num = random.randint(10000,99999)
            query = f"insert into player value({num}, '{username}', '{password}', 15000);"
            self.cursor.execute(query)
            return query
        except:
            return "333"

    def get_player(self, username, password):
        """
        attempts to get a player, if there is no player with matching credentials, does not return tuple
        if there are multiple players with the same login, it will return the first one
        """
        query = f"select * from player where username='{username}' and password='{password}';"
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def reset(self):
        """
        resets the database
        """
        self.cursor.execute("drop table if exists player;")
        self.cursor.execute("create table player (playerID Integer, username varchar(20), password varchar(20), money Integer, PRIMARY KEY(playerID));")

    def add_test(self): 
        """
        inserts an example player
        """
        self.cursor.execute("insert into player value (111, 'user10', 'pass10', 15000);")

    def update(self, player):
        """
        updates the chip value for a given player, called upon disconnect
        """
        newChips = player.get_chips()
        id = player.get_id()
        self.cursor.execute(f"update player set money ={newChips} where playerID={id};")
