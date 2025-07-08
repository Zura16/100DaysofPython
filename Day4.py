# Day4
# Randomization

'''import random
import my_module
# For random integer and making your own module
random_integer = random.randint(1, 10)
print(random_integer)
print(my_module.my_favorite_number)
# For random float generation
random_no_0_to_1 = random.random()
print(random_no_0_to_1)
random_float = random.uniform(1, 10)
print(random_float)

a = random.randint(1, 2)
if a == 1:
    print("Heads")
else:
    print("Tails")

# Lists
fruits = ["apple", "mango"]
states_of_America = ["Delaware", "Pennsylvania"]
print(states_of_America[0])

import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#random_name = random.choice(friends)
random_name = random.randint(0, 4)
print(friends[random_name])'''

import random

# Day4 Project: Rock, Paper, Scissors game
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors ")
a = int(input())
if a == 0:
    print("Rock")
elif a == 1:
    print("Paper")
elif a == 2:
    print("Scissors")
else:
    print("Type a number from 0-2")

b = random.randint(0, 2)
print(f"computer: {b}")
if a == b:
    print("You are tied, try again!")
elif a == 0 and b == 1:
    print("You lose!")
elif a == 0 and b == 2:
    print("You Win!")
elif a == 1 and b == 2:
    print("You lose!")
elif a == 1 and b == 0:
    print("You Win!")
elif a == 2 and b == 0:
    print("You lose!")
elif a == 2 and b == 1:
    print("You Win!")
else:
    print("Try again!")

# Or
import random

a = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
b = random.randint(0, 2)
print(f"Computer chose {b}")

if a == 0 and b == 2:
    print("You win!")
elif b == 0 and a == 2:
    print("You lose!")
elif b > a:
    print("You lose!")
elif b == a:
    print("Draw!")
elif a > b:
    print("You win!")
else:
    print("Type a valid number or you lose")


