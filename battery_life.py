class Battery:
    def __init__(self, model, rate):
        self.model = model
        self.rate = rate
        self.power = 100

    def use_battery(self, seconds):
        used_power = self.rate * seconds
        if self.power > used_power:
            self.power -= used_power
            return f'{used_power:.2f} power used;\n{self.power:.2f} remaining'
        else:
            self.power = 0
            return 'Battery drained!'


my_battery = Battery('Duracell', 0.009)
print(my_battery.use_battery(300))
print(my_battery.use_battery(80000))
