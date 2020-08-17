import pygame
from glob import glob
import sys
from pygame.locals import *


pygame.init()
WINDOWWIDTH = w = 400
WINDOWHEIGHT = h = 400
screen = pygame.display.set_mode((w, h))


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Sprite, self).__init__()
        self.x = x
        self.y = y
        self.list = [
            pygame.image.load(f).convert_alpha() for f in glob("cat/Walk*.png")[1:]
        ]
        self.list_idle = [pygame.image.load(f).convert_alpha() for f in glob("cat/Idle*.png")[1:]]
        self.counter = 0
        self.image = self.list[0]
        self.rect = self.image.get_rect()
        self.dir = ""
        self.prov = ""
        g.add(self)

    # def update(self):
    #     self.counter += .1
    #     if self.counter >= len(self.list):
    #         self.counter = 0
    #     if moveRight:
    #         self.image = self.list[int(self.counter)]
    #         self.prov = self.dir
    #     if moveLeft:
    #         self.image = pygame.transform.flip(self.list[int(self.counter)], True, False)
    #         self.prov = self.dir
    #     if self.dir == "":
    #         if self.counter >= len(self.list_idle):
    #             self.counter = 0
    #         if self.prov == "right":
    #             self.image = self.list_idle[int(self.counter)]
    #         else:
    #             self.image = pygame.transform.flip(self.list_idle[int(self.counter)], True, False)

        #screen.blit(self.image, (self.x, self.y))

g = pygame.sprite.Group()
player = Sprite(100, 100)
clock = pygame.time.Clock()

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 1
while True:
# Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
                player.image = player.list[int(player.counter)]
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False

# Draw the white background onto the surface.
    screen.fill((255, 255, 255))

    # Move the player.
    if moveDown and player.rect.bottom < WINDOWHEIGHT:
        player.rect.top += MOVESPEED
    if moveUp and player.rect.top > 0:
        player.rect.top -= MOVESPEED
    if moveLeft and player.rect.left > -35:
        player.rect.left -= MOVESPEED
        try:
            player.counter += .1
            player.image = pygame.transform.flip(player.list[int(player.counter)], True, False)
        except:
            player.counter = 0
            player.image = pygame.transform.flip(player.list[int(player.counter)], True, False)
    if moveRight and player.rect.right < WINDOWWIDTH + 35:
        player.rect.right += MOVESPEED
        try:
            player.counter -= .1
            player.image = player.list[int(player.counter)]
        except:
            player.counter = 0
            player.image = player.list[int(player.counter)]

    # Draw the player onto the surface.
    g.draw(screen)
    g.update()
    # Draw the window onto the screen.
    pygame.display.update()
    clock.tick(120)

pygame.quit()