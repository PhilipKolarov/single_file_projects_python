from class_juice import Juice


class AppleJuice(Juice):
    def __init__(self, quantity, pulp):
        super().__init__(quantity, False)
        self.title = 'Apple'
        self.taste = 'apple'

    def __str__(self):
        message = f'This {self.taste}" juice is {self.quantity}.'

