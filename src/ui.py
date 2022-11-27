import tkinter as tk
import os.path
import access


class Login(tk.Tk):
    def __init__(self):
        # list for usernames
        self.names = []
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
        # label for instructions
        info = tk.Label(self, text="Enter 2 usernames")
        info.grid(row=0, column=0)
        # entry bar for usernames
        entry = tk.Entry(self)
        entry.insert(0, "Name")
        entry.grid(row=0, column=1)
        # button for accepting usernames
        enter = tk.Button(self, text="Enter",
                          command=lambda: self.get_name(entry))
        enter.grid(row=1, column=0)

    def normal_login(self):
        # label for instructions
        info = tk.Label(self, text="Enter your username: ")
        info.grid(row=0, column=0)
        # entry bar for username
        entry = tk.Entry(self)
        entry.grid(row=0, column=1)
        # button for accepting username
        enter = tk.Button(self, text="Enter",
                          command=lambda: self.get_name(entry))
        enter.grid(row=1, column=0)

    def get_name(self, entry):
        # fetch username from entry
        name = entry.get()
        # delete entry
        entry.delete(0, "end")
        # add name to name list
        self.names.append(name)
        # close window if right amount of names is given
        # N_O_T_E: app doesn't currently check if name is valid
        if len(self.names) > 1 and self.first == True or self.first == False:
            self.destroy()


class Main(tk.Tk):
    def __init__(self, username):
        super().__init__()
        # username
        self.user = username
        # window name, size
        self.title("Pyshare")
        self.geometry("800x400")
        # variables for value entries
        self.entry1_var = tk.StringVar()
        self.entry2_var = tk.StringVar()
        # select db
        self.db = access.init()
        # label for the total
        self.total_label = tk.Label(self, text="Total   ")
        self.total_label.grid(row=0, column=0)
        # instruction label for the user
        self.instructions = tk.Label(text="Add a payment    ")
        self.instructions.grid(row=0, column=1)
        # labels for entries
        self.entry_label1 = tk.Label(self, text="Own share")
        self.entry_label1.grid(row=0, column=2)
        self.entry_label2 = tk.Label(self, text="Other's share")
        self.entry_label2.grid(row=0, column=3)
        # show current share
        self.label = tk.Label(self, text=str(self.get_sum()))
        self.label.grid(row=1, column=0)
        # entries for adding payments
        self.entry1 = tk.Entry(self, textvariable=self.entry1_var)
        self.entry1.grid(row=1, column=2)
        self.entry2 = tk.Entry(self, textvariable=self.entry2_var)
        self.entry2.grid(row=1, column=3)
        # button for accepting payments (accesses the db and updates the label)
        enter = tk.Button(self, text="Enter", command=lambda: [
                          self.add_to_db(), self.change_sum()])
        enter.grid(row=1, column=1)
        # variables for the checkbuttons (1-on, 0-off)
        self.v1 = tk.IntVar()
        self.v2 = tk.IntVar()
        # checkbuttons (start with 50-50 activated)
        self.c1 = tk.Checkbutton(
            self, text="Split 50-50", var=self.v1, command=self.splitting)
        self.c2 = tk.Checkbutton(
            self, text="Choose parts", var=self.v2, command=self.splitting, state="disabled")
        self.c1.grid(row=2, column=1)
        self.c2.grid(row=2, column=2)
        self.c1.invoke()
        # update entry1 if 50-50 selected
        self.entry1.bind("<KeyRelease>", lambda e: self.auto_fill())

    def auto_fill(self):
        # fill entry2 if 50-50 is selected, empty after each change
        if self.v1.get() == 1:
            self.entry2.delete(0, "end")
            self.entry2.insert(0, self.entry1_var.get())

    # update the label
    def change_sum(self):
        new_amount = self.get_sum()
        self.label.config(text=str(new_amount))

    # adds payments to the db
    def add_to_db(self):
        # check for the validity of the payment
        try:
            own_share = self.entry1.get()
            others_share = self.entry2.get()
            own_share = float(own_share)
            others_share = float(others_share)
            if own_share < 0 or others_share < 0:
                raise ValueError
            else:
                # add payment, return True if successful
                response = access.pay(self.db, self.user,
                                      own_share, others_share)
                self.entry1.delete(0, "end")
                self.entry2.delete(0, "end")
        except:
            # label for wrong input
            self.err_label = tk.Label(
                self, text="Enter two non-negative numerals!")
            self.err_label.grid(row=2, column=0)
        self.entry1.delete(0, "end")
        try:
            # delete label after a successful payment
            if response:
                self.err_label.destroy()
        except:
            pass

    # fetch the sum for the db

    def get_sum(self):
        amount = access.get_sum(self.db, self.user)
        return amount

    # make sure that only one checkbutton is available for the user

    def splitting(self):
        if self.v1.get() == 1:
            self.c2.config(state="disabled")
        elif self.c2["state"] == "disabled":
            self.c2.config(state="normal")
        elif self.v2.get() == 1:
            self.c1.config(state="disabled")
        else:
            self.c1.config(state="normal")
