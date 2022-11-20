import ui
import login

def main():
    #opens login window for creating users
    app = ui.Login()
    #initializes the loop
    app.mainloop()
    #exit the program if invalid number of usernames is noticed
    if len(app.names) < 2 and app.first or len(app.names) < 1 and not app.first:
        return
    if app.first:
        #create a db if first time
        db = login.init()
        #adds users
        login.add_users(db, app.names[0],app.names[1])
        #open login window again for loggin in
        app = ui.Login()
        app.mainloop()
    #opens main app with selected user
    main = ui.Main(app.names[0])
    main.mainloop()

if __name__ == "__main__":
    main()






