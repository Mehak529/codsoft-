Python 3.11.7 | packaged by Anaconda, Inc. | (main, Dec 15 2023, 18:05:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... def rock_paper_scissor():
...     user_count=0
...     computer_count=0
...     options = ["rock", "paper", "scissor"]
...     print("Welcome to Rock, Paper, Scissor!")
...     print("choose 'rock', 'paper', or 'scissor' to play. Type 'quit' to exit.")
... 
...     while True:
...         user_choice = input("Your choice: ").lower()
...         if user_choice == "quit":
...             print("Thanks for playing! Goodbye!")
...             break
...         elif user_choice not in options:
...             print("Incorrect choice. Please select 'rock', 'paper', or 'scissor'.")
...             continue
...         
...         computer_choice = random.choice(options)
...         print(f"Computer chose: {computer_choice}")
...         if user_choice == computer_choice:
...             print("It's a tie!")
...         elif (user_choice == "rock" and computer_choice == "scissor") or \
...              (user_choice == "scissor" and computer_choice == "paper") or \
...              (user_choice == "paper" and computer_choice == "rock"):
...             print("You win!")
...             user_count+=1
...         else:
...             print("You lose!, try again")
...             computer_count+=1
...         print("User:",user_count,"| Computer:",computer_count)
... 
