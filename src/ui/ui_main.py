import tkinter as tk
from db import access


class Main(tk.Tk):
    """A class for the main window of the program.
    Args:
        names : all usernames in the database
        username : active user's name
        db : table for payments
    """

    def __init__(self, username, names):
        """A constructor for the class Main

        Args:
            names : all usernames in the database
            username : active user's name
            db : table for payments
        """
        super().__init__()
        # usernames
        self.names = names
        # current user's name
        self.user = username
        # window name, size
        self.title("Pyshare")
        self.geometry("565x430")
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
        # creates a comment entry and label
        self.comment_entry()

    def frame(self):
        """A method for creating a frame in which
        a listbox and scrollbar exist. The listbox
        contains info about the payments

        Args:
            data : payment data (name - user's share - other's share - comment) 
        """
        # fetch data for the listbox
        data = access.get_transactions(self.db)
        # initialize the frame
        self.frame1 = tk.Frame(self)
        self.frame1.grid(row=5, column=0, columnspan=4)
        # initialize the listbox, fill with data
        self.Lb1 = tk.Listbox(self.frame1, width=68, height=17)
        if data is not None:
            for i in data:
                self.Lb1.insert("end", " ".join(map(str, i)))
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

    def auto_fill(self):
        """A method for filling both entry field simultaneously when 50-50
        splitting is selected
        """
        if self.v1.get() == 1:
            if self.e1_focus:
                self.entry2.delete(0, "end")
                self.entry2.insert(0, self.entry1_var.get())
            elif self.e2_focus:
                self.entry1.delete(0, "end")
                self.entry1.insert(0, self.entry2_var.get())

    def change_sum(self):
        """A method for updating the total sum label ad emptying the listbox
        """
        new_amount, new_colour = access.get_sum(self.db, self.user)
        self.label.config(text=str(new_amount), fg=new_colour)
        # listbox is cleared and filled with updated data
        self.Lb1.delete(0, "end")
        self.update_transactions()

    def add_to_db(self):
        """A method for adding new payments to the database and crearing the entry fields
        Args:
            own_share : active users share of the payment
            others_share : other users share of the payment
            comment : an optional comment on the purchase
            response : successful payment -> True, else -> False
        """
        # check for the validity of the payment
        own_share = self.entry1.get()
        others_share = self.entry2.get()
        comment = self.comment_entry1.get()
        response = access.pay(self.db, self.user,
                              own_share, others_share, comment)
        self.entry1.delete(0, "end")
        self.entry2.delete(0, "end")
        self.comment_entry1.delete(0, "end")
        try:
            self.err_label.destroy()
        except:
            pass
        if not response:
            self.err_label = tk.Label(
                self, text="Enter two non-negative numerals!")
            self.err_label.grid(row=3, column=0, columnspan=3, sticky="w")

    def splitting(self):
        """A helper method for the splitting style
        Makes sure that only one style is active
        """
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

    def update_transactions(self):
        """A method for updating the listbox containg the payment information
        Args:
            data : payment data
        """
        data = access.get_transactions(self.db)
        if data is not None:
            for i in data:
                self.Lb1.insert("end", " ".join(map(str, i)))

    def callback_entry1_focus(self):
        """A helper method for turning entry1 active and entry2 unactive
        """
        self.e1_focus = True
        self.e2_focus = False

    def callback_entry2_focus(self):
        """A helper method for turning entry2 active and entry1 unactive
        """
        self.e2_focus = True
        self.e1_focus = False

    def name_labels(self):
        """A method for dispalying user's names on the screen
        Args:
            name1 : active user
            name2 : unactive user
        Methods:
            access.convert_names() : if name ends in s/S, only an apostrophe is added, else 's
        """
        name1, name2 = access.convert_names(self.user, self.names)
        self.entry_label1 = tk.Label(self, text=f"{name1} share")
        self.entry_label1.grid(row=0, column=2)
        self.entry_label2 = tk.Label(self, text=f"{name2} share")
        self.entry_label2.grid(row=0, column=3)

    def general_labels(self):
        """A method for displaying most of the labels on the screeen
        Args:
            amount: total sum
            colour : colour of the total sum, 0 -> black, <0 -> red, >0 -> green
        Methods:
            access.get_sum() : fetches the total sum
        """
        # label for the total
        self.total_label = tk.Label(self, text="Total   ")
        self.total_label.grid(row=0, column=0)
        # instruction label for the user
        self.instructions = tk.Label(text="Add a payment       ")
        self.instructions.grid(row=0, column=1)
        # show current share
        amount, colour = access.get_sum(self.db, self.user)
        self.label = tk.Label(self, text=str(amount), fg=colour)
        self.label.grid(row=1, column=0)
        # maintains constant window size for self.err_label
        self.empty_label = tk.Label(self)
        self.empty_label.grid(row=3, column=0)
        self.payment_info = tk.Label(text="Name || My share || Other's share")
        self.payment_info.grid(row=4, column=0, columnspan=4, sticky="W")

    def entries(self):
        """A method for creating the entry fields
        """
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

    def enter_button(self):
        """A method for creating a button for accepting payments
        """
        # button for accepting payments (accesses the db and updates the label)
        enter = tk.Button(self, text="Enter", command=lambda: [
                          self.add_to_db(), self.change_sum()])
        enter.grid(row=1, column=1)

    # checkbuttons for switching between paymenet modes
    # Split 50-50: types users part and fills the other's share
    # Choose parts: manually type shares

    def check_buttons(self):
        """a method for creating checkbuttons for switching
        between splitting modes
        Split 50-50 -> automatically match shares
        Choose shares -> manually choose shares
        """
        # variables for the checkbuttons (1-on, 0-off)
        self.v1 = tk.IntVar()
        self.v2 = tk.IntVar()
        # checkbuttons
        self.c1 = tk.Checkbutton(
            self, text="Split 50-50", var=self.v1, command=self.splitting)
        self.c2 = tk.Checkbutton(
            self, text="Choose shares", var=self.v2, command=self.splitting, state="disabled")
        self.c1.grid(row=2, column=0)
        self.c2.grid(row=2, column=1)
        # start with 1st button selected (split 50-50)
        self.c1.invoke()

    def comment_entry(self):
        """A method for creating an entry field for the comment parameter
        """
        self.comment_label = tk.Label(self, text="Comment (optional)")
        self.comment_label.grid(row=2, column=2)
        self.comment_entry1 = tk.Entry(self)
        self.comment_entry1.grid(row=2, column=3)
