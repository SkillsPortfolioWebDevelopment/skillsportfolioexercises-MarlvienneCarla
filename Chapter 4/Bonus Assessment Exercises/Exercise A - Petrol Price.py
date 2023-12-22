import tkinter as tk
from tkinter import messagebox

class PetrolCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Petrol Calculator App")

        self.data = self.load_data()

        #fixed the label name from self.result_label to self.self_label
        self.result_label = tk.Label(master, text="", pady=10)
        self.result_label.grid(row=0, column=0, columnspan=2)

        self.calculate_cost_button = tk.Button(master, text="Calculate Cost per liter", command=self.calculate_cost_per_liter)
        self.calculate_cost_button.grid(row=1, column=0, pady=5)

        #corrected the method name from calculate_average_button to calculate_average_price
        self.calculate_average_button = tk.Button(master, text="Calculate Average Price per Liter", command=self.calculate_average_price)
        self.calculate_average_button.grid(row=1, column=1, pady=5)

        #corrected the method name from calculate_under_3_5_button to calculate_under_3_5
        self.calculate_under_3_5_button = tk.Button(master, text="Calculate Liters under 3.5 AED/Liter", command=self.calculate_under_3_5)
        self.calculate_under_3_5_button.grid(row=2, column=0, columnspan=2, pady=5)

    def load_data(self):
        try:
            with open("petrolPrice.txt", "r") as file:
                #fixed the typo in read.lines() to readlines()
                lines = file.readlines()
                data = [tuple(map(float, line.strip().split('\t'))) for line in lines[1:]]
            return data
        except FileNotFoundError:
            messagebox.showwarning("File not Found", "petrolPrice.txt not found.") 
        except Exception as e:
            messagebox.showerror("Error", f"Error reading from file: {str(e)}")       

    def calculate_cost_per_liter(self):
        total_cost = sum(cost for liters, cost in self.data)
        total_liters = sum(liters for liters, cost in self.data)

        cost_per_liter = total_cost / total_liters

        self.result_label.config(text=f"Cost per liter: {cost_per_liter:.2f} AED")

    #corrected the method name from calculate_average_button to calculate_average_price
    def calculate_average_price(self):
        average_price = sum(cost for liters, cost in self.data) / len(self.data)
        self.result_label.config(text=f"Average price per liter: {average_price:.2f} AED")

    #corrected the method name from calculate_under_3_5_button to calculate_under_3_5
    def calculate_under_3_5(self):
        #changed Liters to Liters under 3.5 AED per liter in the result text
        liters_under_3_5 = sum(liters for liters, cost in self.data if cost / liters < 3.5)
        self.result_label.config(text=f"Liters bought at under 3.5 AED per liter: {liters_under_3_5:.2f} Liters")

if __name__ == "__main__":
    root = tk.Tk()
    app = PetrolCalculatorApp(root)
    root.mainloop()
