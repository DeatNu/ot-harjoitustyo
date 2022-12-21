import tkinter as tk


class UiCheck():
    """a class for creating checkbuttons for switching
    between splitting modes
    Split 50-50 -> automatically match shares
    Choose shares -> manually choose shares
    """

    def __init__(self, root):
        """A constructor for the class UiCheck
        """
        # variables for the checkbuttons (1-on, 0-off)
        self.checkbutton_var1 = tk.IntVar()
        self.checkbutton_var2 = tk.IntVar()
        # checkbuttons
        self.checkbutton1 = tk.Checkbutton(
            root, text="Split 50-50", var=self.checkbutton_var1, command=None)
        self.checkbutton2 = tk.Checkbutton(
            root, text="Choose shares", var=self.checkbutton_var2, command=None, state="disabled")
        self.checkbutton1.grid(row=2, column=0)
        self.checkbutton2.grid(row=2, column=1)
        # configure commands for checkbuttons
        self.checkbutton1.config(command=self.splitting)
        self.checkbutton2.config(command=self.splitting)
        # start with 1st button selected (split 50-50)
        self.checkbutton1.invoke()

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

    def return_attrs(self):
        return self.checkbutton_var1, self.checkbutton_var2, self.checkbutton1, self.checkbutton2, self.splitting
