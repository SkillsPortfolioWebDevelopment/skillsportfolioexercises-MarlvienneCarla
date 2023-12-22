import tkinter as tk
from tkinter import ttk

class GreetingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #set the title of the main window
        self.title("Greeting App")
        
        #create instances of InputFrame and DisplayFrame
        self.input_frame = InputFrame(self)
        self.display_frame = DisplayFrame(self)
        
        #pack the frames into the main window
        self.input_frame.pack()
        self.display_frame.pack()

class InputFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='lightblue')
        
        #create widgets fo user input
        self.name_label = ttk.Label(self, text='Name:', background='lightblue')
        self.name_entry = ttk.Entry(self)
        self.color_label = ttk.Label(self, text='Color:', background='lightblue')
        self.color_options = ttk.Combobox(self, values=['blue', 'red', 'green'])
        self.update_button = ttk.Button(self, text='Update Greeting',
                                        command=self.update_greeting)
        
        #grid placement of widgets
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        self.color_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.color_options.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        self.update_button.grid(row=2, column=1, padx=5, pady=5, sticky='e')
        
    def update_greeting(self):
        #get user input from entry and combobox
        name = self.name_entry.get()
        color = self.color_options.get()

        #create a greeting message
        greeting = f"Hello, {name}!"
        
        #call the update_greeting method of DisplayFrame to update the label
        app.display_frame.update_greeting(greeting, color)

class DisplayFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='lightgreen')
        
        #creeate a lebl for displaying the greeting
        self.greeting_label = ttk.Label(self, background='lightgreen')
        self.greeting_label.pack(padx=10, pady=10)
        
    def update_greeting(self, greeting, color):
        #update the text and foreground color of the label
        self.greeting_label['text'] = greeting
        self.greeting_label['foreground'] = color

#create an instance of the GreetingApp class and start the main loop
app = GreetingApp()
app.mainloop()