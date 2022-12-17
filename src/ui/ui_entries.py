import tkinter as tk


class UiEntries():
    """A class for entries
    """

    def __init__(self, root, auto_fill, callback_entry1_focus, callback_entry2_focus):
        """A constructor for the Entries class

        Args:
            root: root of the main window
            auto_fill: function for filling both entry fields simultaneously
            callback_entry1_focus: function for activating entry field
            callback_entry2_focus: function for activating entry field
        """
        # variables for value entries
        self.entry1_var = tk.StringVar()
        self.entry2_var = tk.StringVar()
        # entries for adding payments
        self.entry1 = tk.Entry(root, textvariable=self.entry1_var)
        self.entry1.grid(row=1, column=2)
        self.entry2 = tk.Entry(root, textvariable=self.entry2_var)
        self.entry2.grid(row=1, column=3)
        # update both entries if 50-50 selected
        self.entry1.bind("<KeyRelease>", lambda e: auto_fill())
        self.entry2.bind("<KeyRelease>", lambda e: auto_fill())
        # allow program to see which entry field is active
        self.entry1.bind("<FocusIn>", lambda e: callback_entry1_focus())
        self.entry2.bind("<FocusIn>", lambda e: callback_entry2_focus())
        # start with both in inactive mode
        self.entry1_focus = False
        self.entry2_focus = False

    def return_attrs(self):
        """A method for returning the arguments for the main window
        """
        return self.entry1, self.entry2, self.entry1_var, self.entry2_var, self.entry1_focus, self.entry2_focus
