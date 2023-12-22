import tkinter as tk
from tkinter import ttk

class ArithmeticOperations:
    def __init__(self):
        self.result = 0

    def calculate(self, operation, value1, value2):
        if operation == "Addition":
            self.result = value1 + value2
        elif operation == "Subtraction":
            self.result = value1 - value2
        elif operation == "Multiplication":
            self.result = value1 * value2
        elif operation == "Division":
            if value2 != 0:
                self.result = value1 / value2
            else:
                self.result = "Error (Division by zero)"

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Arithmetic Operations Calculator")

        # Create an instance of the ArithmeticOperations class
        self.arithmetic_calculator = ArithmeticOperations()

        # Labels
        self.label_value1 = tk.Label(master, text="Value 1:")
        self.label_value1.grid(row=0, column=0, padx=10, pady=10)

        self.label_value2 = tk.Label(master, text="Value 2:")
        self.label_value2.grid(row=1, column=0, padx=10, pady=10)

        self.label_operation = tk.Label(master, text="Operation:")
        self.label_operation.grid(row=2, column=0, padx=10, pady=10)

        self.label_result = tk.Label(master, text="Result:")
        self.label_result.grid(row=3, column=0, padx=10, pady=10)

        # Entry widgets
        self.entry_value1 = tk.Entry(master)
        self.entry_value1.grid(row=0, column=1, padx=10, pady=10)

        self.entry_value2 = tk.Entry(master)
        self.entry_value2.grid(row=1, column=1, padx=10, pady=10)

        # Combobox for selecting arithmetic operation
        self.operations = ["Addition", "Subtraction", "Multiplication", "Division"]
        self.combo_operation = ttk.Combobox(master, values=self.operations)
        self.combo_operation.grid(row=2, column=1, padx=10, pady=10)
        self.combo_operation.set("Addition")

        # Result display
        self.result_var = tk.StringVar()
        self.result_label = tk.Label(master, textvariable=self.result_var)
        self.result_label.grid(row=3, column=1, padx=10, pady=10)

        # Button to calculate
        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate(self):
        try:
            value1 = float(self.entry_value1.get())
            value2 = float(self.entry_value2.get())
            operation = self.combo_operation.get()

            self.arithmetic_calculator.calculate(operation, value1, value2)

            # Update the result label
            self.result_var.set(f"Result: {self.arithmetic_calculator.result}")
        except ValueError:
            self.result_var.set("Error (Invalid input)")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
