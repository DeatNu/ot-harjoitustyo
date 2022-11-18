import tkinter as tk
import os.path
#root = tk.Tk()
import time
import access


class Login(tk.Tk):
    def __init__(self):
        self.names = []
        super().__init__()
        self.first = False
        self.title("Login")
        self.geometry("400x200")

        if not os.path.isfile("users.db"):
            self.first = True
            self.first_login()
            print("!")
            #self.normal_login()
        else:
            print("!!", os.path.isfile("users.db"))
            self.normal_login()


    def first_login(self):
        info = tk.Label(self, text ="Enter 2 usernames")
        info.grid(row=0,column=0)
        entry = tk.Entry(self)
        entry.insert(0, "Name")
        entry.grid(row=0,column=1)
        enter = tk.Button(self, text="Enter", command=lambda: self.get_name(entry, enter))
        enter.grid(row=1,column=0)


    def normal_login(self):
        info = tk.Label(self, text ="Enter your username: ")
        info.grid(row=0,column=0)
        entry = tk.Entry(self)
        #entry.insert(0, "Name")
        entry.grid(row=0,column=1)
        enter = tk.Button(self, text="Enter", command=lambda: self.get_name(entry, enter))
        enter.grid(row=1,column=0)


    def get_name(self, entry, enter):
        name = entry.get()
        entry.delete(0,"end")
        self.names.append(name)
        if len(self.names) > 1 and self.first == True or self.first == False:
            #enter["state"] = "disabled"
            self.destroy()



class Main(tk.Tk):
    def __init__(self, username):
        super().__init__()
        self.user = username
        self.title("Pyshare")
        self.geometry("800x400")
        self.db = access.init()
        self.label = tk.Label(text = str(self.get_sum()))
        self.label.grid(row=0,column=0)
        entry = tk.Entry(self)
        #entry.insert(0, "Name")
        entry.grid(row=0,column=3)
        enter = tk.Button(self, text="Enter", command=lambda: [self.add_to_db(entry), self.change_sum()])
        enter.grid(row=0,column=2)

    def change_sum(self):
        new_amount = self.get_sum()
        self.label.config(text=str(new_amount))

    def add_to_db(self, entry):
        amount = entry.get()
        entry.delete(0,"end")
        access.pay(self.db, self.user, int(amount))

    def get_sum(self):
        amount = access.get_sum(self.db, self.user)
        return amount






    



