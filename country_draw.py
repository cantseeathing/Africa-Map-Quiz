from turtle import Turtle


class Draw(Turtle):
    def __init__(self):
        super(Draw, self).__init__()
        self.total_list = []

    def draw_country(self, x, y, name):
        self.penup()
        self.hideturtle()
        self.color('green')
        self.goto(x=x, y=y)
        self.write(f"{name}", True, align="center", font=('Arial', 10, 'normal'))
        self.total_list.append(self)
        return self.total_list
