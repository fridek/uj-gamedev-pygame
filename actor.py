__author__ = 'Sebastian Poreba (sebastian@smashinglabs.pl)'

class Actor(object):
    """Movable actor for both player and CPU characters"""
    def __init__(self, initialPosition, initialDirection, speed, image):
        self.position = initialPosition
        self.previousPosition = initialPosition

        self.direction = initialDirection
        self.previousDirection = initialDirection

        self.image = image

        self.speed = speed

        self.radius = 12

    def bounce(self, x, y):
        if x:
            self.direction.x = self.previousDirection.x * -1
        if y:
            self.direction.y = self.previousDirection.y * -1
        self.position = self.previousPosition
