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
FRAMES_PER_HORSE = 3  # Number of frames in your spritesheet
FRAME_WIDTH = 250
FRAME_HEIGHT = 172

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
font = pygame.font.Font(None, FONT_SIZE)

class Horse(pygame.sprite.Sprite):
    horses = pygame.sprite.Group()
    spritesheet = pygame.image.load(os.path.join("img", "horses.png"))

    def __init__(self, row, x, y, color):
        super().__init__()
        self.color = color
        self.frames = [self.spritesheet.subsurface(pygame.Rect(i * FRAME_WIDTH, row * FRAME_HEIGHT, FRAME_WIDTH, FRAME_HEIGHT)) for i in range(FRAMES_PER_HORSE)]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_x = x
        self.time = 0
        self.animation_counter = 0
        Horse.horses.add(self)

    def update(self):
        global game, run, winning_horse

        if game:
            if self.rect.x < 900:
                self.rect.x += random.randint(0, 4)
                self.animation_counter += 1
                if self.animation_counter % 5 == 0:
                    self.current_frame = (self.current_frame + 1) % FRAMES_PER_HORSE
                    self.image = self.frames[self.current_frame]
            else:
                game = False
                winning_horse = self
                print(f"Horse wins!")
        else:
            self.time += 1

    @classmethod
    def reset_horses(cls):
        for horse in cls.horses:
            horse.rect.x = horse.start_x
            horse.time = 0
            horse.current_frame = 0
            horse.image = horse.frames[horse.current_frame]

def display_winner(winning_horse):
    text = font.render(f"{winning_horse.color} horse wins!!!", True, FONT_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    screen.blit(winning_horse.image, (WIDTH // 2 - winning_horse.image.get_width() // 2, HEIGHT // 2 + text.get_height() // 2 + 10))
    pygame.display.flip()

def display_start_message():
    text = font.render(START_MESSAGE, True, FONT_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + 60))
    pygame.display.flip()

game = True
run = True
winning_horse = None

# Initialize horses
horse_colors = ["Blue", "Brown", "Pink", "Red", "Green"]
horses = [Horse(row, 10, 172 * (row + 0), horse_colors[row]) for row in range(5)]

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
        pygame.time.wait(2000)
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
