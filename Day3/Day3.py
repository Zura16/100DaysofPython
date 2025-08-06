# Day3
'''# Conditional Statements, Logical Operators, Code Blocks and Scope
water_level = 50
if water_level > 80:
    print("Drain Water")
else:
    print("Continue")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("You do want to take a photo? Type  y for Yes and n for No ")
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is ${bill}")


else:
    print("Sorry you have to grow taller before you can ride")

print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? y or n: ")
extra_cheese = input("Do you want extra cheese on your pizza? y or n: ")

if size == "S":
    bill = 15
    if pepperoni == "y":
        bill += 2
    if extra_cheese == "y":
        bill += 1

elif size == "M":
    bill = 20
    if pepperoni == "y":
        bill += 3
    if extra_cheese == "y":
        bill += 1

else:
    bill = 25
    if pepperoni == "y":
        bill += 3
    if extra_cheese == "y":
        bill += 1

print(f"Your total bill is {bill}")

# Logical operators: 'AND', 'OR', 'NOT'
# if 45 <= age <= 55:'''

# Day3 Project: Treasure Island Game
print("Welcome to Treasure Island\nYour mission is to find the treasure.")
a = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' ")
if a == 'left':
    b = input("swim or wait? ")
    if b == "wait":
        c = input("Which door? Blue, Red or Yellow? ")
        if c == "Blue":
            print("Eaten by beasts.\nGame Over.")
        elif c == "Red":
            print("Burned by fire.\nGame Over")
        elif c == "Yellow":
            print("You Win!")
        else:
            print("Game Over")

    else:
        print("Attacked by trout.\nGame Over")

else:
    print("Fall into a hole.\nGame Over.")
