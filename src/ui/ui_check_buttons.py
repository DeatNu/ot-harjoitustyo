import tkinter as tk


class UiCheck():
    """a class for creating checkbuttons for switching
    between splitting modes
    Split 50-50 -> automatically match shares
    Choose shares -> manually choose shares
    """

    def __init__(self, root, splitting):
        """A constructor for the class UiCheck
        """
        # variables for the checkbuttons (1-on, 0-off)
        self.checkbutton_var1 = tk.IntVar()
        self.checkbutton_var2 = tk.IntVar()
        # checkbuttons
        self.checkbutton1 = tk.Checkbutton(
            root, text="Split 50-50", var=self.checkbutton_var1, command=splitting)
        self.checkbutton2 = tk.Checkbutton(
            root, text="Choose shares", var=self.checkbutton_var2, command=splitting, state="disabled")
        self.checkbutton1.grid(row=2, column=0)
        self.checkbutton2.grid(row=2, column=1)
        # start with 1st button selected (split 50-50)
        self.checkbutton1.invoke()

    def return_attrs(self):
        return self.checkbutton_var1, self.checkbutton_var2, self.checkbutton1, self.checkbutton2
