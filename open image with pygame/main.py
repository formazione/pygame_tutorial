import tkinter as tk
from tkinter import filedialog
import button as bt

# Hello, this is a snippet
import pygame


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Quick Start')
clock = pygame.time.Clock()
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))


images = pygame.sprite.Group()
class Image(pygame.sprite.Sprite):
    def __init__(self, file_path, x, y):
        super().__init__()
        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        images.add(self)

def openf():
    file_path = filedialog.askopenfilename()
    # img = tk.PhotoImage(file=self.file_path)
    image = Image(file_path, 0, 30)
    

b1 = bt.Button()
b1.render("Open_file")
b1.command = openf

is_running = True
while is_running:

     screen.blit(background, (0, 0))
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             is_running = False

     images.update()
     images.draw(screen)
     bt.buttons.update()
     bt.buttons.draw(screen)
     pygame.display.update()
     clock.tick(60)
pygame.quit()

