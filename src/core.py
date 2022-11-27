import ui
import login


# pylint expanantions:
# -name "db" makes no sense in snake_case format


def main():
    # opens login wdw for creating users
    login_wdw = ui.Login()
    # initializes the loop
    login_wdw.mainloop()
    # program won't crash if invalid number of usernames is noticed
    if len(login_wdw.names) < 2 and login_wdw.first or len(login_wdw.names) < 1 and not login_wdw.first:
        return
    if login_wdw.first:
        # create a db if first time
        db = login.init()  # pylint: disable=invalid-name
        # adds users
        login.add_users(db, login_wdw.names[0], login_wdw.names[1])
        # open login wdw again for loggin in
        login_wdw = ui.Login()
        login_wdw.mainloop()
    # opens main app with selected user
    main_wdw = ui.Main(login_wdw.names[0])
    main_wdw.mainloop()


if __name__ == "__main__":
    main()
