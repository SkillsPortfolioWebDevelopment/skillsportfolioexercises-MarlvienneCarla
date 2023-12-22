import tkinter as tk
from tkinter import messagebox

class PasswordCheckerApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Checker App")

        #entry widget for password input
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.grid(row=0, column=0, padx=10, pady=10)

        #button to check the entered password
        self.check_button = tk.Button(master, text="Check Password", command=self.check_password)
        self.check_button.grid(row=1, column=0, pady=5)

        #initialize the number of attempts allowed
        self.attempts_remaining = 5

    def check_password(self):
        #get the entered password
        password = self.password_entry.get()

        #check if the password is valid
        if self.is_valid_password(password):
            messagebox.showinfo("Password Valid", "Password is valid!")
            self.master.destroy()
        else:
            #decrease the attempts remaining
            self.attempts_remaining -= 1

            #check if there are more attempts remaining
            if self.attempts_remaining > 0:
                #display an error message with the remaining attempts
                messagebox.showerror("Invalid Password", f"Invalid Password! Attempts remaining: {self.attempts_remaining}")
            else:
                #display a security alert if no attempts remaining
                messagebox.showerror("Security Alert", "Too many failed attempts.")
                self.master.destroy()

    def is_valid_password(self, password):
        #check if the password meets the specified criteria
        has_lowercase = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_uppercase = any(char.isupper() for char in password)
        has_special_char = any(char in "$#@!" for char in password)
        length_valid = 6 <= len(password) <= 12

        #return True if all criteria are met
        return has_lowercase and has_digit and has_uppercase and has_special_char and length_valid

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordCheckerApp(root)
    root.mainloop()
