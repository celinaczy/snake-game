from turtle import Screen, Turtle

class Snake():

    def __init__(self):

        self.segments = []
        self.create_snake()

    def create_snake(self):
        x = 0
        y = 0
        for i in range(3):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.setposition(x, y)
            x -= 20
            self.segments.append(new_segment)

    def move(self, move_distance = 20):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)
