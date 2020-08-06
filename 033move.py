import pygame
from glob import glob
import sys


pygame.init()
screen = pygame.display.set_mode((400, 600))


def debug(message="ended"):
    print("\n", message, "\n")
    pygame.quit()
    sys.exit()


class Cat:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # list of surfaces with all the images for the different animatios
        self.imagelist = [pygame.image.load(f).convert_alpha() for f in glob("cat/Idle*.png")[1:]]
        print(self.imagelist)
        # debug()
        # starting animation
        self.images_counter = 0
        self.image = self.imagelist[0]
        self.direct = "right"

    def update(self):
        self.images_counter += .4
        if self.images_counter >= len(self.imagelist):
            #debug(len(self.imagelist))
            self.images_counter = 0
        if self.direct == "right":
            self.image = self.imagelist[int(self.images_counter)]
            screen.blit(cat.image, (cat.x, cat.y))
        if self.direct == "left":
            self.image = self.imagelist[int(self.images_counter)]
            screen.blit(pygame.transform.flip(cat.image, True, False), (cat.x, cat.y))


cat = Cat(100, 100)
square = pygame.Surface((cat.image.get_size()))
square.fill((0, 180, 250))
sw, sh = screen.get_size()
clock = pygame.time.Clock()
while True:
    screen.fill((128, 255, 128))
    # screen.blit(pygame.transform.scale(cat, (sw, sh)),(0, 0))
    #screen.blit(square, (Cat.x, Cat.y))
    if pygame.event.get(pygame.QUIT):
        break
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                cat.direct = "right"
                cat.x += 10
            if event.key == pygame.K_LEFT:
                cat.direct = "left"
                cat.x -= 10
            if event.key == pygame.K_UP:
                cat.y -= 10
            if event.key == pygame.K_DOWN:
                cat.y += 10
    cat.update()


    pygame.display.update()
    clock.tick(60)


pygame.quit()