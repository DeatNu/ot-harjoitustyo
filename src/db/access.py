import sqlite3


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
    return surplus-debt


def get_transactions(db):  # pylint: disable=invalid-name
    data = db.execute(
        "SELECT U.name, P.own_share, P.others_share FROM Users U LEFT JOIN Payments P ON " +
        "U.id=P.user_id WHERE P.own_share IS NOT NULL AND P.others_share IS NOT NULL").fetchall()
    return data
