# Day2
'''# Data types: 1. Strings and how to find a particular character
print("Hello"[0]) # Always start counting from 0
print("Hello"[-1]) # You can also use negative numbers

# Integer
print(123 + 345)

# Float: Numbers with decimal point
print(1.341)

# Boolean
print(True)
print(False)

# To check the data type
print(type("Hello"))
print(type(123))
print(type(1.23))
print(type(True))

# Conversion of types
# 123
print(int("123") + int("456"))

print("Number of letters in your name: " + str(len(input("Enter your name: "))))

# Mathematical Operations
print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(5 / 3)
print(5 // 3)
print(5 % 3)
print(2 ** 3)

# PEMDAS

# ()
# **
# * or /
# + or -

# Number manipulation
print(round(3.41))
print(round(2.3774652364827364, 3))

#
score = 0
score = score + 1
score += 1

# f-strings
print("your score is" + str(score))
score = 0
height = 1.8
is_winning = True
print(f"Your score is = {score}, your height is = {height}, You're winning is = {is_winning}")'''

# Day2 Project: Tip Calculator
print("Welcome to the tip calculator!")
a = float(input("What is the total bill? $"))
b = int(input("How much tip would you like to give? 10, 12 or 15%: " ))
c = int(input("How many people to split the bill? "))
final = (a + (a * b)/100) / c
print("Each person should pay $" + str(round(final, 2)))
