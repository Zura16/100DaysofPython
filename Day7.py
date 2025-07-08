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