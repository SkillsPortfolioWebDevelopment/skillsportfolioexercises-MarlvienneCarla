import tkinter as tk
from tkinter import messagebox
import random
import time

class WordGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Guessing Game")

        self.words = ["python", "java", "ruby", "javascript", "html", "css"]
        self.score = 0
        self.timer_seconds = 10
        self.current_word = ""

        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        # Score Label
        self.score_label = tk.Label(self.root, text="Score: 0", font=("Helvetica", 14))
        self.score_label.pack(pady=10)

        # Timer Label
        self.timer_label = tk.Label(self.root, text="Time left: 10", font=("Helvetica", 12))
        self.timer_label.pack()

        # Word Label
        self.word_label = tk.Label(self.root, text="", font=("Helvetica", 18, "bold"))
        self.word_label.pack(pady=20)

        # Entry for User's Guess
        self.guess_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.guess_entry.pack(pady=10)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_guess)
        self.submit_button.pack()

    def start_game(self):
        self.reset_timer()
        self.next_word()

    def next_word(self):
        self.current_word = random.choice(self.words)
        shuffled_word = self.shuffle_word(self.current_word)
        self.word_label.config(text=shuffled_word)

    def reset_timer(self):
        self.timer_seconds = 10
        self.update_timer()

    def update_timer(self):
        self.timer_label.config(text=f"Time left: {self.timer_seconds}")
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.end_round()

    def shuffle_word(self, word):
        word_list = list(word)
        random.shuffle(word_list)
        return "".join(word_list)

    def check_guess(self):
        user_guess = self.guess_entry.get().lower()

        if user_guess == self.current_word:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.next_word()
            self.reset_timer()
        else:
            messagebox.showinfo("Incorrect", "Try again!")

    def end_round(self):
        messagebox.showinfo("Time's Up", f"Round Over!\nYour Score: {self.score}")
        self.score = 0
        self.score_label.config(text="Score: 0")
        self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    app = WordGuessingGame(root)
    root.mainloop()
