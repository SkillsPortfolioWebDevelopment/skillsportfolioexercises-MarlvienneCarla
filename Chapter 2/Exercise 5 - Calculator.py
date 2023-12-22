import tkinter as tk

#fucntion to perform arithmetic operation based on user input
def perform_operation():
    #get the number and operation form the user input
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

#perform the slected operation and update the result label
    if operation == "Addition":
        result.set(num1 + num2)
    elif operation == "Subtraction":
        result.set(num1 - num2)
    elif operation == "Multiplication":
        result.set(num1 * num2)
    elif operation == "Division":
        if num2 != 0:
            result.set(num1 / num2)
        else:
            result.set("Division by zero")
    elif operation == "Modulo Division":
        if num2 != 0:
            result.set(num1 % num2)
        else:
            result.set("Division by zero")

#main tkinter input
window = tk.Tk()
window.title("Basic Arithmetic Operations")

#create entry widgets for number input
entry_num1 = tk.Entry(window)
entry_num2 = tk.Entry(window)
entry_num1.grid(row=0, column=1)
entry_num2.grid(row=1, column=1)

#create lables for number input
label_num1 = tk.Label(window, text="Number 1:")
label_num2 = tk.Label(window, text="Number 2:")
label_num1.grid(row=0, column=0, padx=10, pady=10, sticky="e")
label_num2.grid(row=1, column=0, padx=10, pady=10, sticky="e")

#create a dropdown menu for selecting the arithmetic operation
operation_var = tk.StringVar()
operations = ["Addition", "Subtraction", "Multiplication", "Division", "Modulo Division"]
operation_dropdown = tk.OptionMenu(window, operation_var, *operations)
operation_dropdown.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
operation_var.set(operations[0])

#create a button to trigger the calculation
calculate_button = tk.Button(window, text="Calculate", command=perform_operation)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

#create a label to display the result
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
