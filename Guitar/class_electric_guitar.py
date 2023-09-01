from class_guitar import Guitar


class ElectricGuitar(Guitar):
    def __init__(self, frets, battery, strings_qty):
        super().__init__(frets, battery, strings_qty)

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
