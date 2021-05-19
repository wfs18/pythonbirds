"""
    >>> motor = Motor()
    >>> motor.velocity
    0
    >>> motor.speed_up()
    1
    >>> motor.stop()
    0
    >>> motor.speed_up()
    1
    >>> motor.speed_up()
    2
    >>> motor.stop()
    1
    >>> motor.stop()
    0
    >>> motor.stop()
    0
    >>> direction = Direction()
    >>> direction.right()
    'East'
    >>> direction.right()
    'South'
    >>> direction.right()
    'West'
    >>> direction.right()
    'North'
    >>> direction.left()
    'West'
    >>> direction.left()
    'South'
    >>> direction.left()
    'East'
    >>> direction.left()
    'North'
    >>> direction.left()
    'West'
"""


class Car:
    def __init__(self, motor, direction):
        self.motor = motor
        self.direction = direction

    def speedometer(self):
        return self.motor.velocity

    def speed_up(self):
        return self.motor.speed_up()

    def stop(self):
        return self.motor.stop()

    def right(self):
        return self.direction.right_rotation

    def left(self):
        return self.direction.left_rotation


class Motor:
    def __init__(self):
        self.velocity = 0

    def speed_up(self):
        self.velocity += 1
        return self.velocity

    def stop(self):
        self.velocity -= 1
        self.velocity = max(0, self.velocity)
        return self.velocity


NORTH = 'North'
SOUTH = 'South'
EAST = 'East'
WEST = 'West'


class Direction:

    right_rotation = {
        NORTH:EAST, EAST:SOUTH, SOUTH: WEST, WEST:NORTH
    }
    left_rotation = {
        NORTH: WEST, WEST:SOUTH, SOUTH:EAST, EAST:NORTH
    }

    def __init__(self):
        self.value = 'North'

    def right(self):
        self.value = self.right_rotation[self.value]
        # if self.value == NORTH:
        #     self.value = EAST
        # elif self.value == EAST:
        #     self.value = SOUTH
        # elif self.value == SOUTH:
        #     self.value = WEST
        # elif self.value == WEST:
        #     self.value = NORTH
        return self.value

    def left(self):
        self.value = self.left_rotation[self.value]
        # if self.value == NORTH:
        #     self.value = WEST
        # elif self.value == WEST:
        #     self.value = SOUTH
        # elif self.value == SOUTH:
        #     self.value = EAST
        # elif self.value == EAST:
        #     self.value = NORTH
        return self.value
