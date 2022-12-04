import sqlite3

# pylint expanantions:
# -name "db" makes no sense in snake_case format


def init():
    # creates a db and a table for users, returns the db
    db = sqlite3.connect("pyshare.db")  # pylint: disable=invalid-name
    db.isolation_level = None
    db.execute("CREATE TABLE Users (id INTEGER PRIMARY KEY, name TEXT)")
    return db


def add_users(db, name1, name2):  # pylint: disable=invalid-name
    # adds users to the db
    db.execute("INSERT INTO Users (name) VALUES (?)", [name1])
    db.execute("INSERT INTO Users (name) VALUES (?)", [name2])


def fetch_names():
    # returns names from the db
    db = sqlite3.connect("pyshare.db")  # pylint: disable=invalid-name
    db.isolation_level = None
    names = db.execute("SELECT name FROM Users").fetchall()
    names = [name[0] for name in names]
    return names


def validate_name(name):
    names = fetch_names()
    return name in names
