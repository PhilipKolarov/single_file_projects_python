from class_juice import Juice


class OrangeJuice(Juice):
    def __init__(self, quantity, pulp):
        super().__init__(quantity, pulp)
        self.title = 'Orange'
        self.taste = 'orange'
        self.natural_color = 'orange'

