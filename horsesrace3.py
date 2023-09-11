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
    def __init__(self, horsename, x, y):
        super().__init__()
        # self.image = pygame.Surface((50,50))
        self.horsename = horsename
        self.image = pygame.image.load(f"img\\{self.horsename}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        print(self.rect.w)
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


class Spreadsheet(Horse):
    def __init__(self, sheetname, nframes, x, y):
        super().__init__(sheetname, x, y)
        # self.image = pygame.image.load(f"img\\{horsename}.png")
        self.sheetname = sheetname
        self.img = pygame.image.load(f"img\\{self.sheetname}.png")
        self.nframes = nframes
        self.size = [int(self.img.get_width() / self.nframes), self.img.get_height()]
        self.timer = 0
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.animations = []
        self.x = x
        self.y = y
        for x in range(self.nframes):
            self.frame_location = [self.size[0] * x, 0]  # so starting with 0, x moves with each iteration 80 pxl to the right
            self.img_rect = pygame.Rect(self.frame_location, self.size)
            self.image = self.img.subsurface(self.img_rect)  # not the same variable as img
            self.animations.append(self.image)



    def update(self):
        global game, run

        if game:
            if self.timer < 7:
                self.timer += .1
            else:
                self.timer = 0
            timer = int(self.timer)
            if game:
                self.image = self.animations[timer]


        if game:
            if self.rect.x < 900:
                self.rect.x += random.randrange(0, 5) #self.time
            else:
                game = 0
                t2 = Text(f"{self.horsename } wins!!!!",
                        pos=(self.rect.x - 100,self.rect.y+20),
                        color="red", bgcolor="green")


class Animate(pygame.sprite.Sprite):
    def __init__(self, sheetname):
        super().__init__()
    

# d = Animate("dino_1")



game = 1 # used to make the game end with ESC, not very useful though


t1 = Text("SPREADSHEET TUTORIAL", pos=(0,0), fontsize=36, color="yellow", bgcolor="black")
# # IMAGES
# horse1 = Horse("horse1", 10, 200, "white")
# horse2 = Horse("horse2", 10, 300, "blue")
# horse3 = Horse("horse3", 10, 400, "red")
# horse4 = Horse("horse4", 10, 500, "yellow")
# horse5 = Horse("horse5", 10, 600, "green")
bg = pygame.image.load("img\\bg.png")
horse1 = Spreadsheet("dino_green", 8, 10, 200)
horse2 = Spreadsheet("dino_red", 8, 10, 300,)
horse3 = Spreadsheet("dino_blue", 8, 10, 400)
horse4 = Spreadsheet("dino_orange", 8, 10, 500)
horse5 = Spreadsheet("dino_lightblue", 8, 10, 600)


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