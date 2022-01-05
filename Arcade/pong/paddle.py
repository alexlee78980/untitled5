from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos):
        self.y_pos = 0
        self.x_pos = x_pos
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.color("white")
        self.update_paddle()

    def go_up(self):
        if (self.y_pos < 250):
            self.y_pos += 20
            self.update_paddle()

    def go_down(self):
        if (self.y_pos > -250):
            self.y_pos -= 20
            self.update_paddle()

    def update_paddle(self):
        self.setposition(self.x_pos, self.y_pos)
