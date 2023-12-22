import tkinter as tk

class ShapeDrawer(tk.Tk):
    def __init__(self):
        super().__init__()

        #set the title of the main window
        self.title("Shape Drawer")

        #create a canvas for drawing shapes
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()

        #create a variable to store the selected shape and set initial value
        self.shape_var = tk.StringVar(self)
        self.shape_var.set("Select Shape")

        #create a dropdown menu for selecting the shape
        shape_options = ["Select Shape", "Oval", "Rectangle", "Square", "Triangle"]
        shape_dropdown = tk.OptionMenu(self, self.shape_var, *shape_options, command=self.show_input_fields)
        shape_dropdown.pack(padx=10, pady=10)

        #label for input coordinates
        self.input_label = tk.Label(self, text="Input Coordinates:")
        self.input_label.pack(padx=10, pady=5)

        #frame for input fields
        self.input_frame = tk.Frame(self, padx=10, pady=5)
        self.input_frame.pack()

        #input fields for coordinates
        self.coord1_label = tk.Label(self.input_frame, text="Coordinate 1:")
        self.coord1_entry = tk.Entry(self.input_frame, width=10)
        self.coord1_label.grid(row=0, column=0)
        self.coord1_entry.grid(row=0, column=1)

        self.coord2_label = tk.Label(self.input_frame, text="Coordinate 2:")
        self.coord2_entry = tk.Entry(self.input_frame, width=10)
        self.coord2_label.grid(row=1, column=0)
        self.coord2_entry.grid(row=1, column=1)

        #button to draw the selected shape
        self.draw_button = tk.Button(self, text="Draw", command=self.draw_shape)
        self.draw_button.pack(padx=10, pady=10)

    def show_input_fields(self, shape):
        #show or hide input fields based on the selected shape
        if shape == "Select Shape":
            self.input_frame.pack_forget()
        else:
            self.input_frame.pack()

    def draw_shape(self):
        #get the selected shape and input coordinates
        shape = self.shape_var.get()
        coord1 = self.coord1_entry.get()
        coord2 = self.coord2_entry.get()

        #draw the selected shape on the canvas
        if shape == "Oval":
            self.canvas.create_oval(coord1, coord2, outline='black')
        elif shape == "Rectangle":
            self.canvas.create_rectangle(coord1, coord2, outline='black')
        elif shape == "Square":
            self.canvas.create_rectangle(coord1, coord2, outline='black')
        elif shape == "Triangle":
            coords = [int(coord) for coord in coord1.split(",")]
            coords += [int(coord) for coord in coord2.split(",")]
            self.canvas.create_polygon(coords, outline='black')

#create an instance of the ShapeDrawer class and start the main loop
app = ShapeDrawer()
app.mainloop()
