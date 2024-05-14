CREATE DATABASE bytejack;

USE bytejack;

CREATE TABLE player (
    playerID int,
    username varchar(20),
    password varchar(20),
    money int,
    PRIMARY KEY(playerID)
);

CREATE TABLE hand (
    playerID int,
    roundID int,
    total int; -- in order to make this hand and a list, i would need to make another table hand (PK playerID roundID card)
    bet int;
    dealerTotal int;
    won boolean;
);

CREATE TABLE round (
    roundID int;
    gameDate date; -- kinda useless
)

-- save information somewhere outside of docker and then read in each time
-- \copy history from dbsetup/course.data