from turtle import Turtle, Screen
import pandas as pd


class MainScreen:
    def __init__(self, screen_size, background):
        self.answer = None
        self.background = background
        self.screen_size = screen_size
        self.screen = Screen()
        self.screen.title("Africa Map Quiz v1.0")
        self.screen.bgpic(background)
        self.screen.setup(width=self.screen_size[0], height=int(self.screen_size[1] * 1.2))

    def ask(self):
        return self.screen


class Data(MainScreen):
    def __init__(self, source, screen_size=None):
        super().__init__(self, screen_size)
        self.source = source
        screen_size = self.screen_size

    def data_base(self):
        data_base_object = pd.read_csv(self.source)
        return data_base_object, len(data_base_object)
