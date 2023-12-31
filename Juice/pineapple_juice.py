from class_juice import Juice


class PineappleJuice(Juice):
    def __init__(self, quantity, pulp):
        super().__init__(quantity, pulp)
        self.title = 'Pineapple'
        self.taste = 'pineapple'
        self.natural_color = 'yellow'

    def __str__(self):
        message = f'This {self.taste}" juice is {self.quantity}ml.'
        return message
