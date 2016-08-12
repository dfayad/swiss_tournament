swiss_tournament by Daniel Fayad

What is it?

    This project allows you to create swiss tournaments, keep track of the matches and players.

Required Libraries and Dependencies

    Requires: 
    -Python v2.* to be installed
    -PostgreSQL installed
    
How to Run Project
    
    (0.- First you might need to install Vagrant* and VM)
    1.- To run the project you can download the zip file or clone it.
    2.- expand it / go to the directory it is saved on.
    3.- create the database structure described in tournament.sql in PostgreSQL**
    4.- create your client program with the players and matches you want to add, don't forget to import tournament.py and use he fucntions described below
    5.- run your client program (an example can be seen in tournament_test.py) and have fun

    * Here's a resource explaining how to download and use it: https://www.udacity.com/wiki/ud197/install-vagrant
    
    ** (For example, if you're runnng the program in Vagrant VM:
    get to the directory you have vagrant in, use the "vagrant up" command,
    use the "vagrant ssh" command, go to the directory you cloned this project 
    on, type "psql" to access PosgreSQL, then you can import the  database file
    with the command: "\i tournament.sql" after that, you should have your 
    database set up, and you'll be able to continue.)


Files

    --------------
    tournament.sql
    --------------
    SQL for database used, it contains a database named "tournament"
    
    Database contains two tables: PLAYERS, MATCHES
    
    Table PLAYERS contains columns:
        -PLAYER_ID: unique player ID, primary key of this table.
        -NAME: name of player, doesn't have to be unique.
    
    Table MATCHES contains columns:
        -MATCH_ID: unique match ID, primary key of this table.
        -WINNER: unique player ID of winner of this unique match, it references PLAYER_ID from table PLAYERS.
        -LOSER: unique player ID of loser of this unique match, it references PLAYER_ID from table PLAYERS.

    -------------
    tournament.py
    -------------
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

    ------------------
    tournament_test.py
    ------------------

    This file was used for testing the functionality of the project (both python and sql files).

    You can use this as an example on how to creat your own client program to run your own swiss tournament!

