import tkinter as tk
import datetime

def calculate_age():
    dob_str = entry_dob.get()

    try:
        dob_date = datetime.datetime.strptime(dob_str, "%m%d%Y")
        current_date = datetime.datetime.now()
        age = current_date.year - dob_date.year - ((current_date.month, current_date.day) < (dob_date.month, dob_date.day))
        result_label.config(text=f"Your age is {age} years")
    except ValueError:
        result_label.config(text="Invalid. Please use MM/DD/YYYY")

window = tk.Tk()
window.title("Age Calculator")

entry_dob = tk.Entry(window)
entry_dob.grid(row=0, column=0, padx=10, pady=10)

calculate_button = tk.Button(window, text="Calculate Age", command=calculate_age)
calculate_button.grid(row=1, column=0, padx=10, pady=10)

result_label = tk.Label(window, text="Calculate")
result_label.grid(row=2, column=0, padx=10, pady=10)

window.mainloop()