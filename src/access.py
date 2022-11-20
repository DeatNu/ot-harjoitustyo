
import sqlite3

def init():
    db = sqlite3.connect("users.db")
    db.isolation_level = None

    maara = db.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    if len(maara) == 1:
        db.execute("CREATE TABLE Payments (id INTEGER PRIMARY KEY, user_id integer, amount INTEGER)")
    return db

def pay(db, name, amount):
    user_id = db.execute("SELECT id FROM Users WHERE name = (?)",[name]).fetchone()[0]
    db.execute("INSERT INTO payments (user_id, amount) VALUES (?,?)",[user_id, amount])
    return True

def get_sum(db, name):
    user_id = db.execute("SELECT id FROM Users WHERE name = (?)",[name]).fetchone()[0]
    half  = db.execute("SELECT IFNULL(SUM(amount)/2,0) FROM payments").fetchone()[0]
    return half
