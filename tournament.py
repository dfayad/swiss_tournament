#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("DELETE FROM MATCHES;")
    DB.commit()

def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("DELETE FROM MATCHES")
    cursor.execute("DELETE FROM PLAYERS")
    DB.commit()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("SELECT * FROM PLAYERS;")

    #returns list of entries in table "PLAYERS"
    e=cursor.fetchall()
    
    #get the len of e to get number of entries in players table
    return len(e)



def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    cursor = DB.cursor()
    #sql command protected against sql injection
    cursor.execute("INSERT INTO PLAYERS (NAME, WINS, LOSSES, GAMES_PLAYED) VALUES ((%s), 0, 0, 0);",(name,))
    DB.commit()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    DB = connect()
    cursor = DB.cursor()
    cursor.execute("SELECT PLAYER_ID, NAME, WINS, GAMES_PLAYED FROM PLAYERS ORDER BY WINS")
    return (cursor.fetchall())



def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    DB = connect()
    cursor = DB.cursor() #to update both winners and losers
    cursor2 = DB.cursor() #to get games played by winner
    cursor3 = DB.cursor() #to get games played by loser

    winner = str(winner)
    loser = str(loser)

    #UPDATE WINNER
    cursor.execute("UPDATE PLAYERS SET WINS=WINS+1 WHERE PLAYER_ID=(%s)",(winner,))
    cursor.execute("UPDATE PLAYERS SET GAMES_PLAYED=GAMES_PLAYED+1 WHERE PLAYER_ID=(%s)",(winner,))


    #UPDATE LOSER
    cursor.execute("UPDATE PLAYERS SET LOSSES=LOSSES+1 WHERE PLAYER_ID=(%s)",(loser,))
    cursor.execute("UPDATE PLAYERS SET GAMES_PLAYED=GAMES_PLAYED+1 WHERE PLAYER_ID=(%s)",(loser,))

    cursor2.execute("SELECT GAMES_PLAYED FROM PLAYERS WHERE PLAYER_ID=(%s)",(winner,))
    a = cursor2.fetchall()

    cursor3.execute("SELECT GAMES_PLAYED FROM PLAYERS WHERE PLAYER_ID=(%s)",(loser,))
    b = cursor3.fetchall()

    if (a==b):
        num=a[0][0]
    elif(a[0][0]<b[0][0]):#choose greater, one may have skipped a round
        num=b[0][0]
    else:
        num=a[0][0]

    num = str(num)

    
    #ADD TO TABLE OF MATCHES
    cursor.execute(
        "INSERT INTO MATCHES (WINNER, LOSER, ROUND) VALUES ("+winner+", "+loser+", "+num+")")
 
    DB.commit()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
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
    """
    
    #ONLY DO IF READY COLUMN IS "1" FOR ALL ENTRIES



    s = playerStandings()

    #empty array representing the list of match pairings for next round
    pairings = []

    #number of pairings
    n = countPlayers()/2


    k=0 #counter

    #iterate through each of the touples
    while (k<=n):
        #s is ordered by wins
        #player plays next match with next person on the list
        pair = [s[k][0],s[k][1], s[k+1][0],s[k+1][1]]
        pairings.append(pair)
        k=k+2 #add 2 because one pair has alrady been formed

    return pairings






