class Card:
    def __init__(self, number, suite):
        self.number = number
        self.suite = suite
        self.color = self.determine_color(suite)

    @staticmethod
    def determine_color(suite):
        if suite == 'spades' or suite == 'clubs':
            return 'black'
        elif suite == 'hearts' or suite == 'diamonds':
            return 'red'

    @property
    def card_number(self):
        return self.number

    @property
    def card_suite(self):
        return self.suite

    def compare_with(self, new_card):
        new_card_suite = new_card.card_suite()
        result = ''

        if self.suite == new_card_suite:
            result += f'Both cards are {new_card_suite}.\n'
        else:
            result += 'Cards are different suites.\n'
