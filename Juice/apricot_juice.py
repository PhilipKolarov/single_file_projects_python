from class_juice import Juice


class ApricotJuice(Juice):
    def __init__(self, quantity, pulp):
        super().__init__(quantity, pulp)
        self.title = 'Apricot'
        self.taste = 'apricot'
        self.natural_color = 'dark yellow'
