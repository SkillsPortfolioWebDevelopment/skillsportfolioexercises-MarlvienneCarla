import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

class CoffeeVendingMachine(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #title of the main window
        self.title("Coffee Vending Machine")
        
        #instances of OptionsFrame and ButtonFrame
        self.options_frame = OptionsFrame(self)
        self.options_frame.pack()
        
        self.button_frame = ButtonFrame(self)
        self.button_frame.pack()
        
class OptionsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #widgets for coffee options
        self.coffee_label = ttk.Label(self, text='Select Coffee Type:')
        self.coffee_options = ttk.Combobox(self, values=['Espresso', 'Cappuccino', 'Latte'])

        #variables for sugar and milk chekcboxes
        self.sugar_var = tk.IntVar()
        self.sugar_checkbtn = ttk.Checkbutton(self, text='Sugar', variable=self.sugar_var)
        self.milk_var = tk.IntVar()
        self.milk_checkbtn = ttk.Checkbutton(self, text='Milk', variable=self.milk_var)
        
        #pack widgets
        self.coffee_label.pack(padx=10, pady=10)
        self.coffee_options.pack(padx=10, pady=10)
        self.sugar_checkbtn.pack(padx=10, pady=5)
        self.milk_checkbtn.pack(padx=10, pady=5)
        
class ButtonFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #create a button to trigger the display of the message
        self.select_button = ttk.Button(self, text='Select', command=self.display_message)
        self.select_button.pack(padx=10, pady=10)
        
    def display_message(self):
        #get selected options from the OptionsFrame
        coffee = app.options_frame.coffee_options.get()
        sugar = 'with Sugar' if app.options_frame.sugar_var.get() == 1 else 'without Sugar'
        milk = 'with Milk' if app.options_frame.milk_var.get() == 1 else 'without Milk'

        #compose the message and display it in a messagebox
        message = f"You have selected {coffee}, {sugar}, and {milk}. Enjoy your coffee!"
        
        messagebox.showinfo("Coffee Vending Machine", message)

app = CoffeeVendingMachine()
app.mainloop()