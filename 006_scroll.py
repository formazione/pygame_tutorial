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

        # scroll
        self.map_pos = (0,0)
        self.moveBox = (100,100,300,300)
        
        self.dogwalking = glob("dog/Walk*.png")
        self.dogidling = glob("dog/Idle*.png")
        self.load_images()

    def load(self, x):
        return pygame.image.load(x).convert_alpha()

    def flip(self, x):
        return pygame.transform.flip(self.load(x), 1, 0)

    def load_images(self):
        self.list = [self.load(f) for f in self.dogwalking]
        self.listflip = [self.flip(f) for f in self.dogwalking]
        self.list_idle = [self.load(f) for f in self.dogidling]
        self.list_idleflip = [self.flip(f) for f in self.dogidling]
        self.counter = 0
        self.image = self.list[0]
        self.rect = self.image.get_rect()
        self.dir = ""
        self.prov = ""
        g.add(self)

    def update_counter(self, vel, img_list):
        self.counter += vel
        if self.counter >= len(img_list):
            self.counter = 0
        self.image = img_list[int(self.counter)]

    def update(self):
        if moveRight:
            self.update_counter(.1, self.list)
            self.prov = self.dir

        if moveLeft:
            self.update_counter(.1, self.listflip)
            # self.image = self.listflip[int(self.counter)]
            self.prov = self.dir

        if self.dir == "":
            self.update_counter(.1, self.list_idle)

            if moveRight:
                self.image = self.list_idle[int(self.counter)]

            else:
                self.image = self.list_idleflip[int(self.counter)]
        self.move_box()

    def move_box(self):
        # MOVE THE BOX
        mx,my = self.map_pos
        if self.rect.x <= self.moveBox[0]:
            self.rect.x += MOVESPEED
            mx += MOVESPEED
        elif self.rect.x >= self.moveBox[2]-32:
            self.rect.x -= MOVESPEED
            mx -= MOVESPEED
        if self.rect.y <= self.moveBox[1]:
            self.rect.y += MOVESPEED
            my += MOVESPEED
        elif self.rect.y >= self.moveBox[3]-32:
            self.rect.y -= MOVESPEED
            my -= MOVESPEED
        self.map_pos = (mx,my)

def create_surface(scene: list[str]) -> pygame.Surface:
    # the size of the Surface depends, on the columns and rows of the scene list of string
    map = pygame.Surface((len(scene[0])*64,len(scene)*64)) 
    x,y = 0,0
    for row in scene:
        for tile in row:
            # if tile in "-":
            #     pygame.draw.rect(map,(0,155,0),((x,y),(64,64)))
            if tile != " ":
                pygame.draw.rect(map,(125,125,125),((x,y),(64,64)))
            else:
                pygame.draw.rect(map,(255,128,122),((x,y),(64,64)))
            x += 64
        y += 64
        x = 0
    return map

scene = [
    "                       ",
    "                       ",
    "                       ",
    "                       ",
    "       ciao a tutti    ",
    "                       ",
    "                       ",
    "       X     X  X  X   ",
    "       X     X  X  X   ",
    "                       ",
    "                       ",
    "                       "]
    
# We will create a Surface (map) with the tiles
map = create_surface(scene)
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

        # KEYUP

        if event.type == KEYUP:
            player.counter = 0
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
    screen.blit(map, player.map_pos)
    g.draw(screen)
    g.update()
    # Draw the window onto the screen.
    pygame.display.update()
    clock.tick(120)

pygame.quit()