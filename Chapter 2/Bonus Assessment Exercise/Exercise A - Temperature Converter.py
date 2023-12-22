import tkinter as tk

def convert_temperature():
    try:
        temperature = float(entry_temperature.get())
        if temperature_var.get() == "Celsius to Fahrenheit":
            result = (temperature * 9/5) + 32
            result_label. config(text=f"Result: {result:.2f} F")
        elif temperature_var.get() == "Fahrenheit to Celsius":
            result = (temperature - 32) * 5/9
            result_label.config(text=f"Result: {result:.2f} C")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

window = tk.Tk()
window.title("Temperature Converter")

entry_temperature = tk.Entry(window)
entry_temperature.grid(row=0, column=0, padx=10, pady=10)

temperature_var = tk.StringVar()
temperature_var.set("Celsius to Fahrenheit")
temperature_options = ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
temperature_dropdown = tk.OptionMenu(window, temperature_var, *temperature_options)
temperature_dropdown.grid(row=0, column=1, padx=10, pady=10)

convert_button = tk.Button(window, text="Convert", command=convert_temperature)
convert_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(window, text="Result: ")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()