__author__ = 'Sebastian Poreba (sebastian@smashinglabs.pl)'

from actor import Actor

from vec2d import vec2d

class Creep(Actor):
    def __init__(self, initialPosition, initialDirection, speed, image):
        Actor.__init__(self, initialPosition, initialDirection, speed, image)

    def move(self, timeDelta, boundsRect):
        displacement = vec2d(
            self.direction.x * self.speed * timeDelta,
            self.direction.y * self.speed * timeDelta)

        self.previousPosition = self.position
        self.previousDirection = self.direction
        self.position += displacement

        if self.position.x < boundsRect.left or self.position.x > boundsRect.right:
            self.bounce(True, False)
        elif self.position.y < boundsRect.top or self.position.y > boundsRect.bottom:
            self.bounce(False, True)



