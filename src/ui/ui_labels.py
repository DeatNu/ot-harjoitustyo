import tkinter as tk


class UiLabels():
    """A class for creating labels to the main window
    """

    def __init__(self, root, name1, name2, amount, colour):
        """A constructor for the class UiLabels

        Args:
            root : root of the main window
            name1 : active user
            name2 : other user
            amount : sum when starting the app
            colour : color of the sum label
        """
        # labels for names
        self.entry1_label = tk.Label(root, text=f"{name1} share")
        self.entry1_label.grid(row=0, column=2)
        self.entry2_label = tk.Label(root, text=f"{name2} share")
        self.entry2_label.grid(row=0, column=3)
        # label for the total
        self.total_label = tk.Label(root, text="Balance ")
        self.total_label.grid(row=0, column=0)
        # instruction label for the user
        self.instructions = tk.Label(root, text="Add a payment       ")
        self.instructions.grid(row=0, column=1)
        # show current share
        self.sum_label = tk.Label(root, text=str(amount), fg=colour)
        self.sum_label.grid(row=1, column=0)
        # maintains constant window size for self.err_label
        self.empty_label = tk.Label(root)
        self.empty_label.grid(row=3, column=0)
        self.payment_info = tk.Label(
            root, text="Name                             ||   My share   ||   Other's share   ||   Comment")
        self.payment_info.grid(row=4, column=0, columnspan=4, sticky="W")
        # label and entry field for the optional payment comment
        self.comment_label = tk.Label(root, text="Comment (optional)")
        self.comment_label.grid(row=2, column=2)

    def return_attrs(self):
        return (self.entry1_label, self.entry2_label, self.total_label, self.instructions,
                self.sum_label, self.empty_label, self.payment_info, self.comment_label)
