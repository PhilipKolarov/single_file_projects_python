import time


class TrafficLights:
    ORDER = ['RED - Stop!', 'RED & YELLOW - Ready!', 'GREEN - Go!', 'YELLOW - Slow Down!']

    def __init__(self, red_time, switch_time, green_time):
        self.red_time = red_time
        self.switch_time = switch_time
        self.green_time = green_time
        self.activated = False

    def activate(self):
        self.activated = True
        while self.activated:
            print(self.ORDER[0])
            time.sleep(self._determine_sleep_length(self.ORDER[0]))
            self.ORDER = self.ORDER[1:] + [self.ORDER[0]]

    def deactivate(self):
        self.activated = False

    def _determine_sleep_length(self, current_state):
        if current_state == 'RED - Stop!':
            return self.red_time
        elif current_state == 'RED & YELLOW - Ready!' or current_state == 'YELLOW - Slow Down!':
            return self.switch_time
        elif current_state == 'GREEN - Go!':
            return self.green_time


lights = TrafficLights(10, 2.5, 5)
lights.activate()
lights.deactivate()
