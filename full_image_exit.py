# full screen image with exit button drawed

import pygame

pygame.init()

wh = width, height = pygame.display.get_desktop_sizes()[0]
print(width, height)

screen = pygame.display.set_mode((wh), pygame.FULLSCREEN)


def bg():
    image = pygame.image.load("image.jpg")
    image_scaled = pygame.transform.scale(image, (wh))
    screen.blit(image_scaled, (0, 0))  # Or use image if not scaled

def exit_button():
    exit_button_rect = pygame.Rect(10, 10, 50, 50)  # Create a rectangle for the button
    exit_button_color = (255, 0, 0)  # Red color for the button
    pygame.draw.rect(screen, exit_button_color, exit_button_rect)
    pygame.draw.line(screen, (255,255,255),
        (exit_button_rect[0],exit_button_rect[1]),
        (exit_button_rect[0]+exit_button_rect[2],exit_button_rect[1]+exit_button_rect[3]),
        3
        )
    pygame.draw.line(screen, (255,255,255),
        (exit_button_rect[0]+exit_button_rect[2],exit_button_rect[1]),
        (exit_button_rect[0],exit_button_rect[1]+exit_button_rect[3]),
        3
        )
    return exit_button_rect


bg()
exit_button_rect = exit_button()

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button_rect.collidepoint(event.pos):
                running = False


pygame.quit()
