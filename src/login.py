import sqlite3


#db.execute("DROP TABLE Users")
def init():
    db = sqlite3.connect("users.db")
    db.isolation_level = None
    db.execute("CREATE TABLE Users (id INTEGER PRIMARY KEY, name TEXT, total INTEGER)")
    return db

def add_users(db, name1,name2):
    db.execute("INSERT INTO Users (name, total) VALUES (?, 0)",[name1])
    db.execute("INSERT INTO Users (name, total) VALUES (?, 0)",[name2])

#maara = db.execute("SELECT * FROM Users WHERE name=?", ["JJ"]).fetchone()
#print(maara)

