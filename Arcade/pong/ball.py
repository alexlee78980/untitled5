from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.width = 20
        self.heigh = 20
        self.x_pos = 0
        self.y_pos = 0
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        self.x_pos += self.x_move
        self.y_pos += self.y_move
        self.goto(self.x_pos, self.y_pos)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def point(self):
        self.move_speed = 0.1
        self.x_pos = 0
        self.y_pos = 0
        self.bounce_x()
        self.goto(self.x_pos, self.y_pos)
