import mysql.connector
import random

class DB:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='rotmgbestgame', host="db", database="bytejack")
        self.cursor = self.cnx.cursor(buffered=True)
        self.reset()
        self.add_test()

    def insert_player(self, username, password):
        try:
            num = random.randint(10000,99999)
            query = f"insert into player value({num}, '{username}', '{password}', 15000);"
            self.cursor.execute(query)
            return query
        except:
            return "333"

    def get_player(self, username, password):
        query = f"select * from player where username='{username}' and password='{password}';"
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def reset(self):
        self.cursor.execute("drop table if exists player;")
        self.cursor.execute("create table player (playerID Integer, username varchar(20), password varchar(20), money Integer, PRIMARY KEY(playerID));")

    def add_test(self): 
        self.cursor.execute("insert into player value (111, 'user10', 'pass10', 15000);")
