import tkinter as tk
from tkinter import scrolledtext, messagebox

class NumbersListApp:
    def __init__(self, master):
        self.master = master
        master.title("Numbers List App")

        # Text widget for displaying the list of numbers
        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=20, height=10)
        self.text_area.grid(row=0, column=0, padx=10, pady=10)

        # Button for reading and displaying numbers
        self.read_button = tk.Button(master, text="Read Numbers", command=self.read_numbers)
        self.read_button.grid(row=1, column=0, pady=5)

    def read_numbers(self):
        try:
            with open("numbers.txt", "r") as file:
                numbers = [int(line.strip()) for line in file]

            # Display the numbers in the text area
            self.text_area.delete(1.0, tk.END)  # Clear previous content
            for number in numbers:
                self.text_area.insert(tk.END, f"{number}\n")
        except FileNotFoundError:
            messagebox.showwarning("File Not Found", "numbers.txt not found.")
        except ValueError:
            messagebox.showerror("Invalid Data", "File contains non-integer data.")
        except Exception as e:
            messagebox.showerror("Error", f"Error reading from file: {str(e)}")

if __name__ == "Reading to a List":
    root = tk.Tk()
    app = NumbersListApp(root)
    root.mainloop()