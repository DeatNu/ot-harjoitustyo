import sqlite3


# pylint expanantions:
# -name "db" makes no sense in snake_case format
# -sql query is sensible as a one liner


def init():
    db = sqlite3.connect("pyshare.db")  # pylint: disable=invalid-name
    db.isolation_level = None
    maara = db.execute(
        "SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    if len(maara) == 1:
        db.execute("CREATE TABLE Payments (id INTEGER PRIMARY KEY, user_id integer, own_share REAL, others_share REAL)")  # pylint: disable=line-too-long
    return db


def pay(db, name, own_share, others_share):  # pylint: disable=invalid-name
    user_id = db.execute("SELECT id FROM Users WHERE name = (?)", [
                         name]).fetchone()[0]
    db.execute("INSERT INTO Payments (user_id, own_share, others_share) VALUES (?,?,?)", [
               user_id, own_share, others_share])
    return True


def get_sum(db, name):  # pylint: disable=invalid-name
    user_id = db.execute("SELECT id FROM Users WHERE name = (?)", [
                         name]).fetchone()[0]
    surplus = db.execute("SELECT IFNULL(SUM(others_share),0) FROM Payments WHERE user_id = (?)", [
                         user_id]).fetchone()[0]
    debt = db.execute("SELECT IFNULL(SUM(others_share),0) FROM Payments WHERE user_id <> (?)", [
                      user_id]).fetchone()[0]
    return surplus-debt
