CREATE DATABASE bytejack;

USE bytejack;

CREATE TABLE player (
    playerID Integer,
    username varchar(20),
    password varchar(20),
    money Integer,
    PRIMARY KEY(playerID)
);

CREATE USER 'webapp'@'%' IDENTIFIED BY "rotmgbestgame";
GRANT ALL ON bytejack.* TO 'webapp'@'%';
