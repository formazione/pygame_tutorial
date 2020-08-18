import pygame


pygame.init()

screen = pygame.display.set_mode((400, 600))
square = pygame.Surface((50, 70))
bg = pygame.image.load("images/002.png").convert()
bg_rect = bg.get_rect()
print(bg_rect)
square.fill((0, 180, 250))
while True:
    screen.fill((128, 255, 128))
    screen.blit(bg, (10, 50))
    screen.blit(square, (300, 100))
    if pygame.event.get(pygame.QUIT):
        break
    pygame.display.update()

pygame.quit()

# https://pythonprogramming.altervista.org/pygame-tutorial-n-1/