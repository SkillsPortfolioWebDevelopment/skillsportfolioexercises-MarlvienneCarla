import tkinter as tk
from tkinter import simpledialog

class Animal:
    def __init__(self, animal_type, name, colour, age, weight, noise):
        self.type = animal_type
        self.name = name
        self.colour = colour
        self.age = age
        self.weight = weight
        self.noise = noise

    def say_hello(self):
        print(f"{self.type} {self.name} says: Hello!")

    def make_noise(self):
        print(f"{self.type} {self.name} makes noise: {self.noise}")

    def animal_details(self):
        return f"Type: {self.type}\nName: {self.name}\nColour: {self.colour}\nAge: {self.age}\nWeight: {self.weight}\nNoise: {self.noise}"

class AnimalGUI:
    def __init__(self, master):
        self.master = master
        master.title("Animal Details App")

        # Instantiate Dog and Cow objects
        self.dog = Animal("Dog", "Buddy", "Brown", 3, 15.0, "Woof!")
        self.cow = Animal("Cow", "Daisy", "White", 5, 800.0, "Moo!")

        # Buttons for each animal
        self.dog_button = tk.Button(master, text="Dog Details", command=self.show_dog_details)
        self.dog_button.grid(row=0, column=0, padx=10, pady=10)

        self.cow_button = tk.Button(master, text="Cow Details", command=self.show_cow_details)
        self.cow_button.grid(row=1, column=0, padx=10, pady=10)

        # Button to enter values for a new animal
        self.new_animal_button = tk.Button(master, text="Enter New Animal", command=self.enter_new_animal)
        self.new_animal_button.grid(row=2, column=0, padx=10, pady=10)

    def show_dog_details(self):
        # Invoke methods for the Dog object
        self.dog.say_hello()
        self.dog.make_noise()
        details = self.dog.animal_details()
        self.display_details(details)

    def show_cow_details(self):
        # Invoke methods for the Cow object
        self.cow.say_hello()
        self.cow.make_noise()
        details = self.cow.animal_details()
        self.display_details(details)

    def enter_new_animal(self):
        # Ask user to enter values for a new animal
        animal_type = simpledialog.askstring("Animal Type", "Enter animal type:")
        name = simpledialog.askstring("Animal Name", "Enter animal name:")
        colour = simpledialog.askstring("Animal Colour", "Enter animal colour:")
        age = simpledialog.askinteger("Animal Age", "Enter animal age:")
        weight = simpledialog.askfloat("Animal Weight", "Enter animal weight:")
        noise = simpledialog.askstring("Animal Noise", "Enter animal noise:")

        # Create a new Animal object with user-input values
        new_animal = Animal(animal_type, name, colour, age, weight, noise)

        # Display details for the new animal
        details = new_animal.animal_details()
        self.display_details(details)

    def display_details(self, details):
        # Display details in a new window
        details_window = tk.Toplevel(self.master)
        details_window.title("Animal Details")
        details_label = tk.Label(details_window, text=details)
        details_label.pack(padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = AnimalGUI(root)
    root.mainloop()
