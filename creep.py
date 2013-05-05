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

        self.position += displacement

        if self.position.x < boundsRect.left:
            self.position.x = boundsRect.left
            self.direction.x *= -1
        elif self.position.x > boundsRect.right:
            self.position.x = boundsRect.right
            self.direction.x *= -1
        elif self.position.y < boundsRect.top:
            self.position.y = boundsRect.top
            self.direction.y *= -1
        elif self.position.y > boundsRect.bottom:
            self.position.y = boundsRect.bottom
            self.direction.y *= -1



