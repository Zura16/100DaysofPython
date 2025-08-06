# Day5
'''fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
print(fruits)

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]
total_score = sum(student_scores)
print(total_score)

sum = 0
for score in student_scores:
    sum += score

print(sum)

print(max(student_scores))

maxi = 0
for score in student_scores:
    if score > maxi:
        maxi = score
print(maxi)

# for defining a number in a range
for number in range(1, 11, 2):
    print(number)
# To add the number from 1-100
x = 0
for no in range(1, 101):
    x += no
print(x)


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue

    print(i)'''

# Day5 Project: PyPassword Generator
import random

print("Welcome to the PyPassword Generator!")
a = int(input("How many letters would you like in your password? "))
b = int(input("How many symbols would you like? "))
c = int(input("How many numbers would you like? "))
l = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
s = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
n = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
d = a + b + c

password_list = []
for char in range(0, a):
    password_list.append(random.choice(l))
for char in range(0, b):
    password_list.append(random.choice(s))
for char in range(0, c):
    password_list.append(random.choice(n))

print(password_list)
random.shuffle(password_list)
print(password_list)


password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
