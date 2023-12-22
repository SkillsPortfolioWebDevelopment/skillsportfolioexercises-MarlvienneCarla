import tkinter as tk
from tkinter import messagebox

class Students:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calc_grade(self):
        average_mark = (self.mark1 + self.mark2 + self.mark3) / 3
        return average_mark

    def display(self):
        return f"Name: {self.name}, Average Grade: {self.calc_grade():.2f}"

class StudentsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Students Information App")

        # Create an instance with predefined values
        self.student1 = Students("John", 75, 82, 90)

        # Display information for the first student
        self.label_student1 = tk.Label(master, text=self.student1.display())
        self.label_student1.grid(row=0, column=0, padx=10, pady=10)

        # Button to input values for the second student
        self.input_button = tk.Button(master, text="Input Values", command=self.input_values)
        self.input_button.grid(row=1, column=0, pady=10)

    def input_values(self):
        # Ask user to input values for the second student
        name = input("Enter student name: ")
        mark1 = float(input("Enter mark 1: "))
        mark2 = float(input("Enter mark 2: "))
        mark3 = float(input("Enter mark 3: "))

        # Create an instance with user-input values
        self.student2 = Students(name, mark1, mark2, mark3)

        # Display information for the second student
        self.label_student2 = tk.Label(self.master, text=self.student2.display())
        self.label_student2.grid(row=2, column=0, padx=10, pady=10)
        
        # Display a message box with the average grade for the second student
        messagebox.showinfo("Average Grade", f"The average grade for {self.student2.name} is {self.student2.calc_grade():.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentsGUI(root)
    root.mainloop()
