from abc import ABC, abstractmethod


class Color(ABC):
    MAX_VALUE = 255
    MIN_VALUE = 0

    def __init__(self, red, green, blue):
        self.red = self.color_value_range_checker(red)
        self.green = self.color_value_range_checker(green)
        self.blue = self.color_value_range_checker(blue)

    def color_value_range_checker(self, value):
        if self.MAX_VALUE >= value >= self.MIN_VALUE:
            return value

        raise ValueError(f'The value of all colors must be at least {self.MIN_VALUE} and at most {self.MAX_VALUE}!')

    def __repr__(self):
        pass
