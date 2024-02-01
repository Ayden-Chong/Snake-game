import turtle
STARTING_POSITIONS = [(0,0),(-20,0), (-40,0), (-60,0),(-80,0),(-100,0)]

class Snake:
    def __init__(self):
        self.canmove = True
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.addsegment(position)

    def addsegment(self, position):
        segment1= turtle.Turtle("square")
        segment1.color("white")
        segment1.penup()
        segment1.goto(position)
        self.segments.append(segment1)

    def extend(self):
        self.addsegment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            nex_x = self.segments[i-1].xcor()
            nex_y = self.segments[i-1].ycor()
            self.segments[i].goto(nex_x, nex_y)
        
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270 and self.canmove == True:
            self.head.seth(90)
            self.canmove = False
    
    def down(self):
        if self.head.heading() != 90 and self.canmove == True:
            self.head.seth(270)
            self.canmove = False
    
    def left(self):
        if self.head.heading() != 0 and self.canmove == True:
            self.head.seth(180)
            self.canmove = False
    
    def right(self):
        if self.head.heading() != 180 and self.canmove == True:
            self.head.seth(0)
            self.canmove = False
    
    def reset(self):
        for i in self.segments:
            i.reset()
            i.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]