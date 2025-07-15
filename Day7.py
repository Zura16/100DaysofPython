# Day7
# Day7 Project: Hangman
import random

word_list = ["aardvark", "baboon", "camel"]
word = random.choice(word_list)
print(word)
blanks = len(word) * "_"
print(blanks)
'''or
place_holder = ""
for position in range(word_list):
    place_holder += "_"'''
j = 0
correct_letters = []
life = 6

while j in range(len(word)):
    j += 1
    display = ""
    letter = input("Guess a letter: ").lower()
    if letter in correct_letters:
        print("Who've already guessed this, try again!")
        j - 1

    for i in word:
        if i == letter:
            display += i
            correct_letters.append(i)

        elif i in correct_letters:
            display += i

        else:
            display += "_"

    print(display)

    if letter not in word:
        life -= 1
    if "_" not in display:
        print("You Won!")
        break
    if life < 1:
        print(f"You Lose! It was {word}!")
        break




total_letters = len(word)


import random
from dictionary import words
import check_input

def display_gallows(num_incorrect):
    pass  

def display_letters(letters):
    print(' '.join(letters))

def get_letters_remaining(incorrect, correct):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    remaining = [letter for letter in alphabet if letter not in incorrect and letter not in correct]
    return remaining

def main():
    play = True
    while play:
        word = random.choice(words).upper()
        correct_guesses = ['_'] * len(word)
        incorrect_guesses = []
        num_correct = 0
        num_incorrect = 0
        
        print("Welcome to Hangman!")
        
        while num_incorrect < 6:
            print("\nIncorrect guesses:")
            display_letters(incorrect_guesses)

            if num_incorrect == 0:
                print("========")
                print("||/   |")
                print("||")
                print("||")
                print("||")
                print("||")
                print("_ _ _ _ _")
            elif num_incorrect == 1:
                print("Incorrect! \n")
                print("========")
                print("||/   | ")
                print("||    o ")
                print("||")
                print("||")
                print("||")
            elif num_incorrect == 2:
                print("Incorrect! \n")
                print("========")
                print("||/   | ")
                print("||    o ")
                print("||    | ")
                print("||")
                print("||")
            elif num_incorrect == 3:
                print("Incorrect! \n")
                print("========")
                print("||/   | ")
                print("||    o ")
                print("||    | ")
                print("||   /  ")
                print("||")
            elif num_incorrect == 4:
                print("Incorrect! \n")
                print("========")
                print("||/   | ")
                print("||    o ")
                print("||    | ")
                print("||   / \ ")
                print("||")
            elif num_incorrect == 5:
                print("Incorrect! \n")
                print("========")
                print("||/   | ")
                print("||   \o ")
                print("||    | ")
                print("||   / \ ")
                print("||")
            
            print("\n")
            display_gallows(num_incorrect)
            print("\nCorrect guesses:")
            display_letters(correct_guesses)
            print("\n")
            print("Letters remaining:")
            display_letters(get_letters_remaining(incorrect_guesses, correct_guesses))
            print("\n")


            
            guess = input("Enter a letter: ").upper()
            if  guess.isalpha() == False:
                print("This is not a letter.")
                continue
                
            if len(guess) != 1:
                print("Please enter a single letter.")
                continue

            if guess in incorrect_guesses or guess in correct_guesses:
                print("You've already guessed that letter.")
                continue
            
            

            if guess in word:
                for i, letter in enumerate(word):
                    if letter == guess:
                        correct_guesses[i] = guess
                        print("Correct!")
                        num_correct += 1
                if num_correct == len(word):
                    print("\n You win!")
                    break
            else:
                if guess.isalpha() == False:
                    print()
                else: 
                    incorrect_guesses.append(guess)
                    num_incorrect += 1
        
        if num_incorrect == 6:
            print("Incorrect! \n")
            print("========")
            print("||/   | ")
            print("||   \o/ ")
            print("||    | ")
            print("||   / \ ")
            print("||")
            print("\nSorry, you loose...The word was:", word)
        
        play_input = check_input.get_yes_no("Play again (Y/N): ")
        if play_input != "Y":
            False
        

if __name__ == "__main__":
    main()