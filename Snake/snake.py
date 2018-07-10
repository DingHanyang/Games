from Snake import constant


class Snake(object):
    def __init__(self):
        self.length = 1
        self.direction = constant.RIGHT

    def set_length(self, length):
        self.length = length

    def set_direction(self, direction):
        self.direction = direction
