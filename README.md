# swiss_tournament

Steps Required to run application:
1. clone repository
2. 






--------------------------
tournament.sql
SQL for database used, it contains a database named "tournament"

Database contains two tables: PLAYERS, MATCHES

Table PLAYERS contains columns:
-PLAYER_ID: unique player ID, primary key of this table.
-NAME: name of player, doesn't have to be unique.
-WINS: number of wins of this player.
-LOSSES: number of losses of this player.
-GAMES_PLAYED: number of games played by this player.

Table MATCHES contains columns:
-MATCH_ID: unique match ID, primary key of this table.
-WINNER: unique player ID of winner of this unique match, it references PLAYER_ID from table PLAYERS.
-LOSER: unique player ID of loser of this unique match, it references PLAYER_ID from table PLAYERS.
-ROUND: round the match took place in.


--------------------------
tournament.py
Python script with functions in order to implement a swiss tournament

Functions included are:
-connect(): 
    This function has no arguments and it connects to the PosgreSQL database named "tournament". Returns database connection.
-deletePlayers(): 
    This function deletes all entries of Players and Matches from the database "tournament". Doesn't return anything.
-countPlayers(): 
    This function returns the number of players currently registered. Returns an int.
-registerPlayer():
    Adds a player to the tournament database.
      
        The database assigns a unique serial id number for the player.
      
        Args:
          name: the player's full name (need not be unique).
-playerStandings():
    Returns a list of the players and their win records, sorted by wins.
    
        The first entry in the list should be the player in first place, or a player
        tied for first place if there is currently a tie.
    
        Returns:
          A list of tuples, each of which contains (id, name, wins, matches):
            id: the player's unique id (assigned by the database)
            name: the player's full name (as registered)
            wins: the number of matches the player has won
            matches: the number of matches the player has played

-reportMatch(winner, loser):
    Records the outcome of a single match between two players.
    
        Args:
          winner:  the id number of the player who won
          loser:  the id number of the player who lost

-swissPairings():
    Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
