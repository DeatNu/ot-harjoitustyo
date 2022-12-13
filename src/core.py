import sqlite3
from ui import ui_main
from ui import ui_login
from db import login

# pylint expanantions:
# -name "db" makes no sense in snake_case format


def main():
    # opens login wdw for creating users
    login_wdw = ui_login.Login()
    if not login_wdw.first:
        usernames = login.fetch_names()
        login_wdw.usernames = usernames
    # initializes the loop
    login_wdw.mainloop()
    # program won't crash if invalid number of usernames is noticed
    if invalid(login_wdw):
        return
    if login_wdw.first and len(login_wdw.names) > 3:
        # create a db if first time
        db = login.init()  # pylint: disable=invalid-name
        # adds users
        login.add_users(db, login_wdw.names)
        # open login wdw again for loggin in
        login_wdw = ui_login.Login()
        usernames = login.fetch_names()
        login_wdw.usernames = usernames
        login_wdw.mainloop()
    # opens main app with selected user
    try:
        #names = login.fetch_names()
        if login.validate_name(login_wdw.names[0]) and login.validate_pwd(login_wdw.names):
            main_wdw = ui_main.Main(login_wdw.names[0], usernames)
            main_wdw.mainloop()
    except IndexError:
        pass


def invalid(login_wdw):
    if login_wdw.first:
        if len(login_wdw.names) < 4:
            return True
    else:
        if len(login_wdw.names) < 2:
            return True
    return False


if __name__ == "__main__":
    main()
