from class_juice import Juice


class PeachJuice(Juice):
    def __init__(self, quantity, pulp):
        super().__init__(quantity, pulp)
        self.title = 'Peach'
        self.taste = 'peach'
        self.natural_color = 'orange'

    def __str__(self):
        message = f'This {self.taste}" juice is {self.quantity}ml.'
        return message
