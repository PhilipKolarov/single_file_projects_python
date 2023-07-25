from class_juice import Juice


class AppleJuice(Juice):
    def __init__(self, quantity, color):
        super().__init__(quantity, False, color)
        self.title = 'Apple'
        self.taste = 'apple'
        self.natural_color = color
        self.density = 1.04

    def __str__(self):
        message = f'This {self.taste} juice is {self.quantity}ml.'
        return message

    def show_density(self):
        return self.density
