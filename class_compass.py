class Compass:
    MAX_DEGREES = 360

    def __init__(self, color):
        self.color = color
        self.current_degrees = 0

    def turn(self, degrees, direction):
        if direction == 'right' or direction == 'clockwise':
            self.current_degrees += degrees
        elif direction == 'left' or direction == 'anticlockwise':
            self.current_degrees = self.current_degrees - degrees
        else:
            return 'Direction not compatible! Must be one of the following: right, clockwise, left, anticlockwise.'

        self.current_degrees %= 360
        if self.current_degrees < 0:
            self.current_degrees = 360 - self.current_degrees
        return f'Compass turned successfully'

    def current_direction(self):
        if self.current_degrees < 22.5 or self.current_degrees >= 337.5:
            return 'North'
        elif 22.5 <= self.current_degrees < 67.5:
            return 'Northeast'
        elif 67.5 <= self.current_degrees < 112.5:
            return 'East'
        elif 112.5 <= self.current_degrees < 157.5:
            return 'Southeast'
        elif 157.5 <= self.current_degrees < 202.5:
            return 'South'
        elif 202.5 <= self.current_degrees < 247.5:
            return 'Southwest'
        elif 247.5 <= self.current_degrees < 292.5:
            return 'West'
        elif 292.5 <= self.current_degrees < 337.5:
            return 'Northwest'


my_compass = Compass('blue')
print(my_compass.current_direction())
print(my_compass.turn(50, 'right'))
print(my_compass.current_direction())
print(my_compass.turn(156, 'left'))
print(my_compass.current_direction())
