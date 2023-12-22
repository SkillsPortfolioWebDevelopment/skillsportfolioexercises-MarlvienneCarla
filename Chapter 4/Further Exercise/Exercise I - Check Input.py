import tkinter as tk
from tkinter import messagebox
import re

class RegexCheckerApp:
    def __init__(self, master):
        self.master = master
        master.title("Regex Checker App")

        #entry widget for user input
        self.input_entry = tk.Entry(master)
        self.input_entry.grid(row=0, column=0, padx=10, pady=10)

        #button to check uppercase, lowercase, numbers, and underscores
        self.btn_check_alphanumeric = tk.Button(master, text="Check Alphanumeric", command=self.check_alphanumeric)
        self.btn_check_alphanumeric.grid(row=1, column=0, pady=5)

        #button to check if the string starts with a specific number
        self.btn_check_start_with_number = tk.Button(master, text="Check Start with Number", command=self.check_start_with_number)
        self.btn_check_start_with_number.grid(row=2, column=0, pady=5)

        #button to find substrings within the string
        self.btn_find_substring = tk.Button(master, text="Find Substring", command=self.find_substring)
        self.btn_find_substring.grid(row=3, column=0, pady=5)

        #button to match a word at the beginning of a string
        self.btn_match_word_at_beginning = tk.Button(master, text="Match Word at Beginning", command=self.match_word_at_beginning)
        self.btn_match_word_at_beginning.grid(row=4, column=0, pady=5)

    def check_alphanumeric(self):
        input_text = self.input_entry.get()
        #regular expression to match a string with only upper and lowercase letters, numbers, and underscores
        pattern = re.compile(r'^[a-zA-Z0-9_]+$')

        if pattern.match(input_text):
            messagebox.showinfo("Result", "String matches the pattern!")
        else:
            messagebox.showerror("Result", "String does not match the pattern.")

    def check_start_with_number(self):
        input_text = self.input_entry.get()
        #regular expression to match a string that starts with a specific number (e.g., 5)
        pattern = re.compile(r'^5.*')

        if pattern.match(input_text):
            messagebox.showinfo("Result", "String starts with the specified number!")
        else:
            messagebox.showerror("Result", "String does not start with the specified number.")

    def find_substring(self):
        input_text = self.input_entry.get()
        #regular expression to find substrings within the string (e.g., find 'abc')
        pattern = re.compile(r'abc')

        matches = pattern.findall(input_text)
        if matches:
            messagebox.showinfo("Result", f"Substrings found: {', '.join(matches)}")
        else:
            messagebox.showinfo("Result", "No substrings found.")

    def match_word_at_beginning(self):
        input_text = self.input_entry.get()
        #regular expression to match a word at the beginning of a string (e.g., 'apple')
        pattern = re.compile(r'^apple')

        if pattern.match(input_text):
            messagebox.showinfo("Result", "Word matches at the beginning of the string!")
        else:
            messagebox.showerror("Result", "Word does not match at the beginning of the string.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RegexCheckerApp(root)
    root.mainloop()
