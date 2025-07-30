# from turtle import Turtle
# from turtle import *
# Alias Module name: import turtle as t
# turtle = t.Turtle()
'''
tim = Turtle()
tim.shape("turtle")
tim.color("red")
for i in range(4):
    tim.right(90)
    tim.forward(100)'''

'''import turtle as t
import random
tim = t.Turtle()'''
# for a dashed line
'''for i in range(50):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()'''
# For shapes from triangle to hexagon
'''for h in range(3):
    tim.right(120)
    tim.forward(100)
for i in range(4):
    tim.right(90)
    tim.forward(100)
for j in range(5):
    tim.right(72)
    tim.forward(100)
for k in range(6):
    tim.right(60)
    tim.forward(100)

or

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for j in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(j)'''

'''def random_color():
    r = random.randint(0, 255) / 255
    g = random.randint(0, 255) / 255
    b = random.randint(0, 255) / 255
    color = (r, g, b)
    return color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+10)

draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()'''

'''for i in range(200):
    tim.forward(30)
    tim.color(random_color())
    tim.setheading(random.choice(directions))'''


# Tuple = Can't change
'''import colorgram

rgb_colors = []
colors = colorgram.extract('Damian.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)'''
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()

tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (243, 227, 80), (160, 75, 43), (24, 30, 60), (214, 147, 91), (125, 160, 217), (55, 89, 144), (45, 37, 30), (41, 48, 114), (29, 44, 34), (147, 57, 81), (129, 32, 43), (202, 82, 121), (145, 31, 25), (214, 81, 54), (71, 31, 40), (68, 112, 77), (133, 181, 163), (95, 105, 199), (190, 141, 156), (72, 78, 41), (152, 207, 219), (96, 161, 82), (48, 87, 32), (158, 187, 232), (169, 162, 72), (145, 210, 190)]
dots_per_row = 10
spacing = 50
grid_width = dots_per_row * spacing
grid_height = dots_per_row * spacing

# Start from the top-left corner of the grid
start_x = -grid_width / 2
start_y = -grid_height / 2
tim.goto(start_x, start_y)


for i in range(dots_per_row):
    for j in range(dots_per_row):
        tim.dot(20, random.choice(color_list))
        tim.forward(spacing)

    tim.backward(spacing * dots_per_row)
    tim.left(90)
    tim.forward(spacing)
    tim.right(90)

screen = turtle_module.Screen()
screen.exitonclick()
