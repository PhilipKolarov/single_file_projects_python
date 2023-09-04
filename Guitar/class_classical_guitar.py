from class_guitar import Guitar


class ClassicalGuitar(Guitar):
    STRING_BORDERS = [6, 6]

    def __init__(self, model, frets, battery=None, strings_qty=6):
        super().__init__(model, frets, battery, strings_qty)

    def determine_standard_tuning(self):
        if self.strings_qty == 6:
            return ['E', 'A', 'D', 'G', 'B', 'E']

    def __repr__(self):
        return f'This classical guitar had {self.frets} frets.'


classical_guitar = ClassicalGuitar('Kremona', 22, None, 6)
print(classical_guitar.__repr__())
