__author__ = 'Sebastian Poreba (sebastian@smashinglabs.pl)'

class Board(object):
    """Keeps information about surroundings - items and walls"""
    def __init__(self):
        self.walls_ = [[]]
        self.width = 0
        self.height = 0
        self.pxScale = 30

        self.readMapFile('assets/map1.txt')
        print(self.width, self.height)
        pass

    def collides(self, actor):
        actorX = actor.position.x
        actorY = actor.position.y


    def isWall(self, x, y):
        if x == 0 or y == 0:
            return True
        if y >= len(self.walls_) or x >= len(self.walls_[1]):
            return True
        return self.walls_[y][x]

    def readMapFile(self, filename):
        i = 1
        for line in open(filename):
            j = 1
            arr = [False]
            for c in line.strip():
                arr.append(c != ' ')
                j+=1
            self.walls_.append(arr)
            i+=1
        self.width = j-1
        self.height = i-1








