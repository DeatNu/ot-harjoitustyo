import tkinter as tk
from db import access
from ui.ui_frame import UiFrame
from ui.ui_entries import UiEntries
from ui.ui_labels import UiLabels
from ui.ui_check_buttons import UiCheck


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
        self.create_labels()
        # creates entry boxes
        self.create_entries()
        # creates the enter button
        self.create_enter_button()
        # creates the check buttons
        self.create_check_buttons()
        # creates the frame including a listbox and a scrollbar
        self.create_frame()

    def create_frame(self):
        """A method for calling the frame class that creates a frame with a listbox
        """
        # fetch data for the listbox
        data = access.get_transactions(self.db)
        self.payment_frame = UiFrame(data)
        self.payment_frame.grid(row=5, column=0, columnspan=4)

    def create_labels(self):
        """A method for displaying the labels on the screeen
        Args:
            amount: total sum
            colour : colour of the total sum, 0 -> black, <0 -> red, >0 -> green
            name1 : active user
            name2 : unactive user
        Methods:
            access.get_sum() : fetches the total sum
            access.convert_names() : if name ends in s/S, only an apostrophe is added, else 's
        """
        amount, colour = access.get_sum(self.db, self.user)
        name1, name2 = access.convert_names(self.user, self.names)
        self.entry1_label, self.entry2_label, self.total_label, self.instructions, self.sum_label, self.empty_label, \
            self.payment_info, self.comment_label = UiLabels(
                self, name1, name2, amount, colour).return_attrs()

    def create_entries(self):
        """A method for creating the entry fields
        """
        self._entries = UiEntries(
            self, self.auto_fill, self.callback_entry1_focus, self.callback_entry2_focus)
        self.entry1, self.entry2, self.entry1_var, self.entry2_var, self.entry1_focus, self.entry2_focus, self.comment1_entry = self._entries.return_attrs()

    def create_check_buttons(self):
        """A method for creating and initializing the checkbuttons
        """
        self.checkbutton_var1, self.checkbutton_var2, self.checkbutton1, self.checkbutton2 = UiCheck(
            self, self.splitting).return_attrs()

    def create_enter_button(self):
        """A method for creating a button for accepting payments
        """
        # button for accepting payments (accesses the db and updates the label)
        enter = tk.Button(self, text="Enter", command=lambda: [
                          self.add_to_db(), self.change_sum()])
        enter.grid(row=1, column=1)

    def auto_fill(self):
        """A method for filling both entry field simultaneously when 50-50
        splitting is selected
        """
        if self.checkbutton_var1.get() == 1:
            if self.entry1_focus:
                self.entry2.delete(0, "end")
                self.entry2.insert(0, self.entry1_var.get())
            elif self.entry2_focus:
                self.entry1.delete(0, "end")
                self.entry1.insert(0, self.entry2_var.get())

    def change_sum(self):
        """A method for updating the total sum label ad emptying the listbox
        """
        new_amount, new_colour = access.get_sum(self.db, self.user)
        self.sum_label.config(text=str(new_amount), fg=new_colour)
        # listbox is cleared and filled with updated data
        self.payment_frame.payment_listbox.delete(0, "end")
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
        comment = self.comment1_entry.get()
        response = access.pay(self.db, self.user,
                              own_share, others_share, comment)
        self.entry1.delete(0, "end")
        self.entry2.delete(0, "end")
        self.comment1_entry.delete(0, "end")
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
        if self.checkbutton_var1.get() == 1:
            self.checkbutton2.config(state="disabled")
        elif self.checkbutton2["state"] == "disabled":
            self.checkbutton2.config(state="normal")
            self.checkbutton1.config(state="disabled")
            self.checkbutton2.invoke()
        elif self.checkbutton_var2.get() == 1:
            self.checkbutton1.config(state="disabled")
        else:
            self.checkbutton1.config(state="normal")
            self.checkbutton2.config(state="disabled")
            self.checkbutton1.invoke()

    def update_transactions(self):
        """A method for updating the listbox containg the payment information
        Args:
            data : payment data
        """
        data = access.get_transactions(self.db)
        if data is not None:
            for i in data:
                self.payment_frame.payment_listbox.insert(
                    "end", " ".join(map(str, i)))

    def callback_entry1_focus(self):
        """A helper method for turning entry1 active and entry2 unactive
        """
        self.entry1_focus = True
        self.entry2_focus = False

    def callback_entry2_focus(self):
        """A helper method for turning entry2 active and entry1 unactive
        """
        self.entry2_focus = True
        self.entry1_focus = False
