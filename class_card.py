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
        new_card_number = new_card.card_number()
        result = ''

        if self.card_suite == new_card_suite:
            result += f'Both cards are {new_card_suite}.\n'
        else:
            result += 'Cards are different suites.\n'

        if self.card_number > new_card_number:
            result += f'{self.__str__()} is greater than {new_card.__str__}.'
        elif self.card_number < new_card_number:
            result += f'{self.__str__()} is less than {new_card.__str__}.'
        elif self.card_number == new_card_number:
            result += 'Both cards are equal.'

    def __str__(self):
        return f'{self.title} of {self.suite}'
