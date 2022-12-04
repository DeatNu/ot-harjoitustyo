import tkinter as tk
import os.path
from db import access


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
        if len(name) < 1:
            return
        # delete entry
        entry.delete(0, "end")
        # add name to name list
        if self.first:
            if len(self.names) > 0:
                if name == self.names[0]:
                    return
        self.names.append(name)
        # close window if right amount of names is given
        # N_O_T_E: app doesn't currently check if name is valid
        if len(self.names) > 1 and self.first == True or self.first == False:
            self.destroy()


class Main(tk.Tk):
    def __init__(self, username, names):
        super().__init__()
        # usernames
        self.names = names
        # current user's name
        self.user = username
        # window name, size
        self.title("Pyshare")
        self.geometry("530x430")
        # select (and initialize) db
        self.db = access.init()
        # creates labels
        self.general_labels()
        # creates name labels
        self.name_labels()
        # creates entry boxes
        self.entries()
        # creates the enter button
        self.enter_button()
        # creates the check buttons
        self.check_buttons()
        # creates the frame including a listbox and a scrollbar
        self.frame()

    def frame(self):
        # fetch data for the listbox
        data = access.get_transactions(self.db)
        # initialize the frame
        self.frame1 = tk.Frame(self)
        self.frame1.grid(row=5, column=0, columnspan=4)
        # initialize the listbox, fill with data
        self.Lb1 = tk.Listbox(self.frame1, width=64, height=17)
        if data is not None:
            for i in data:
                self.Lb1.insert("end", i)
        self.Lb1.grid(row=0, column=0)
        # initialize a vertical scrollbar
        self.v_bar = tk.Scrollbar(self.frame1, orient='vertical')
        self.v_bar.grid(row=0, column=1, sticky='ns', rowspan=3)
        # set scrollbar to the listbox
        self.Lb1.config(yscrollcommand=self.v_bar.set)
        self.v_bar.config(command=self.Lb1.yview)
        # enables the program to see which entry field is active
        self.entry1.bind("<FocusIn>", lambda e: self.callback_entry1_focus())
        self.entry2.bind("<FocusIn>", lambda e: self.callback_entry2_focus())
        # start with both in inactive mode
        self.e1_focus = False
        self.e2_focus = False

    # fill the other entry field if 50-50 is selected, empty after each change
    def auto_fill(self):
        if self.v1.get() == 1:
            if self.e1_focus:
                self.entry2.delete(0, "end")
                self.entry2.insert(0, self.entry1_var.get())
            elif self.e2_focus:
                self.entry1.delete(0, "end")
                self.entry1.insert(0, self.entry2_var.get())

    # update the label and the lsitbox

    def change_sum(self):
        new_amount = access.get_sum(self.db, self.user)
        self.label.config(text=str(new_amount))
        # listbox is cleared and filled with updated data
        self.Lb1.delete(0, "end")
        self.update_transactions()

    # adds payments to the db
    def add_to_db(self):
        # check for the validity of the payment
        own_share = self.entry1.get()
        others_share = self.entry2.get()
        response = access.pay(self.db, self.user, own_share, others_share)
        self.entry1.delete(0, "end")
        self.entry2.delete(0, "end")
        try:
            self.err_label.destroy()
        except:
            pass
        if not response:
            self.err_label = tk.Label(
                self, text="Enter two non-negative numerals!")
            self.err_label.grid(row=3, column=0, columnspan=3, sticky="w")

    # make sure that only one checkbutton is available for the user

    def splitting(self):
        if self.v1.get() == 1:
            self.c2.config(state="disabled")
        elif self.c2["state"] == "disabled":
            self.c2.config(state="normal")
            self.c1.config(state="disabled")
            self.c2.invoke()
        elif self.v2.get() == 1:
            self.c1.config(state="disabled")
        else:
            self.c1.config(state="normal")
            self.c2.config(state="disabled")
            self.c1.invoke()

    # gets new data after a new payment
    # and updates the listbox

    def update_transactions(self):
        # payment data
        data = access.get_transactions(self.db)
        if data is not None:
            for i in data:
                self.Lb1.insert("end", i)

    # entry2 -> entry1 enabled
    def callback_entry1_focus(self):
        self.e1_focus = True
        self.e2_focus = False

    # entry1 -> entry2 enabled
    def callback_entry2_focus(self):
        self.e2_focus = True
        self.e1_focus = False

    # draws both users' names on the screen
    # if name ends in s/S, only an apostrophe is added
    # active user displayed on left
    def name_labels(self):
        name1, name2 = access.convert_names(self.user, self.names)
        self.entry_label1 = tk.Label(self, text=f"{name1} share")
        self.entry_label1.grid(row=0, column=2)
        self.entry_label2 = tk.Label(self, text=f"{name2} share")
        self.entry_label2.grid(row=0, column=3)

    def general_labels(self):
        # label for the total
        self.total_label = tk.Label(self, text="Total   ")
        self.total_label.grid(row=0, column=0)
        # instruction label for the user
        self.instructions = tk.Label(text="Add a payment    ")
        self.instructions.grid(row=0, column=1)
        # show current share
        self.label = tk.Label(self, text=str(
            access.get_sum(self.db, self.user)))
        self.label.grid(row=1, column=0)
        # maintains constant window size for self.err_label
        self.empty_label = tk.Label(self)
        self.empty_label.grid(row=3, column=0)
        self.payment_info = tk.Label(text="Name || My share || Other's share")
        self.payment_info.grid(row=4, column=0, columnspan=4, sticky="W")

    # entry fields for both users
    def entries(self):
        # variables for value entries
        self.entry1_var = tk.StringVar()
        self.entry2_var = tk.StringVar()
        # entries for adding payments
        self.entry1 = tk.Entry(self, textvariable=self.entry1_var)
        self.entry1.grid(row=1, column=2)
        self.entry2 = tk.Entry(self, textvariable=self.entry2_var)
        self.entry2.grid(row=1, column=3)
        # update both entries if 50-50 selected
        self.entry1.bind("<KeyRelease>", lambda e: self.auto_fill())
        self.entry2.bind("<KeyRelease>", lambda e: self.auto_fill())

    # button for accepting payments
    def enter_button(self):
        # button for accepting payments (accesses the db and updates the label)
        enter = tk.Button(self, text="Enter", command=lambda: [
                          self.add_to_db(), self.change_sum()])
        enter.grid(row=1, column=1)

    # checkbuttons for switching between paymenet modes
    # Split 50-50: types users part and fills the other's share
    # Choose parts: manually type shares

    def check_buttons(self):
        # variables for the checkbuttons (1-on, 0-off)
        self.v1 = tk.IntVar()
        self.v2 = tk.IntVar()
        # checkbuttons
        self.c1 = tk.Checkbutton(
            self, text="Split 50-50", var=self.v1, command=self.splitting)
        self.c2 = tk.Checkbutton(
            self, text="Choose shares", var=self.v2, command=self.splitting, state="disabled")
        self.c1.grid(row=2, column=1)
        self.c2.grid(row=2, column=2)
        # start with 1st button selected (split 50-50)
        self.c1.invoke()
