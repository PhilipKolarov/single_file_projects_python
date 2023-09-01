from class_guitar import Guitar


class ClassicalGuitar(Guitar):
    def __init__(self, frets, battery=None, strings_qty=6):
        super().__init__(frets, battery, strings_qty)

    def determine_standard_tuning(self):
        if self.strings_qty == 6:
            return ['E', 'A', 'D', 'G', 'B', 'E']

    def __repr__(self):
        return f'This classical guitar had {self.frets} frets.'
