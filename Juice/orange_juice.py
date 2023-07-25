from class_juice import Juice


class OrangeJuice(Juice):
    def __init__(self, quantity, pulp):
        super().__init__(quantity, pulp)
        self.title = 'Orange'
        self.taste = 'orange'
        self.natural_color = 'orange'
        if self.pulp:
            self.density = 1.25
        else:
            self.density = 1.04

    def __str__(self):
        message = f'This {self.taste} juice is {self.quantity}ml.'
        return message

    @property
    def show_density(self):
        return self.density
