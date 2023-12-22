import tkinter as tk
from tkinter import messagebox

#define a base class for shapes
class Shape:
    def __init__(self):
        self.sides = []

    def input_sides(self):
        pass

    def area(self):
        pass

#subclass for Circle
class Circle(Shape):
    def input_sides(self):
        radius = float(input("Enter the radius of the circle: "))
        self.sides = [radius]

    def area(self):
        return 3.14 * self.sides[0] * self.sides[0]

#subclass for Rectangle
class Rectangle(Shape):
    def input_sides(self):
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        self.sides = [length, width]

    def area(self):
        return self.sides[0] * self.sides[1]

#subclass for Triangle
class Triangle(Shape):
    def input_sides(self):
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        self.sides = [base, height]

    def area(self):
        return 0.5 * self.sides[0] * self.sides[1]

#GUI for the Shape Calculator
class ShapeCalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Shape Area Calculator")

        #create instances of the subclasses
        self.circle = Circle()
        self.rectangle = Rectangle()
        self.triangle = Triangle()

        #buttons for each shape
        self.circle_button = tk.Button(master, text="Calculate Circle Area", command=self.calculate_circle_area)
        self.circle_button.grid(row=0, column=0, pady=10)

        self.rectangle_button = tk.Button(master, text="Calculate Rectangle Area", command=self.calculate_rectangle_area)
        self.rectangle_button.grid(row=1, column=0, pady=10)

        self.triangle_button = tk.Button(master, text="Calculate Triangle Area", command=self.calculate_triangle_area)
        self.triangle_button.grid(row=2, column=0, pady=10)

    #method to calculate and show the area of a circle
    def calculate_circle_area(self):
        self.circle.input_sides()
        area = self.circle.area()
        messagebox.showinfo("Circle Area", f"The area of the circle is: {area:.2f}")

    #method to calculate and show the area of a rectangle
    def calculate_rectangle_area(self):
        self.rectangle.input_sides()
        area = self.rectangle.area()
        messagebox.showinfo("Rectangle Area", f"The area of the rectangle is: {area:.2f}")

    #method to calculate and show the area of a triangle
    def calculate_triangle_area(self):
        self.triangle.input_sides()
        area = self.triangle.area()
        messagebox.showinfo("Triangle Area", f"The area of the triangle is: {area:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeCalculatorGUI(root)
    root.mainloop()
