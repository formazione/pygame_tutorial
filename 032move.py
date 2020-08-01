import pygame


pygame.init()
screen = pygame.display.set_mode((400, 600))


class Cat:
    x = 100
    y = 100


cat = pygame.image.load("cat/Idle (1).png").convert_alpha()
square = pygame.Surface((cat.get_size()))
square.fill((0, 180, 250))
sw, sh = screen.get_size()
clock = pygame.time.Clock()
while True:
    screen.fill((128, 255, 128))
    # screen.blit(pygame.transform.scale(cat, (sw, sh)),(0, 0))
    #screen.blit(square, (Cat.x, Cat.y))
    screen.blit(cat, (Cat.x, Cat.y))
    if pygame.event.get(pygame.QUIT):
        break
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Cat.x += 10
            if event.key == pygame.K_LEFT:
                Cat.x -= 10
            if event.key == pygame.K_UP:
                Cat.y -= 10
            if event.key == pygame.K_DOWN:
                Cat.y += 10



    pygame.display.update()
    clock.tick(60)


pygame.quit()