__author__ = 'Sebastian Poreba (sebastian@smashinglabs.pl)'

class Actor(object):
    """Movable actor for both player and CPU characters"""
    def __init__(self, initialPosition, initialDirection, speed, image):
        self.position = initialPosition

        self.direction = initialDirection

        self.image = image

        self.speed = speed

        self.radius = 12
