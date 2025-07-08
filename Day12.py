# Day12
# Namespace: Local vs Global Scope
# Local scope meaning to create the variable inside the function
# Whereas global scope means that we create the variable outside the function
# Does Python has Block scope? No

import random 
# To check if the num is prime
def is_prime(num):
    import math
    prime = True
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            prime = False
            break
    return prime

# Python constants and global scope
# Values you define that never have to change
# Day 12 Project: The Number Guessing Game

EASY_LEVEL_TURNS = 11
HARD_LEVEL_TURNS = 6


def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too high")
    elif user_guess < actual_answer:
        print("Too low")
    else:
        print(f"You got it. The actual answer is {actual_answer}")

def set_difficulty():
    a = input("Choose a difficulty, 'easy' or 'hard': ")


    if a == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS




def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100")
    answer = random.randint(1, 100)
    print(f"psst: the correct answer is {answer}")
    turns = set_difficulty()

    guess = 0

    while guess != answer:
        turns -= 1
        print(f"You have {turns} turns remaining.")
        guess = int(input("Make a guess: "))
        if turns == 1:
            print("You ran out of guesses")
            break
        check_answer(guess, answer)
game()
