class Oven:
    def __init__(self, model, max_temperature, modes):
        self.model = model
        self.max_temperature = max_temperature
        self.modes = modes
        self.plugged_in = True

    def switch_power(self):
        if self.plugged_in:
            self.plugged_in = False
            return 'Oven unplugged'
        else:
            self.plugged_in = True
            return 'Oven plugged in'

    def cook(self, mode, temperature, duration, *food_items):
        if mode not in self.modes:
            return 'No such mode available!'
        if not self.plugged_in:
            return 'Switch oven on first!'
        if not food_items:
            return 'Food item(s) required!'
        if temperature > self.max_temperature:
            return f'Maximum temperature of {self.max_temperature} degrees exceeded!'

        return f'Returning cooked {", ".join(food_items)}, cooked at {temperature} for {duration} minutes.'

    def __repr__(self):
        return f'This {self.model} oven has a maximum temperature of {self.max_temperature} degrees and the following modes: {", ".join(self.modes)}'


my_oven = Oven('Gorenje', 240, ['grill', 'light', 'grill & ventilator', 'microwave'])
print(my_oven.cook('grill', 180, 45, 'pork chops', 'onions', 'carrots'))
print(my_oven.switch_power())
print(my_oven.__repr__())
