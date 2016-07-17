-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


--create db
CREATE DATABASE tournament;

-- A TABLE THAT HAS THE PLAYERS' INFORMATION
CREATE TABLE PLAYERS
(

PLAYER_ID SERIAL PRIMARY KEY, --primary key

--Players
NAME TEXT, --name of players

--Number of wins
WINS INT,

--Number of losses
LOSSES INT,

--Number of games played
GAMES_PLAYED INT

);

-- A TABLE THAT HAS THE MATCHES' INFORMATION
CREATE TABLE MATCHES
(

MATCH_ID SERIAL PRIMARY KEY, --PRIMARY KEY OF MATCHES

WINNER INT REFERENCES PLAYERS(PLAYER_ID), --WINNER OF MATCH

LOSER INT REFERENCES PLAYERS(PLAYER_ID), --WINNER OF MATCH

ROUND INT --ROUND THAT THE MATCH TOOK PLACE IN

);
