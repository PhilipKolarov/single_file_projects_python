class Color:
    MAX_VALUE = 255
    MIN_VALUE = 0

    def __init__(self, red, green, blue):
        self.red = self._color_value_range_checker(red)
        self.green = self._color_value_range_checker(green)
        self.blue = self._color_value_range_checker(blue)

    def _color_value_range_checker(self, value):
        if self.MAX_VALUE >= value >= self.MIN_VALUE:
            return value

        raise ValueError(f'The value of all colors must be at least {self.MIN_VALUE} and at most {self.MAX_VALUE}!')

    def modify_red(self, value):
        self.red += value

    def modify_green(self, value):
        self.green += value

    def modify_blue(self, value):
        self.blue += value

    def __repr__(self):
        return f'Red: {self.red}; Green: {self.green}; Blue: {self.blue}.'


blue = Color(0, 0, 255)
red = Color(255, 0, 0)
green = Color(0, 255, 0)
yellow = Color(255, 255, 0)

