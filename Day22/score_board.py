from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.center = ""
        self.game_over = False
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(0, 200)
        self.write(self.center, align= "center", font=(("Courier", 80, "normal")))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def center_(self):
        self.center = "-"
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def check_game_over(self):
        if self.l_score >= 5:
            self.goto(0, 0)
            self.write("Left Player Wins!", align="center", font=("Courier", 40, "bold"))
            self.screen.exitonclick()
            self.screen.bye()
            self.game_over = True
        elif self.r_score >= 5:
            self.goto(0, 0)
            self.write("Right Player Wins!", align="center", font=("Courier", 40, "bold"))
            self.screen.exitonclick()
            self.screen.bye()
            self.game_over = True