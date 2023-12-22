import tkinter as tk
from tkinter import messagebox

class BioApp:
    def __init__(self, master):
        self.master = master
        master.title("Bio App")

        # Labels
        self.label_name = tk.Label(master, text="Name:")
        self.label_age = tk.Label(master, text="Age:")
        self.label_hometown = tk.Label(master, text="Hometown:")

        # Entry widgets
        self.entry_name = tk.Entry(master)
        self.entry_age = tk.Entry(master)
        self.entry_hometown = tk.Entry(master)

        # Buttons
        self.button_write = tk.Button(master, text="Write to File", command=self.write_to_file)
        self.button_read = tk.Button(master, text="Read from File", command=self.read_from_file)

        # Layout
        self.label_name.grid(row=0, column=0, sticky=tk.E)
        self.label_age.grid(row=1, column=0, sticky=tk.E)
        self.label_hometown.grid(row=2, column=0, sticky=tk.E)

        self.entry_name.grid(row=0, column=1)
        self.entry_age.grid(row=1, column=1)
        self.entry_hometown.grid(row=2, column=1)

        self.button_write.grid(row=3, column=0, columnspan=2, pady=10)
        self.button_read.grid(row=4, column=0, columnspan=2)

    def write_to_file(self):
        try:
            with open("bio.txt", "w") as file:
                name = self.entry_name.get()
                age = self.entry_age.get()
                hometown = self.entry_hometown.get()

                file.write(f"Name: {name}\nAge: {age}\nHometown: {hometown}")

            messagebox.showinfo("Success", "Data written to bio.txt successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error writing to file: {str(e)}")

    def read_from_file(self):
        try:
            with open("bio.txt", "r") as file:
                content = file.read()

            messagebox.showinfo("File Content", f"File Content:\n\n{content}")
        except FileNotFoundError:
            messagebox.showwarning("File Not Found", "bio.txt not found. Write to file first.")
        except Exception as e:
            messagebox.showerror("Error", f"Error reading from file: {str(e)}")

if __name__ == "User Information":
    root = tk.Tk()
    app = BioApp(root)
    root.mainloop()