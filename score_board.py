from turtle import Turtle


class Score:
    def __init__(self, screen_size, length):
        self.content = None
        self.length = length
        try:
            with open("high_score.txt", mode='r') as file:
                self.content = file.read()
                file.close()
        except IOError:
            with open("high_score.txt", mode='w') as file:
                file.write(str(0))
                self.content = 0
                print("File created successfully")
        else:
            if self.content == '':
                file = open("high_score.txt", mode="w")
                self.content = 0
                file.write(str(self.content))
            else:
                self.high_score = self.content
            print(f"high score: {self.content}")
        self.high_score = int(self.content)
        self.game_over_banner = Turtle()
        self.game_over_banner.hideturtle()
        self.game_over_banner.penup()
        self.game_over_banner.color('red')
        self.level = 0
        self.screen_size = screen_size
        self.score_banner_object = Turtle()
        self.score_banner_object.color("green")
        self.score_banner_object.penup()
        self.score_banner_object.hideturtle()
        self.score_banner_object.goto(x=0, y=int((self.screen_size[1] / 2)))
        self.score_banner_object.write(f"Score: {self.level}/{self.length}", True, align="left",
                                       font=('Arial', 15, 'normal'))
        self.hs_banner_object = Turtle()
        self.hs_banner_object.color("red")
        self.hs_banner_object.penup()
        self.hs_banner_object.hideturtle()
        self.hs_banner_object.goto(x=0, y=int((self.screen_size[1] / -2)*1.1))
        self.hs_banner_object.write(f"Highest Score: {self.high_score}/{self.length}", True, align="left",
                                    font=('Arial', 15, 'normal'))

    def game_over(self):
        self.game_over_banner.write("Game Over!", True, align="center", font=('Arial', 15, 'bold'))
        if self.level > self.high_score:
            self.high_score = self.level
            self.record()
        self.level = 0

    def update_score(self):
        self.level += 1
        self.score_banner_object.clear()
        self.hs_banner_object.clear()
        if self.level > self.high_score:
            self.high_score = self.level
            self.record()
        self.score_banner_object.goto(x=0, y=int((self.screen_size[1] / 2)))
        self.score_banner_object.write(f"Score: {self.level}/{self.length}", True, align="left",
                                       font=('Arial', 15, 'normal'))
        self.hs_banner_object.goto(x=0, y=int((self.screen_size[1] / -2)*1.1))
        self.hs_banner_object.write(f"Highest Score: {self.high_score}/{self.length}", True, align="left",
                                    font=('Arial', 15, 'normal'))

    def record(self):
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))
            file.close()
