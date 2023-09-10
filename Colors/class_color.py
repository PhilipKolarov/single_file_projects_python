from abc import ABC, abstractmethod


class Color(ABC):
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        pass
