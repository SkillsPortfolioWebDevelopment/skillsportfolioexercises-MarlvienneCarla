import tkinter as tk
from tkinter import scrolledtext, messagebox

class StringSearchApp:
    def __init__(self, master):
        self.master = master
        master.title("String Search App")

        # Text widget for displaying file content
        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.text_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Entry widget for free text search
        self.search_entry = tk.Entry(master, width=30)
        self.search_entry.grid(row=1, column=0, padx=10, pady=5)

        # Button for initiating the search
        self.search_button = tk.Button(master, text="Search", command=self.search_occurrences)
        self.search_button.grid(row=1, column=1, pady=5)

        # Load file content on app startup
        self.load_file_content()

    def load_file_content(self):
        try:
            with open("sentences.txt", "r") as file:
                content = file.read()
            self.text_area.insert(tk.END, content)
        except FileNotFoundError:
            messagebox.showwarning("File Not Found", "sentences.txt not found.")

    def search_occurrences(self):
        search_text = self.search_entry.get().strip()

        if not search_text:
            messagebox.showwarning("Empty Search", "Please enter a search term.")
            return

        try:
            with open("sentences.txt", "r") as file:
                content = file.read()

            occurrences = content.lower().count(search_text.lower())

            messagebox.showinfo("Search Result", f'The string "{search_text}" appears {occurrences} times.')
        except FileNotFoundError:
            messagebox.showwarning("File Not Found", "sentences.txt not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Error reading from file: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StringSearchApp(root)
    root.mainloop()