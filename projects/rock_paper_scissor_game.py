'''
Rock, Paper, Scissors Game in Python 🎮

💡 Game Rules:
Rock beats Scissors 🔹✂️ 
Scissors beat Paper ✂️📄
Paper beats Rock 📄🔹
If both choose the same, it's a draw.

'''
import random
import tkinter as tk
from tkinter import messagebox

# List of choices
choices = ["rock", "paper", "scissors"]

# Global variables to track scores
user_score = 0
computer_score = 0
rounds = 3  # Default is Best of 3
current_round = 1

# Function to determine the winner
def check_winner(user_choice):

    # use global as variables have global scope
    global user_score, computer_score, current_round
    
    # computer choice
    computer_choice = random.choice(choices)
    result_text.set(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        winner_text.set("It's a draw! 🤝")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        user_score += 1
        winner_text.set("You win! 🎉")
    else:
        computer_score += 1
        winner_text.set("Computer wins! 💻🏆")

    # Update Scores
    score_text.set(f"User: {user_score} | Computer: {computer_score}")

    # Check if game is over
    if current_round >= rounds:
        if user_score > computer_score:
            messagebox.showinfo("Game Over", "Congratulations! 🎉 You won the series!")
        elif user_score < computer_score:
            messagebox.showinfo("Game Over", "Computer won the series! 💻🏆 Better luck next time.")
        else:
            messagebox.showinfo("Game Over", "It's a tie series! 🤝")
        
        reset_game()  # Restart the game
    else:
        current_round += 1
        round_text.set(f"Round {current_round} of {rounds}")

# Function to reset the game
def reset_game():
    global user_score, computer_score, current_round
    user_score = 0
    computer_score = 0
    current_round = 1
    round_text.set(f"Round {current_round} of {rounds}")
    score_text.set("User: 0 | Computer: 0")
    result_text.set("Make your choice!")

# Function to set number of rounds
def set_rounds(value):
    global rounds
    rounds = int(value)
    reset_game()

# Creating GUI
root = tk.Tk()
root.title("Rock Paper Scissors 🎮")
root.geometry("400x400")

# UI Elements
round_text = tk.StringVar(value=f"Round {current_round} of {rounds}")
score_text = tk.StringVar(value="User: 0 | Computer: 0")
result_text = tk.StringVar(value="Make your choice!")
winner_text = tk.StringVar(value="")

tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(root, textvariable=round_text, font=("Arial", 12)).pack()
tk.Label(root, textvariable=score_text, font=("Arial", 12)).pack()
tk.Label(root, textvariable=result_text, font=("Arial", 12)).pack()
tk.Label(root, textvariable=winner_text, font=("Arial", 14, "bold"), fg="blue").pack(pady=5)

# Buttons for choices
tk.Button(root, text="Rock 🔹", font=("Arial", 12), command=lambda: check_winner("rock")).pack(pady=5)
tk.Button(root, text="Paper 📄", font=("Arial", 12), command=lambda: check_winner("paper")).pack(pady=5)
tk.Button(root, text="Scissors ✂️", font=("Arial", 12), command=lambda: check_winner("scissors")).pack(pady=5)

# Dropdown for round selection
tk.Label(root, text="Select Number of Rounds:", font=("Arial", 10)).pack(pady=5)
rounds_menu = tk.StringVar(value="3")
tk.OptionMenu(root, rounds_menu, "3", "5", "7", command=set_rounds).pack()

# Reset Button
tk.Button(root, text="Restart Game 🔄", font=("Arial", 12), command=reset_game).pack(pady=10)

# Run the application
root.mainloop()
