import sqlite3
import bcrypt

# pylint expanantions:
# -name "db" makes no sense in snake_case format


def init():
    db = sqlite3.connect("pyshare.db")  # pylint: disable=invalid-name
    db.isolation_level = None
    db.execute(
        "CREATE TABLE Users (id INTEGER PRIMARY KEY, name TEXT, password TEXT, salt TEXT)")
    return db


def add_users(db, users):  # pylint: disable=invalid-name
    # adds users to the db
    name1 = users[0]
    pwd1 = users[1]
    name2 = users[2]
    pwd2 = users[3]
    pwd1, salt1 = hash_pwd(pwd1)
    pwd2, salt2 = hash_pwd(pwd2)
    db.execute("INSERT INTO Users (name, password, salt) VALUES (?,?,?)", [
               name1, pwd1, salt1])
    db.execute("INSERT INTO Users (name, password, salt) VALUES (?,?,?)", [
               name2, pwd2, salt2])


def fetch_names():
    # returns names from the db
    db = sqlite3.connect("pyshare.db")  # pylint: disable=invalid-name
    db.isolation_level = None
    names = db.execute("SELECT name FROM Users").fetchall()
    names = [name[0] for name in names]
    return names


def fetch_pwds():
    # returns passwords from the db
    db = sqlite3.connect("pyshare.db")  # pylint: disable=invalid-name
    db.isolation_level = None
    pwds = db.execute("SELECT password FROM Users").fetchall()
    pwds = [pwd[0] for pwd in pwds]
    return pwds


def fetch_salt(user):
    # returns salt from the db
    db = sqlite3.connect("pyshare.db")  # pylint: disable=invalid-name
    db.isolation_level = None
    try:
        salt = db.execute("SELECT salt FROM Users WHERE name=(?)", [
                          user]).fetchone()[0]
    except TypeError:
        salt = ""
    return salt


def validate_name(name):
    names = fetch_names()
    return name in names


def validate_pwd(name_and_pwd):
    name, pwd = name_and_pwd
    pwds = fetch_pwds()
    salt = fetch_salt(name)
    pwd, _ = hash_pwd(pwd, salt)
    return pwd in pwds


def hash_pwd(password, salt=None):
    password = bytes(password, encoding='utf-8')
    if not salt:
        salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    return hashed, salt
