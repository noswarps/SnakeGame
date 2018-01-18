from Snake.color import Color
import random


class Food:

    def __init__(self, size=10, color=Color.red, screen_width=500, screen_height=500):
        self.width, self.height = size, size
        self.color = color
        self._sw, self._sh = screen_width, screen_height
        self.x = random.randint(0, self._sw // self.width - 1) * self.width
        self.y = random.randint(0, self._sh // self.height - 1) * self.height

    def move(self):
        self.x = random.randint(0, self._sw // self.width - 1) * self.width
        self.y = random.randint(0, self._sh // self.height - 1) * self.height

    @property
    def pos(self):
        return self.x, self.y

    @property
    def size(self):
        return self.width, self.height
