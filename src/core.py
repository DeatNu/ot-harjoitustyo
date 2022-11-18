import ui
import login

def main():
    app = ui.Login()
    app.mainloop()
    if len(app.names) < 2 and app.first or len(app.names) < 1 and not app.first:
        return
    if app.first:
        db = login.init()
        login.add_users(db, app.names[0],app.names[1])
        app = ui.Login()
        app.mainloop()
    print("logging in...")
    main = ui.Main(app.names[0])
    main.mainloop()

if __name__ == "__main__":
    main()






