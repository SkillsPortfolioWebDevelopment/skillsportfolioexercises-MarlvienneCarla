import tkinter as tk
from tkinter import font

#fucntions to change the font style of the label
def change_font_style():
    #create a new fornt with specified family, size, and weight
    new_font = font.Font(family="Helvetica", size=16, weight="bold")
    #configure the label to use the new font
    label.config(font=new_font)

#create the main window
window = tk.Tk()
window.title("Welcome to My GUI Program")

#disable window resizing
window.geometry("400x200")

#set the backgroun color of the window
window.resizable(False, False)

#set the background color of the window
window.configure(bg="lightblue")

#create a label widget with specified text and font
label = tk.Label(window, text="Welcome to My GUI Program", font=("Arial", 20))
label.pack(pady=20)

#create a button widget to trigger font style change
font_button = tk.Button(window, text="Change Font Style", command=change_font_style)
font_button.pack()

window.mainloop()