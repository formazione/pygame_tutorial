import pygame
import sys
import random
import os

pygame.init()

# Constants
WIDTH = 1000
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
FONT_SIZE = 50
FONT_COLOR = (255, 255, 255)
START_MESSAGE = "Press any key to start again"

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
font = pygame.font.Font(None, FONT_SIZE)

class Horse(pygame.sprite.Sprite):
    horses = pygame.sprite.Group()

    def __init__(self, horsename, x, y, color):
        super().__init__()
        self.horsename = horsename
        self.color = color
        self.image = pygame.image.load(os.path.join("img", f"{self.horsename}.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_x = x
        self.time = 0
        Horse.horses.add(self)

    def update(self):
        global game, run, winning_horse

        if game:
            if self.rect.x < 900:
                self.rect.x += random.randint(0, 4)
            else:
                game = False
                winning_horse = self.color
                print(f"{self.horsename} ({self.color}) wins!!!!")
        else:
            self.time += 1
            if self.time > 200:
                run = False

    @classmethod
    def reset_horses(cls):
        for horse in cls.horses:
            horse.rect.x = horse.start_x
            horse.time = 0

def display_winner(color):
    text = font.render(f"{color} horse wins!!!", True, FONT_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()

def display_start_message():
    text = font.render(START_MESSAGE, True, FONT_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 + 60))
    pygame.display.flip()

game = True
run = True
winning_horse = None

# Initialize horses
horse1 = Horse("horse1", 10, 100, "Brown")
horse2 = Horse("horse2", 10, 200, "red")
horse3 = Horse("horse3", 10, 300, "Blue")
horse4 = Horse("horse4", 10, 400, "Yellow")
horse5 = Horse("horse5", 10, 500, "Pink")

while run:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and not game:
            game = True
            Horse.reset_horses()

    if not game and winning_horse:
        display_winner(winning_horse)
        pygame.time.wait(10000)
        Horse.reset_horses()
        display_start_message()
        waiting_for_key = True
        while waiting_for_key:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    waiting_for_key = False
                if event.type == pygame.KEYDOWN:
                    waiting_for_key = False
                    game = True
                    winning_horse = None

    Horse.horses.update()
    Horse.horses.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
