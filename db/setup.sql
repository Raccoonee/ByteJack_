CREATE DATABASE bytejack;

USE bytejack;

CREATE TABLE player (
    playerID Integer,
    username varchar(20),
    password varchar(20),
    money Integer,
    PRIMARY KEY(playerID)
);

-- CREATE TABLE hand (
--     playerID Integer,
--     roundID Integer,
--     total Integer, -- in order to make this hand and a list, i would need to make another table hand (PK playerID roundID card)
--     bet Integer,
--     dealerTotal Integer,
-- );

-- CREATE TABLE round (
--     roundID Integer,
--     gameDate date, -- kinda useless
-- );

INSERT INTO player VALUES (1, "kat", "kat", 1000);

CREATE USER 'webapp'@'%' IDENTIFIED BY "rotmgbestgame";
GRANT ALL ON bytejack.* TO 'webapp'@'%';

-- save information somewhere outside of docker and then read in each time
-- \copy history from dbsetup/course.data