import sqlite3
from decimal import Decimal

# pylint expanantions:
# -name "db" makes no sense in snake_case format


def init():
    # connects to the db, cteates a table for payments if it doesn't exist yet
    db = sqlite3.connect("pyshare.db")  # pylint: disable=invalid-name
    db.isolation_level = None
    maara = db.execute(
        "SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    if len(maara) == 1:
        db.execute("CREATE TABLE Payments (id INTEGER PRIMARY KEY, user_id integer, " +
                   "own_share REAL, others_share REAL)")
    return db


def pay(db, name, own_share, others_share):  # pylint: disable=invalid-name
    try:
        own_share = round(float(own_share), 2)
        others_share = round(float(others_share), 2)
        if own_share < 0 or others_share < 0:
            raise ValueError
    except ValueError:
        return False
    # adds a paymnet to the db
    user_id = db.execute("SELECT id FROM Users WHERE name = (?)", [
                         name]).fetchone()[0]
    db.execute("INSERT INTO Payments (user_id, own_share, others_share) VALUES (?,?,?)", [
               user_id, own_share, others_share])
    return True


def get_sum(db, name):  # pylint: disable=invalid-name
    # returns the net of all payments
    user_id = db.execute("SELECT id FROM Users WHERE name = (?)", [
                         name]).fetchone()[0]
    surplus = db.execute("SELECT IFNULL(SUM(others_share),0) FROM Payments WHERE user_id = (?)", [
                         user_id]).fetchone()[0]
    debt = db.execute("SELECT IFNULL(SUM(others_share),0) FROM Payments WHERE user_id <> (?)", [
                      user_id]).fetchone()[0]
    amount = surplus-debt
    if amount > 100_000_000:
        amount = f"{Decimal(amount):.2E}"
    return amount


def get_transactions(db):  # pylint: disable=invalid-name
    data = db.execute(
        "SELECT U.name, P.own_share, P.others_share FROM Users U LEFT JOIN Payments P ON " +
        "U.id=P.user_id WHERE P.own_share IS NOT NULL AND P.others_share IS NOT NULL").fetchall()
    return data


def convert_names(user, names):
    if user != names[0]:
        names[0], names[1] = names[1], names[0]

    if names[0][-1] == "s" or names[0][-1] == "S":
        name1 = names[0]+"'"
    else:
        name1 = names[0]+"'s"

    if names[1][-1] == "s" or names[1][-1] == "S":
        name2 = names[1]+"'"
    else:
        name2 = names[1]+"'s"
    return name1, name2
