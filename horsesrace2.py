import pygame
import sys
import random



pygame.init()
width = 1000
height = 800
size = width, height

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

horses = pygame.sprite.Group()
class Horse(pygame.sprite.Sprite):
    def __init__(self, horsename, x, y, color):
        super().__init__()
        # self.image = pygame.Surface((50,50))
        self.horsename = horsename
        self.image = pygame.image.load(f"img\\{self.horsename}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        print(self.rect.w)
        self.color = color
        # self.image.fill(self.color)
        horses.add(self)
        self.time = 0

    def update(self):
        global game, run

        if game:
            if self.rect.x < 900:
                self.rect.x += random.randrange(0, 5) #self.time
            else:
                game = 0
                t1.kill()
                t2 = Text(f"{self.horsename } wins!!!!",
                        pos=(self.rect.x - 100,self.rect.y+20),
                        color="red", bgcolor="green")
            
        else:
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                print("ESV")
                run = 0

class Text(pygame.sprite.Sprite):
    """ create a rendered text you can blit with blit function """

    def __init__(self, text, fontname="Arial", fontsize=20,
        color='white', bgcolor='', pos=(0,0), centered=0):
        ''' surface = buffer_screen or screen '''

        super().__init__()
        self.text = text
        self.pos = pos
        self.bgcolor = bgcolor
        self.fontprint = pygame.font.SysFont(fontname, fontsize)
        self.image = self.fontprint.render(self.text, 1, color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos
        if bgcolor == '':
            pass
        else:
            self.add_background()
        if centered:
            self.pos = self.x - self.w // 2, self.y - self.h //2
        horses.add(self)
        # print(pos, self.pos)


    def add_background(self):
        img = self.image.copy()
        self.image.fill(self.bgcolor)
        self.image.blit(img, (0,0))




t1 = Text("Horses Race", pos=(0,0), fontsize=36, color="yellow", bgcolor="black")

game = 1
# IMAGES
horse1 = Horse("horse1", 10, 200, "white")
horse2 = Horse("horse2", 10, 300, "blue")
horse3 = Horse("horse3", 10, 400, "red")
horse4 = Horse("horse4", 10, 500, "yellow")
horse5 = Horse("horse5", 10, 600, "green")
bg = pygame.image.load("img\\bg.png")


run = 1
while run:
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
    horses.update()
    horses.draw(screen)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()