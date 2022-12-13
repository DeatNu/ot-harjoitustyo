import tkinter as tk
import os


class Login(tk.Tk):
    """A class for the login window. Inherits the class tk.TK

    Main methods:
        first_login() : used to create new users
        normal_login() : used to gain access to the main window
    """

    def __init__(self):
        """A constructor for the class Login

        Args:
            names : all usernames stored in the database
            username : active user's name 
            first : no users created -> True, else -> False

        Methods:
            first_login() : used to create new users
            normal_login() : used to gain access to the main window
        """
        # list for usernames
        self.names = []
        self.usernames = []
        super().__init__()
        # assume that app has been launched previously
        self.first = False
        # set title and window size
        self.title("Login")
        self.geometry("400x200")

        # check if first time opeing the app
        if not os.path.isfile("pyshare.db"):
            self.first = True
            self.first_login()
        else:
            self.normal_login()

    def first_login(self):
        """Modifies the login window for creating new users 
        """
        # label for instructions
        self.info = tk.Label(self, text="Enter first username: ")
        self.info.grid(row=0, column=0)
        # entry bar for usernames
        entry = tk.Entry(self)
        entry.insert(0, "Name")
        entry.grid(row=0, column=1)
        # button for accepting usernames
        enter = tk.Button(self, text="Enter",
                          command=lambda: self.get_name(entry))
        enter.grid(row=1, column=0)

    def normal_login(self):
        """Modifies the login window for logging in
        """
        # label for instructions
        self.info = tk.Label(self, text="Enter your username: ")
        self.info.grid(row=0, column=0)
        # entry bar for username
        self.entry = tk.Entry(self)
        self.entry.grid(row=0, column=1)
        # button for accepting username
        enter = tk.Button(self, text="Enter",
                          command=lambda: self.get_name(self.entry))
        enter.grid(row=1, column=0)
        self.v1 = tk.IntVar()
        self.help = tk.Checkbutton(
            self, text="Forgot username?", var=self.v1, command=self.reveal_usernames)
        self.help.grid(row=1, column=1)

    def reveal_usernames(self):
        """A method for showing usernames in the database
        in case the user forgot theirs
        """
        if self.v1.get() == 1:
            # 1 -> pressed
            self.title_label = tk.Label(text="Usernames: ")
            self.title_label.grid(row=2, column=0)
            self.user_label1 = tk.Label(text=self.usernames[0])
            self.user_label1.grid(row=3, column=0, columnspan=5, sticky="W")
            self.user_label2 = tk.Label(text=self.usernames[1])
            self.user_label2.grid(row=4, column=0, columnspan=5, sticky="W")
        elif self.v1.get() == 0:
            # 0 -> not pressed
            self.title_label.destroy()
            self.user_label1.destroy()
            self.user_label2.destroy()

    def get_name(self, entry):
        """A method for fetching the names and passwords
        Exits the login window when conditions satisfied 

        Args:
            name : name/password fetched
            entry : field where input is typed
        """
        # fetch username from entry
        name = entry.get()
        if len(name) < 1:
            return
        # delete entry
        entry.delete(0, "end")
        # add name to name list
        if self.first:
            if len(self.names) > 0:
                if name in self.names:
                    return
        self.names.append(name)
        self.config_label()
        # close window if right amount of names is given
        # N_O_T_E: app doesn't currently check if name is valid
        if len(self.names) > 3 and self.first or not self.first and len(self.names) > 1:
            self.destroy()

    def config_label(self):
        """A method for changing the labels
        """
        labels = ["Enter first password: ",
                  "Enter second username: ", "Enter second password: "]
        labels2 = ["Enter your password: "]
        if self.first and len(self.names) < 4:
            self.info.config(text=labels[len(self.names)-1])
        elif len(self.names) < 2:
            self.info.config(text=labels2[len(self.names)-1])
        if len(self.names) % 2 == 1:
            if not self.first:
                self.entry.config(show="*")
