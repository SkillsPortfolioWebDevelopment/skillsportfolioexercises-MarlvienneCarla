import tkinter as tk

def convert_to_uppercase():
    user_input = entry.get()
    uppercase_text = user_input.upper()
    result_label.config(text=f"Uppercase Text: {uppercase_text}")

# Create the main window
window = tk.Tk()
window.title("Uppercase Converter")

# Create an entry widget for user input
entry = tk.Entry(window)
entry.grid(row=0, column=0, padx=10, pady=10)

# Create a button to convert to uppercase
convert_button = tk.Button(window, text="Convert to Uppercase", command=convert_to_uppercase)
convert_button.grid(row=1, column=0, padx=10, pady=10)

# Create a label to display the result
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.grid(row=2, column=0, padx=10, pady=10)

# Start the GUI main loop
window.mainloop()
