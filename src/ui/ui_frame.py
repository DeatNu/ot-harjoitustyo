import tkinter as tk


class UiFrame(tk.Frame):
    """A class for creating a frame in which
    a listbox and scrollbar exist. The listbox
    contains info about the payments
    """

    def __init__(self, data):
        """A constructor for the class UiFrame
        Args:
            data : payment data (name - user's share - other's share - comment) 
        """
        super().__init__()
        # initialize the frame
        # initialize the listbox, fill with data
        self.payment_listbox = tk.Listbox(self, width=68, height=17, font ="Courier 11")
        if data is not None:
            for i in data:
                self.payment_listbox.insert("end", self.format_string(i))
        self.payment_listbox.grid(row=0, column=0)
        # initialize a vertical scrollbar
        self.scrollbar = tk.Scrollbar(self, orient='vertical')
        self.scrollbar.grid(row=0, column=1, sticky='ns', rowspan=3)
        # set scrollbar to the listbox
        self.payment_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.payment_listbox.yview)


    def format_string(self, item):
        """a helper method for converting a tuple to a formatted string

        Args:
            item: tuple containeing payment data

        Returns:
            s: formatted string
        """
        lengths = [17,7,10]
        s = ""
        for i,j in zip(item[:-1],lengths):
            if len(str(i))>j:
                i = i[:j-3] + "..."
            s += str(i).ljust(j) + "   "
        s += item[-1]
        return s

    def return_func(self):
        """A method for returning the formatting function
        """
        return self.format_string