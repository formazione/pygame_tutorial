import pygame


pygame.init()

screen = pygame.display.set_mode((400, 600))
square = pygame.Surface((50, 70))
bg = pygame.image.load("images/002.png").convert_alpha()
bg_rect = bg.get_rect()
x, y, w, h = bg.get_rect()
size = bg.get_size()
print(w, h)
print(size)
print(bg_rect)
square.fill((0, 180, 250))
sw, sh = screen.get_size()
while True:
    screen.fill((128, 255, 128))
    screen.blit(pygame.transform.scale(bg, (sw, sh)),(0, 0))
    screen.blit(square, (300, 100))
    if pygame.event.get(pygame.QUIT):
        break
    pygame.display.update()

pygame.quit()