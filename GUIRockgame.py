import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        
        self.user_score = 0
        self.computer_score = 0
        
        # Set up the background color
        self.root.configure(bg='lightblue')
        
        # Create GUI components
        self.create_widgets()
    
    def create_widgets(self):
        # Title label
        self.title_label = tk.Label(self.root, text="Rock Paper Scissors Game", font=("Helvetica", 18, "bold"), bg='lightblue', fg='darkblue')
        self.title_label.pack(pady=10)

        # Score labels
        self.score_frame = tk.Frame(self.root, bg='lightblue')
        self.score_frame.pack(pady=5)

        self.user_score_label = tk.Label(self.score_frame, text="Your Score: 0", font=("Helvetica", 14), bg='lightblue', fg='green')
        self.user_score_label.pack(side=tk.LEFT, padx=20)

        self.computer_score_label = tk.Label(self.score_frame, text="Computer Score: 0", font=("Helvetica", 14), bg='lightblue', fg='red')
        self.computer_score_label.pack(side=tk.LEFT, padx=20)

        # Buttons for user choice
        self.button_frame = tk.Frame(self.root, bg='lightblue')
        self.button_frame.pack(pady=20)

        self.rock_button = tk.Button(self.button_frame, text="Rock", width=12, height=2, bg='grey', fg='white', font=("Helvetica", 12), command=lambda: self.user_choice('Rock'))
        self.rock_button.grid(row=0, column=0, padx=15)

        self.paper_button = tk.Button(self.button_frame, text="Paper", width=12, height=2, bg='lightgrey', fg='black', font=("Helvetica", 12), command=lambda: self.user_choice('Paper'))
        self.paper_button.grid(row=0, column=1, padx=15)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", width=12, height=2, bg='lightgreen', fg='black', font=("Helvetica", 12), command=lambda: self.user_choice('Scissors'))
        self.scissors_button.grid(row=0, column=2, padx=15)

        # Result and History
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg='lightblue', fg='darkblue')
        self.result_label.pack(pady=10)

        self.history_label = tk.Label(self.root, text="Game History:\n", font=("Helvetica", 12), bg='lightblue', fg='darkblue')
        self.history_label.pack(pady=5)

        # Restart button
        self.restart_button = tk.Button(self.root, text="Play Again", bg='lightcoral', fg='white', font=("Helvetica", 12), command=self.restart_game, state=tk.DISABLED)
        self.restart_button.pack(pady=10)
    
    def user_choice(self, choice):
        choices = ['Rock', 'Paper', 'Scissors']
        com_choice = random.choice(choices)
        
        # Determine the winner
        result = self.determine_winner(choice, com_choice)
        
        # Update scores
        self.update_scores(result)
        
        # Update history
        self.update_history(choice, com_choice, result)

        # Display the result
        self.result_label.config(text=f"Computer chose: {com_choice}\n{result}")
        self.restart_button.config(state=tk.NORMAL)
        
    def determine_winner(self, user, computer):
        if user == computer:
            return "It's a draw!"
        elif (user == 'Rock' and computer == 'Scissors') or \
             (user == 'Paper' and computer == 'Rock') or \
             (user == 'Scissors' and computer == 'Paper'):
            return "You win!"
        else:
            return "Computer wins!"
    
    def update_scores(self, result):
        if result == "You win!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1
        
        self.user_score_label.config(text=f"Your Score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

    def update_history(self, user, computer, result):
        history_text = self.history_label.cget("text")
        new_entry = f"You chose {user}, Computer chose {computer}: {result}\n"
        self.history_label.config(text=history_text + new_entry)

    def restart_game(self):
        self.result_label.config(text="")
        self.restart_button.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
game = RockPaperScissorsGame(root)

# Run the application
root.mainloop()
