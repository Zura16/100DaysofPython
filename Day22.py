from turtle import Screen, Turtle
from paddle import tim
from ball import Ball
import time
from score_board import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_tim = tim((350, 0))
l_tim = tim((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_tim.go_up, "Up")
screen.onkey(r_tim.go_down, "Down")
screen.onkey(l_tim.go_up, "w")
screen.onkey(l_tim.go_down, "s")


while not scoreboard.game_over:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_tim) < 50 and ball.xcor()>320 or ball.distance(l_tim) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    

screen.exitonclick()