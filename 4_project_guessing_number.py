# import random
# import re
# print("Would you like to generate a random number within a range, or just any random number?")
# print("1. Random number within a range")
# print("2. Just a random number")
# choice = int(input("Enter your choice (1 or 2): "))
# if choice == 1:
#     while True:
#         try:
#             lower_bound = int(input("Enter the lower bound: "))
#             upper_bound = int(input("Enter the upper bound: "))
#             if lower_bound <= 0 or upper_bound <= 0:
#                 print("Please enter positive numbers for both bounds.")
#             elif lower_bound >= upper_bound:
#                 print("Lower bound should be less than upper bound. Please try again.")
#             else:
#                 break
#         except ValueError:
#             print("Invalid input. Please enter numeric values.")
#     random_number = random.randint(lower_bound, upper_bound)    
# else:
#     random_number = random.randint(1, 100)
# print("Random number generated. Try to guess it!")
# attempts = 0
# while True:
#     guess = input("Enter your guess: ")
#     if not re.match("^[0-9]*$", guess):
#         print("Please enter a valid number.")
#         continue
#     guess = int(guess)
#     attempts += 1
#     if guess<=random_number-5 or guess>=random_number+5:
#         print("You're very close!")
#     elif guess < random_number:
#         print("Too low! Try again.")
#     elif guess > random_number:
#         print("Too high! Try again.")
#     else:
#         print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
#         if attempts <= 3:
#             print("Amazing! You guessed it in just a few attempts!")
#         elif attempts <= 5:
#             print("Great job! You guessed it in a reasonable number of attempts.")
#         else:
#             print("Good effort! With a bit more practice, you'll guess it faster next time.")
#         break

import tkinter as tk
from tkinter import messagebox
import random
import re

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.choice = tk.IntVar()
        self.attempts = 0
        self.random_number = None

        self.create_choice_screen()

    def create_choice_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Would you like to generate a random number within a range or use 1-100?").pack(pady=10)
        tk.Radiobutton(self.master, text="1. Within a range", variable=self.choice, value=1).pack()
        tk.Radiobutton(self.master, text="2. Default (1–100)", variable=self.choice, value=2).pack()
        tk.Button(self.master, text="Next", command=self.process_choice).pack(pady=10)

    def process_choice(self):
        choice = self.choice.get()
        if choice == 1:
            self.create_range_input_screen()
        elif choice == 2:
            self.random_number = random.randint(1, 100)
            self.create_guess_screen()
        else:
            messagebox.showerror("Error", "Please select a choice.")

    def create_range_input_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Enter Lower Bound:").pack()
        self.lower_entry = tk.Entry(self.master)
        self.lower_entry.pack()

        tk.Label(self.master, text="Enter Upper Bound:").pack()
        self.upper_entry = tk.Entry(self.master)
        self.upper_entry.pack()

        tk.Button(self.master, text="Start Game", command=self.start_game_with_range).pack(pady=10)

    def start_game_with_range(self):
        try:
            lower = int(self.lower_entry.get())
            upper = int(self.upper_entry.get())
            if lower <= 0 or upper <= 0:
                raise ValueError("Positive numbers only.")
            if lower >= upper:
                raise ValueError("Lower bound must be less than upper bound.")
            self.random_number = random.randint(lower, upper)
            self.create_guess_screen()
        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))

    def create_guess_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Random number generated. Try to guess it!").pack(pady=10)
        self.guess_entry = tk.Entry(self.master)
        self.guess_entry.pack()
        tk.Button(self.master, text="Submit Guess", command=self.check_guess).pack(pady=5)
        self.feedback_label = tk.Label(self.master, text="")
        self.feedback_label.pack()

    def check_guess(self):
        guess = self.guess_entry.get()
        if not re.match("^[0-9]+$", guess):
            self.feedback_label.config(text="Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts += 1

        if abs(guess - self.random_number) <= 5 and guess != self.random_number:
            self.feedback_label.config(text="You're very close!")
        elif guess < self.random_number:
            self.feedback_label.config(text="Too low! Try again.")
        elif guess > self.random_number:
            self.feedback_label.config(text="Too high! Try again.")
        else:
            message = f"Congratulations! You guessed it in {self.attempts} attempts.\n"
            if self.attempts <= 3:
                message += "Amazing! You guessed it in just a few attempts!"
            elif self.attempts <= 5:
                message += "Great job! You guessed it in a reasonable number of attempts."
            else:
                message += "Good effort! With more practice, you'll get better!"
            messagebox.showinfo("Game Over", message)
            self.master.destroy()


# Launch the GUI app
if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGame(root)
    root.mainloop()
