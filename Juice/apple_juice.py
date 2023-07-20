from class_juice import Juice


class AppleJuice(Juice):
    def __init__(self, quantity):
        super().__init__(quantity, False)
        self.title = 'Apple'
        self.taste = 'apple'

