class Oven:
    def __init__(self, model, max_temperature, modes):
        self.model = model
        self.max_temperature = max_temperature
        self.modes = modes
        self.plugged_in = True

    def switch_power(self):
        self.plugged_in = False

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

