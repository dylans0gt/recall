import os
import time
import random
import pyfiglet
from termcolor import colored

banner = pyfiglet.figlet_format("Recall", font="Speed")
color_banner = colored(banner, color="cyan")
print(color_banner)
print("Memory game.")

score = 0
wrong_guesses = 0
digits = 5

print(f"You have 2 seconds to memorize a {digits}-digit number.")

while wrong_guesses < 5:
    random_number = str(random.randint(0, 10**digits-1)).zfill(digits)
    
    print(" ")
    print(pyfiglet.figlet_format(random_number, font="Digital"))
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    user_guess = input("Please type in the number you just saw: ")

    if user_guess == random_number:
        print("Congratulations! You got it right.")
        score += 3
        wrong_guesses = 0
    else:
        print(f"Sorry, that was not correct. The number was {random_number}.")
        score -= 1
        wrong_guesses += 1
    
    if score % 12 == 0:
        digits += 1
        print(f"Congratulations! You reached {score} points and the number of digits has increased to {digits}.")
    
print(f"Game over. Your final score is {score}.")
