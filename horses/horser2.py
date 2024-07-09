import pygame
import sys
import random
import os

pygame.init()

# Constants
WIDTH = 1000
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

class Horse(pygame.sprite.Sprite):
    horses = pygame.sprite.Group()

    def __init__(self, horsename, x, y):
        super().__init__()
        self.horsename = horsename
        self.image = pygame.image.load(os.path.join("img", f"{self.horsename}.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.time = 0
        Horse.horses.add(self)

    def update(self):
        global game, run

        if game:
            if self.rect.x < 900:
                self.rect.x += random.randint(0, 4)
            else:
                game = False
                print(f"{self.horsename} wins!!!!")
        else:
            self.time += 1
            if self.time > 200:
                run = False

game = True

horse1 = Horse("horse1", 10, 100)
horse2 = Horse("horse2", 10, 200)
horse3 = Horse("horse3", 10, 300)
horse4 = Horse("horse4", 10, 400)
horse5 = Horse("horse5", 10, 500)

run = True
while run:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    Horse.horses.update()
    Horse.horses.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
