from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", "r") as file:
            tempscore = int(file.read())
            self.highscore = tempscore
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_score()
        self.hideturtle()
    
    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.highscore}", align="center", font=("Arial", 24, "normal"))

    def gameover(self):
        self.goto(0,0)
        self.color("#FF4B2B")
        self.write(f"Game Over!", align = "center", font= ("Arial", 24, "normal"))

    def resetscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update_score()

    
    