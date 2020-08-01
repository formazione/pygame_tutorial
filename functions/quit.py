import pygame

def user_inputs():
    if pygame.event.get(pygame.QUIT):
        return 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
    	return 1