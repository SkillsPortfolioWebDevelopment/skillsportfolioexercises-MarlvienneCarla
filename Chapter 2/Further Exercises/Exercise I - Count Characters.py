import tkinter as tk

def count_characters():
    input_string = entry_string.get()
    input_string = input_string.lower()  # Convert the input to lowercase for case insensitivity
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    total_letters = len(input_string)
    num_vowels = sum(1 for char in input_string if char in vowels)
    num_consonants = sum(1 for char in input_string if char in consonants)
    num_special_chars = total_letters - num_vowels - num_consonants

    result_label.config(text=f"Total number of letters: {total_letters}\nNumber of vowels: {num_vowels}\nNumber of consonants: {num_consonants}\nNumber of special characters: {num_special_chars}")

# Create the main window
window = tk.Tk()
window.title("Character Counter")

# Create an entry widget for the user to enter a string
entry_string = tk.Entry(window)
entry_string.grid(row=0, column=0, padx=10, pady=10)

# Create a button to count characters
count_button = tk.Button(window, text="Count Characters", command=count_characters)
count_button.grid(row=1, column=0, padx=10, pady=10)

# Create a label to display the result
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.grid(row=2, column=0, padx=10, pady=10)

# Start the GUI main loop
window.mainloop()
