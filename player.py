__author__ = 'Sebastian Poreba (sebastian@smashinglabs.pl)'

from actor import Actor

class Player(Actor):
    """Movable actor for both player and CPU characters"""
    def __init__(self, initialPosition, initialDirection, speed, image):
        Actor.__init__(self, initialPosition, initialDirection, speed, image)

    def move(self, timeDelta, boundsRect):
        pass



