import tkinter as tk
from tkinter import ttk

class BurgerShackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Burger Shack Ordering System")

        # Variables to store user choices
        self.burger_type_var = tk.StringVar()
        self.toppings_var = tk.StringVar()
        self.condiments_var = tk.StringVar()
        self.sides_var = tk.StringVar()
        self.payment_var = tk.StringVar()

        # Initialize GUI components
        self.create_widgets()

    def create_widgets(self):
        # Burger Type
        burger_label = ttk.Label(self.root, text="Choose Burger Type:")
        burger_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        burger_types = ["Beef", "Chicken", "Vegetarian"]
        burger_dropdown = ttk.Combobox(self.root, textvariable=self.burger_type_var, values=burger_types)
        burger_dropdown.grid(row=0, column=1, padx=10, pady=5)

        # Toppings
        toppings_label = ttk.Label(self.root, text="Choose Toppings:")
        toppings_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        toppings_entry = ttk.Entry(self.root, textvariable=self.toppings_var)
        toppings_entry.grid(row=1, column=1, padx=10, pady=5)

        # Condiments
        condiments_label = ttk.Label(self.root, text="Choose Condiments:")
        condiments_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        condiments_entry = ttk.Entry(self.root, textvariable=self.condiments_var)
        condiments_entry.grid(row=2, column=1, padx=10, pady=5)

        # Sides
        sides_label = ttk.Label(self.root, text="Choose Sides:")
        sides_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        sides_entry = ttk.Entry(self.root, textvariable=self.sides_var)
        sides_entry.grid(row=3, column=1, padx=10, pady=5)

        # Payment
        payment_label = ttk.Label(self.root, text="Enter Payment Amount:")
        payment_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        payment_entry = ttk.Entry(self.root, textvariable=self.payment_var)
        payment_entry.grid(row=4, column=1, padx=10, pady=5)

        # Order Button
        order_button = ttk.Button(self.root, text="Place Order", command=self.place_order)
        order_button.grid(row=5, column=0, columnspan=2, pady=10)

    def place_order(self):
        # Get user choices
        burger_type = self.burger_type_var.get()
        toppings = self.toppings_var.get()
        condiments = self.condiments_var.get()
        sides = self.sides_var.get()
        payment = self.payment_var.get()

        # Process order (add your logic here)
        order_summary = f"Burger: {burger_type}\nToppings: {toppings}\nCondiments: {condiments}\nSides: {sides}"

        # Calculate change (add your logic here)
        change = float(payment) - self.calculate_order_cost()

        # Display order summary and change
        result_text = f"Order Summary:\n{order_summary}\n\nChange: {change:.2f} AED"
        result_label = ttk.Label(self.root, text=result_text)
        result_label.grid(row=6, column=0, columnspan=2, pady=10)

    def calculate_order_cost(self):
        # Add your logic to calculate the cost of the order based on choices
        # This is a placeholder; you should modify it according to your pricing structure
        return 20.0

if __name__ == "__main__":
    root = tk.Tk()
    app = BurgerShackApp(root)
    root.mainloop()
