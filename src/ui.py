import tkinter as tk
import os.path
#root = tk.Tk()
import time
import access


class Login(tk.Tk):
    def __init__(self):
        #list for usernames
        self.names = []
        super().__init__()
        #assume that app has been launched previously
        self.first = False
        #set title and window size
        self.title("Login")
        self.geometry("400x200")

        #check if first time opeing the app
        if not os.path.isfile("users.db"):
            self.first = True
            self.first_login()
        else:
            self.normal_login()


    def first_login(self):
        #label for instructions
        info = tk.Label(self, text ="Enter 2 usernames")
        info.grid(row=0,column=0)
        #entry bar for usernames
        entry = tk.Entry(self)
        entry.insert(0, "Name")
        entry.grid(row=0,column=1)
        #button for accepting usernames
        enter = tk.Button(self, text="Enter", command=lambda: self.get_name(entry, enter))
        enter.grid(row=1,column=0)


    def normal_login(self):
        #label for instructions
        info = tk.Label(self, text ="Enter your username: ")
        info.grid(row=0,column=0)
        #entry bar for username
        entry = tk.Entry(self)
        entry.grid(row=0,column=1)
        #button for accepting username
        enter = tk.Button(self, text="Enter", command=lambda: self.get_name(entry, enter))
        enter.grid(row=1,column=0)


    def get_name(self, entry, enter):
        #fetch username from entry
        name = entry.get()
        #delete entry
        entry.delete(0,"end")
        #add name to name list
        self.names.append(name)
        #close window if right amount of names is given
        #N_O_T_E: app doesn't currently check if name is valid
        if len(self.names) > 1 and self.first == True or self.first == False:
            #enter["state"] = "disabled"
            self.destroy()



class Main(tk.Tk):
    def __init__(self, username):
        super().__init__()
        #username
        self.user = username
        #window name, size
        self.title("Pyshare")
        self.geometry("800x400")
        #select db
        self.db = access.init()
        #show current share (currently shows same number for all)
        self.instructions = tk.Label(text="Add a payment")
        self.instructions.grid(row=0,column=0)
        self.label = tk.Label(self, text = str(self.get_sum()))
        self.label.grid(row=1,column=0)
        #entry for adding payments
        entry = tk.Entry(self)
        entry.grid(row=1,column=2)
        #button for accepting payments
        enter = tk.Button(self, text="Enter", command=lambda: [self.add_to_db(entry), self.change_sum()])
        enter.grid(row=1,column=1)

    #update the label
    def change_sum(self):
        new_amount = self.get_sum()
        self.label.config(text=str(new_amount))

    #adds payments to the db
    def add_to_db(self, entry):
        amount = entry.get()
        #check for the validity of the payment
        try:
            amount = float(amount)
            if amount < 0:
                raise ValueError
            else:
                #add payment, return True if successful
                response = access.pay(self.db, self.user, amount)
        except:
            #label for wrong input
            self.err_label = tk.Label(self, text="Enter only non-negative numerals!")
            self.err_label.grid(row=2,column=0)
        entry.delete(0,"end")
        try:
            #delelte label after a successful payment
            if response:
                self.err_label.destroy()
        except:
            pass


    #fetch the sum for the db
    def get_sum(self):
        amount = access.get_sum(self.db, self.user)
        return amount






    



