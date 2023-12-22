import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "your_username" and password == "your_password":
        result_label.config(text="Login successful!", fg="green")
    else:
        result_label.config(text="Login failed. Please try again.", fg="red")

window = tk.Tk()
window.title("Login Page")

window.columnconfigure(1, weight=1)
window.rowconfigure(3, weight=1)

username_label = tk.Label(window, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
username_entry = tk.Entry(window)
username_entry.grid(row=1, column=1, padx=10, pady=10)

password_label = tk.Label(window, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
password_entry = tk.Entry(window, show="*") 
password_entry.grid(row=2, column=1, padx=10, pady=10)

login_button = tk.Button(window, text="Login", command=login)
login_button.grid(row=3, column=1, padx=10, pady=10)

result_label = tk.Label(window, text="", fg="black")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
