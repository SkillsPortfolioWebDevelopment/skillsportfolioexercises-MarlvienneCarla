import tkinter as tk
from tkinter import messagebox

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    @classmethod
    def oldest_dog_woof(cls, dog1, dog2):
        oldest_dog = dog1 if dog1.age > dog2.age else dog2
        messagebox.showinfo("Woof!", f"The oldest dog, {oldest_dog.name}, says: Woof!")

class DogGUI:
    def __init__(self, master):
        self.master = master
        master.title("Dog Information App")

        # Create two Dog instances
        self.dog1 = Dog("Buddy", 5, "Labrador")
        self.dog2 = Dog("Max", 7, "German Shepherd")

        # Display Dog 1 information
        self.label_dog1 = tk.Label(master, text=f"Dog 1: {self.dog1.name}, {self.dog1.age} years old, {self.dog1.breed}")
        self.label_dog1.grid(row=0, column=0, padx=10, pady=10)

        # Display Dog 2 information
        self.label_dog2 = tk.Label(master, text=f"Dog 2: {self.dog2.name}, {self.dog2.age} years old, {self.dog2.breed}")
        self.label_dog2.grid(row=1, column=0, padx=10, pady=10)

        # Button to trigger oldest dog woof
        self.woof_button = tk.Button(master, text="Oldest Dog Woof", command=self.oldest_dog_woof)
        self.woof_button.grid(row=2, column=0, pady=10)

    def oldest_dog_woof(self):
        Dog.oldest_dog_woof(self.dog1, self.dog2)

if __name__ == "__main__":
    root = tk.Tk()
    app = DogGUI(root)
    root.mainloop()
