import pygame
from glob import glob
import sys


pygame.init()
screen = pygame.display.set_mode((400, 600))


class Cat:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.list = [
            pygame.image.load(f).convert_alpha() for f in glob("cat/Idle*.png")[1:]
        ]
        self.counter = 0
        self.image = self.list[0]
        self.dir = "right"

    def update(self):
        self.counter += .4
        if self.counter >= len(self.list):
            self.counter = 0
        if self.dir == "right":
            self.image = self.list[int(self.counter)]
        if self.dir == "left":
            self.image = pygame.transform.flip(self.list[int(self.counter)], True, False)        
        screen.blit(self.image, (self.x, self.y))

cat = Cat(100, 100)
clock = pygame.time.Clock()

while True:
    screen.fill((128, 255, 128))
    if pygame.event.get(pygame.QUIT):
        break
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_RIGHT:
                cat.dir = "right"
                cat.x += 10
            if event.key == pygame.K_LEFT:
                cat.dir = "left"
                cat.x -= 10
            if event.key == pygame.K_UP:
                cat.y -= 10
            if event.key == pygame.K_DOWN:
                cat.y += 10
    cat.update()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
