class Card:
    NUMBER_DICT = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11,
                   'Queen': 12, 'King': 13, 'Ace': 14}

    def __init__(self, title, suite):
        self.number = self.determine_number(title)
        self.title = title
        self.suite = suite
        self.color = self.determine_color(suite)

    def determine_number(self, t):
        t_str = str(t)
        return self.NUMBER_DICT[t_str]

    @staticmethod
    def determine_color(suite):
        if suite == 'spades' or suite == 'clubs':
            return 'black'
        elif suite == 'hearts' or suite == 'diamonds':
            return 'red'

    @property
    def card_title(self):
        return self.title

    @property
    def card_suite(self):
        return self.suite

    @property
    def card_number(self):
        return self.number

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


card_a = Card(10, 'Spades')
print(card_a.card_number)
print(card_a.card_suite)
print(card_a.card_title)
print(card_a.__str__())

