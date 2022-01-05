from turtle import Screen, Turtle

MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.facing = self.segments[0].heading()
        self.head = self.segments[0]

    def create_snake(self):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        self.segments.append(segment)
        for postition in range(0, 2):
            self.extend()

    def add_segment(self, pos):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(pos)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def crash(self):
        for seg in self.segments[1:]:
            if self.head.distance(seg) < 10:
                return True
        return False

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.facing == 0:
            self.segments[0].left(90)
        elif self.facing == 180:
            self.segments[0].right(90)
        self.facing = self.segments[0].heading()

    def down(self):
        if (self.facing == 0):
            self.segments[0].right(90)
        elif (self.facing == 180):
            self.segments[0].left(90)
        self.facing = self.segments[0].heading()

    def right(self):
        if (self.facing == 90):
            self.segments[0].right(90)
        elif (self.facing == 270):
            self.segments[0].left(90)
        self.facing = self.segments[0].heading()

    def left(self):
        if (self.facing == 90):
            self.segments[0].left(90)
        elif (self.facing == 270):
            self.segments[0].right(90)
        self.facing = self.segments[0].heading()
