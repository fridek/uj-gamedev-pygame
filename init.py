__author__ = 'Sebastian Poreba (sebastian@smashinglabs.pl)'

import pygame
import sys, os, math

sys.path.append('./third_party')

from pygame.locals import *
from random import randint, choice
from vec2d import vec2d

from player import Player
from creep import Creep
from board import Board

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
N_CREEPS = 20
PLAYER_SPEED = 3 # px per frame

pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('aMAZEing game')
screen = pygame.display.get_surface()

clock = pygame.time.Clock()

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

images = [
    pygame.image.load('assets/pinkcreep.png').convert_alpha(),
    pygame.image.load('assets/graycreep.png').convert_alpha()
]
boardTile = pygame.image.load('assets/brick_tile.png').convert_alpha()

# list of all displayable items
# Array<Item>
items = []

for i in range(N_CREEPS):
    items.append(Creep(vec2d(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)),
                        vec2d(choice([-1, 1]), choice([-1, 1])),
                        0.1,
                        choice(images)))

playerImage = pygame.image.load('assets/bluecreep.png').convert_alpha()
player = Player(vec2d(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)),
                   vec2d(choice([-1, 1]), choice([-1, 1])),
                   0.1,
                   playerImage)

board = Board()

def drawBoard():
    img_rect = boardTile.get_rect()

    nrows = int(screen.get_height() / img_rect.height) + 1
    ncols = int(screen.get_width() / img_rect.width) + 1

    for y in range(nrows):
        for x in range(ncols):
            if (board.isWall(x, y)):
                img_rect.topleft = (x * img_rect.width, y * img_rect.height)
                screen.blit(boardTile, img_rect)

def itemTick(item, timeDelta):
    """
    @param {Item} item
    """
    image = pygame.transform.rotate(
        item.image, -item.direction.angle)
    imageWidth, imageHeight = image.get_size()

    draw_pos = image.get_rect().move(
        item.position.x - imageWidth / 2,
        item.position.y - imageHeight / 2)
    screen.blit(image, draw_pos)

    boundsRect = screen.get_rect().inflate(
        -imageWidth, -imageHeight)
    item.move(timeDelta, boundsRect)


def input(events):
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit(0)
        # else:
        #     print(event)

    # keyboard polling
    key = pygame.key.get_pressed()
    if key[K_RIGHT]:
        if player.position.x < SCREEN_WIDTH - PLAYER_SPEED:
            player.position.x += PLAYER_SPEED
    if key[K_LEFT]:
        if player.position.x > PLAYER_SPEED:
            player.position.x -= PLAYER_SPEED
    if key[K_DOWN]:
        if player.position.y < SCREEN_HEIGHT - PLAYER_SPEED:
            player.position.y += PLAYER_SPEED
    if key[K_UP]:
        if player.position.y > PLAYER_SPEED:
            player.position.y -= PLAYER_SPEED
    if key[K_a]:
        for item in items:
            board.collides(item)

    # player should look at the mouse
    mousePos = vec2d(pygame.mouse.get_pos())
    player.direction.angle = (mousePos - player.position).angle



while True:
    timeDelta = clock.tick(50)
    input(pygame.event.get())

    screen.blit(background, (0, 0))
    drawBoard()

    for item in items:
        itemTick(item, timeDelta)

    itemTick(player, timeDelta)

    pygame.display.flip()
