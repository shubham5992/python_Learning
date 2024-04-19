# This Python script is a simple number guessing game. It starts by generating a random number between 1 and 100 as the target. Then, it repeatedly asks the user to guess the number or type "Q" to quit.

# If the user guesses correctly, it prints "Success: Correct Guess" and ends the game. If the user's guess is too small, it prompts them to choose a bigger number. If the guess is too large, it prompts them to choose a smaller number.

# The game continues until the user guesses the correct number or chooses to quit by typing "Q". After the game ends, it prints "GAME OVER".



import random

target = random.randint(1,100)

while True:
    userChoice = input("Guess the Number or Quit(Q)") 
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess")
        break
    elif (userChoice < target):
        print("your number was too small. take a bigger number")
    else:
         print("your number was too big. take a smaller number")


print("-------GAME OVER--------")    
