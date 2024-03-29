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
        self.idle = [pygame.image.load(f).convert_alpha() for f in glob(f"cat/Idle*.png")[1:]]
        self.walk = [pygame.image.load(f).convert_alpha() for f in glob(f"cat/Walk*.png")[1:]]
        self.imagelist = self.idle
        print(self.imagelist)
        # debug()
        # starting animation
        self.images_counter = 0
        self.image = self.imagelist[0]
        self.direct = ""
        self.store_direction = ""

    def update(self):
        self.images_counter += .4
        if self.images_counter >= len(self.imagelist):
            #debug(len(self.imagelist))
            self.images_counter = 0
        if self.direct == "right":
            self.imagelist = self.walk
            self.image = self.imagelist[int(self.images_counter)]
            self.store_direction = "right"
            screen.blit(cat.image, (cat.x, cat.y))
        elif self.direct == "left":
            self.imagelist = self.walk
            self.image = self.imagelist[int(self.images_counter)]
            screen.blit(pygame.transform.flip(cat.image, True, False), (cat.x, cat.y))
            self.store_direction = "left"
        else:
            self.imagelist = self.idle
            self.image = self.imagelist[int(self.images_counter)]
            if self.store_direction == "left":
                screen.blit(pygame.transform.flip(cat.image, True, False), (cat.x, cat.y))
            else:
                screen.blit(cat.image, (cat.x, cat.y))



cat = Cat(100, 100)
square = pygame.Surface((cat.image.get_size()))
square.fill((0, 180, 250))
sw, sh = screen.get_size()
clock = pygame.time.Clock()
while True:
    screen.fill((128, 255, 128))
    # screen.blit(pygame.transform.scale(cat, (sw, sh)),(0, 0))
    #screen.blit(square, (Cat.x, Cat.y))
    match cat.direct:
        case "right":
            cat.x += 2
        case "left":
            cat.x -= 2
    if pygame.event.get(pygame.QUIT):
        break
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                cat.direct = "right"

            if event.key == pygame.K_LEFT:
                cat.direct = "left"
            if event.key == pygame.K_UP:
                cat.y -= 10
            if event.key == pygame.K_DOWN:
                cat.y += 10
        if event.type == pygame.KEYUP:
            cat.direct = ""
    cat.update()


    pygame.display.update()
    clock.tick(60)


pygame.quit()