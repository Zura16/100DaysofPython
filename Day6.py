'''
# Day6
# Code Blocks and functions
# Functions

def my_func():
    print("Hello")
    print("Bye")

my_func()

# Reeborg's World: Hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    while not at_goal:
        if front_is_clear():
            turn_right()
        elif wall_in_front():
            turn_left()
            move()
            turn_right()

        else:
            front_is_clear
            turn_right()

        move()
        turn_right()
        move()

    # turn_left()


# for i in range(6):
#   jump()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        turn_right()
        if wall_in_front():
            turn_left()
            if wall_in_front():
                turn_left()

# Day6 Project: Reeborg's World Maze
# My Solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    while not at_goal:
        if front_is_clear():
            turn_right()
        elif wall_in_front():
            turn_left()
            move()
            turn_right()

        else:
            front_is_clear
            turn_right()

        move()
        turn_right()
        move()

    # turn_left()


# for i in range(6):
#   jump()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        turn_right()
        if wall_in_front():
            turn_left()
            if wall_in_front():
                turn_left()

# Professor's Solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal:
    if right_is_clear:
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
import random
'''