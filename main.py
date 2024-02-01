import turtle
import time 
from snake import Snake
from food import Food
from score import Score

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snak = Snake()
fud = Food()
score= Score()

isgamestart = True
def quit():
    with open("highscore.txt") as file:
        prevhighscore = int(file.read())

    if (score.highscore > prevhighscore):
        with open("highscore.txt", "w") as file:
            file.write(str(score.highscore))
    global isgamestart
    isgamestart = False

screen.listen()
screen.onkey(snak.up, "Up")
screen.onkey(snak.down, "Down")
screen.onkey(snak.left, "Left")
screen.onkey(snak.right, "Right")
screen.onkey(quit, "q")

while isgamestart:
    snak.canmove = True
    snak.move()
    screen.update()
    time.sleep(0.15)

    if snak.head.distance(fud) < 15:
        fud.reposition()
        score.increase_score()
        snak.extend()

    for i in snak.segments[1:]:
        if snak.head.position() == i.position():
            score.resetscore()
            snak.reset()
            
    if snak.head.xcor() < -280:
        snak.head.setx(280)
    elif snak.head.xcor() > 280:
        snak.head.setx(-280)
    elif snak.head.ycor() < -280:
        snak.head.sety(280)
    elif snak.head.ycor() > 280:
        snak.head.sety(-280)
