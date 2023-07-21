from class_juice import Juice


class PeachJuice(Juice):
    def __init__(self, quantity, pulp):
        super().__init__(quantity, pulp)
        self.title = 'Peach'
        self.taste = 'peach'
        self.natural_color = 'orange'

