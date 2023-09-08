from class_guitar import Guitar


class ElectricGuitar(Guitar):
    STRING_BORDERS = [6, 9]

    def __init__(self, model, frets, battery, strings_qty):
        super().__init__(model, frets, battery, strings_qty)

    def determine_standard_tuning(self):
        if self.strings_qty == 6:
            return ['E', 'A', 'D', 'G', 'B', 'E']
        elif self.strings_qty == 7:
            return ['B', 'E', 'A', 'D', 'G', 'B', 'E']
        elif self.strings_qty == 8:
            return ['F#', 'B', 'E', 'A', 'D', 'G', 'B', 'E']
        elif self.strings_qty == 9:
            return ['C#', 'F#', 'B', 'E', 'A', 'D', 'G', 'B', 'E']

    def __repr__(self):
        return f'This electric guitar has {self.strings_qty} strings and {self.frets} frets.'


electric_guitar = ElectricGuitar('LTD', 24, None, 7)
print(electric_guitar.__repr__())
print(electric_guitar.display_tuning())
