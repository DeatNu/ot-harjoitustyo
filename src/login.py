import sqlite3



def init():
    #creates a db and a table for users, returns the db
    db = sqlite3.connect("users.db")
    db.isolation_level = None
    db.execute("CREATE TABLE Users (id INTEGER PRIMARY KEY, name TEXT)")
    return db

def add_users(db, name1,name2):
    #adds users to the db
    db.execute("INSERT INTO Users (name) VALUES (?)",[name1])
    db.execute("INSERT INTO Users (name) VALUES (?)",[name2])

