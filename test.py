import turtle
import time

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

segments= []
starting_positions = [(0,0),(-20,0), (-40,0)]

for position in starting_positions:
    segment1= turtle.Turtle("square")
    segment1.color("white")
    segment1.penup()
    segment1.goto(position)
    segments.append(segment1)

is_game_started = True
while is_game_started:
    for i in range(len(segments)-1,0,-1):
        nex_x = segments[i-1].xcor()
        nex_y = segments[i-1].ycor()
        segments[i].goto(nex_x, nex_y)
        
    segments[0].forward(20)
    screen.update()
    time.sleep(0.2)



screen.exitonclick()
