import tkinter as tk
from tkinter import ttk
from math import pi

class AreaCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        #set the title and geometry of the main window
        self.title("Area Calculator")
        self.geometry("400x300")

        #create a notebook to hold different frames for each shape
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)

        #create instances of CircleFrame, SquareFrame, and RectangleFrame
        self.circle_frame = CircleFrame(self.notebook)
        self.square_frame = SquareFrame(self.notebook)
        self.rectangle_frame = RectangleFrame(self.notebook)

        #add frames to the notebook with corresponding labels
        self.notebook.add(self.circle_frame, text="Circle")
        self.notebook.add(self.square_frame, text="Square")
        self.notebook.add(self.rectangle_frame, text="Rectangle")

class CircleFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #widgets for circle calculations
        self.radius_label = ttk.Label(self, text='Radius:')
        self.radius_entry = ttk.Entry(self)
        self.calculate_button = ttk.Button(self, text='Calculate', command=self.calculate_area)
        self.result_label = ttk.Label(self, text='')

        #pack widgets
        self.radius_label.pack(padx=10, pady=10)
        self.radius_entry.pack(padx=10)
        self.calculate_button.pack(padx=10, pady=10)
        self.result_label.pack(padx=10, pady=5)

    def calculate_area(self):
        #calculate the area of a circle and update the result label
        radius = float(self.radius_entry.get())
        area = pi * radius ** 2
        self.result_label.configure(text=f"Area: {area}")

class SquareFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #widgets for square calculations
        self.side_label = ttk.Label(self, text='Side:')
        self.side_entry = ttk.Entry(self)
        self.calculate_button = ttk.Button(self, text='Calculate', command=self.calculate_area)
        self.result_label = ttk.Label(self, text='')

        #pack widgets
        self.side_label.pack(padx=10, pady=10)
        self.side_entry.pack(padx=10)
        self.calculate_button.pack(padx=10, pady=10)
        self.result_label.pack(padx=10, pady=5)

    def calculate_area(self):
        #calculate the area of a square and update the result label
        side = float(self.side_entry.get())
        area = side ** 2
        self.result_label.configure(text=f"Area: {area}")

class RectangleFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #widgets for reactangle calculations
        self.length_label = ttk.Label(self, text='Length:')
        self.length_entry = ttk.Entry(self)
        self.width_label = ttk.Label(self, text='Width:')
        self.width_entry = ttk.Entry(self)
        self.calculate_button = ttk.Button(self, text='Calculate', command=self.calculate_area)
        self.result_label = ttk.Label(self, text='')

        #pack widgets
        self.length_label.pack(padx=10, pady=10)
        self.length_entry.pack(padx=10)
        self.width_label.pack(padx=10, pady=5)
        self.width_entry.pack(padx=10)
        self.calculate_button.pack(padx=10, pady=10)
        self.result_label.pack(padx=10, pady=5)

    def calculate_area(self):
        #calculate he area of a reactangle and upate the result label
        length = float(self.length_entry.get())
        width = float(self.width_entry.get())
        area = length * width
        self.result_label.configure(text=f"Area: {area}")

app = AreaCalculator()
app.mainloop()