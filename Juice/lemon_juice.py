from class_juice import Juice


class LemonJuice(Juice):
    def __init__(self, quantity, pulp):
        super().__init__(quantity, pulp)
        self.title = 'Lemon'
        self.taste = 'lemon'
        self.natural_color = 'yellow'

    def __str__(self):
        message = f'This {self.taste}" juice is {self.quantity}ml.'
        return message
