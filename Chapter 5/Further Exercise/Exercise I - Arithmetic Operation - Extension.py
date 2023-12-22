import tkinter as tk
from tkinter import ttk, messagebox

class ArithmeticOperations:
    def __init__(self):
        self.result = 0

    def calculate(self, operation_type, value1, value2):
        try:
            if operation_type == "Arithmetic":
                self.result = self.arithmetic_operation(value1, value2)
            elif operation_type == "Relational":
                self.result = self.relational_operation(value1, value2)
            # Add more operation types as needed
            else:
                messagebox.showwarning("Invalid Operation Type", "Please select a valid operation type.")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

    def arithmetic_operation(self, value1, value2):
        raise NotImplementedError("Subclasses should implement this method")

    def relational_operation(self, value1, value2):
        raise NotImplementedError("Subclasses should implement this method")

class ArithmeticCalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Arithmetic Calculator")

        # Create an instance of the ArithmeticOperations class
        self.arithmetic_calculator = ArithmeticOperations()

        # Labels
        self.label_value1 = tk.Label(master, text="Value 1:")
        self.label_value1.grid(row=0, column=0, padx=10, pady=10)

        self.label_value2 = tk.Label(master, text="Value 2:")
        self.label_value2.grid(row=1, column=0, padx=10, pady=10)

        self.label_operation_type = tk.Label(master, text="Operation Type:")
        self.label_operation_type.grid(row=2, column=0, padx=10, pady=10)

        self.label_result = tk.Label(master, text="Result:")
        self.label_result.grid(row=3, column=0, padx=10, pady=10)

        # Entry widgets
        self.entry_value1 = tk.Entry(master)
        self.entry_value1.grid(row=0, column=1, padx=10, pady=10)

        self.entry_value2 = tk.Entry(master)
        self.entry_value2.grid(row=1, column=1, padx=10, pady=10)

        # Combobox for selecting operation type
        self.operation_types = ["Arithmetic", "Relational"]
        self.combo_operation_type = ttk.Combobox(master, values=self.operation_types)
        self.combo_operation_type.grid(row=2, column=1, padx=10, pady=10)
        self.combo_operation_type.set("Arithmetic")

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
            operation_type = self.combo_operation_type.get()

            self.arithmetic_calculator.calculate(operation_type, value1, value2)

            # Update the result label
            self.result_var.set(f"Result: {self.arithmetic_calculator.result}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

class AdvancedArithmeticCalculator(ArithmeticOperations):
    def arithmetic_operation(self, value1, value2):
        return value1 + value2

    def relational_operation(self, value1, value2):
        return value1 > value2

if __name__ == "__main__":
    root = tk.Tk()
    app = ArithmeticCalculatorGUI(root)
    root.mainloop()
