from class_guitar import Guitar


class AcousticGuitar(Guitar):
    STRING_BORDERS = [6, 8]

    def __init__(self, model, frets, battery, strings_qty=6):
        super().__init__(model, frets, battery, strings_qty)

    def determine_standard_tuning(self):
        if self.strings_qty == 6:
            return ['E', 'A', 'D', 'G', 'B', 'E']
        elif self.strings_qty == 7:
            return ['B', 'E', 'A', 'D', 'G', 'B', 'E']
        elif self.strings_qty == 8:
            return ['F#', 'B', 'E', 'A', 'D', 'G', 'B', 'E']

    def __repr__(self):
        return f'This acoustic guitar has {self.strings_qty} strings and {self.frets} frets.'
