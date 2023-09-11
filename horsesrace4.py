import pygame
import sys
import random



pygame.init()
width = 1500
height = 800
size = width, height

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

surfaces = pygame.sprite.Group()
class Horse(pygame.sprite.Sprite):
    def __init__(self, dinoname, x, y):
        super().__init__()
        # self.image = pygame.Surface((50,50))
        self.dinoname = dinoname
        self.image = pygame.image.load(f"img\\{self.dinoname}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        print(self.rect.w)
        surfaces.add(self)
        self.time = 0

    def update(self):
        global game, run

        if game:
            if self.rect.x < 1400:
                self.rect.x += random.randrange(0, 5) #self.time
                Text(f"{self.dinoname } {self.rect.x}",
                        pos=(self.rect.x - 100,self.rect.y+20),
                        color="red", bgcolor="green")
            else:
                game = 0
                t1.kill()
                t2 = Text(f"{self.dinoname } wins!!!!",
                        pos=(self.rect.x - 100,self.rect.y+20),
                        color="red", bgcolor="green")
            
        else:
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                surfaces.empty()
                run_game()

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
        surfaces.add(self)
        # print(pos, self.pos)


    def add_background(self):
        img = self.image.copy()
        self.image.fill(self.bgcolor)
        self.image.blit(img, (0,0))

    def update(self):
        # Incredible how I fixed the trace leaved by the moving text with this
        # line: 9.9.2023 11.15 (this is insane!)
        if game:
            self.image.fill(0)


class Spreadsheet(Horse):
    def __init__(self, sheetname, x, y):
        super().__init__(sheetname, x, y)
        # self.image = pygame.image.load(f"img\\{dinoname}.png")
        self.sheetname = sheetname
        self.img = pygame.image.load(f"img\\{self.sheetname}.png")
        self.nframes = 8
        self.timer = 0
        self.rect = self.img.get_rect()
        self.size = [int(self.rect.w / self.nframes), self.rect.h]
        self.rect.x = x
        self.rect.y = y
        self.animations = []
        self.x = x
        self.y = y
        self.red_dot = pygame.Surface((10,10))
        for x in range(self.nframes):
            self.frame_location = [self.size[0] * x, 0]  # so starting with 0, x moves with each iteration 80 pxl to the right
            self.img_rect = pygame.Rect(self.frame_location, self.size)
            self.image = self.img.subsurface(self.img_rect)  # not the same variable as img
            self.animations.append(self.image)



    def update(self):
        global game, run
        speed = random.randrange(0, 5)
        if game:
            if self.timer < 7:
                self.timer += .15*speed  #.1
            else:
                self.timer = 0
            timer = int(self.timer)
            if game:
                self.image = self.animations[timer]


        if game:
            if self.rect.x < 1400:
                self.rect.x += speed #self.time
                # THE SCORE FOLLOWING THE DINO (INCREDIBLE TRICK WITH self.image.fill(0) in text to delete trace)
                tx = Text(f"{self.rect.x}",
                        pos=(self.rect.x - 100, self.rect.y+20),
                        color="blue", bgcolor='yellow')
                # LITTLE RED DOT FOLLOWING THE SCORE
                # for s in score:
                #     if self.rect.x > s:
                #         self.red_dot.fill('green')
                #     else:
                #         self.red_dot.fill('red')
                # score.append(self.rect.x)
                # screen.blit(self.red_dot, (self.rect.x-100,self.rect.y+10))

            else:
                game = 0
                t2 = Text(f"{self.dinoname } wins!!!! with {self.rect.x} points!",
                        pos=(self.rect.x - 500, self.rect.y+20),
                        fontsize=26,
                        color="red", bgcolor="yellow")
        else:
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                surfaces.empty()
                run_game()

class Animate(pygame.sprite.Sprite):
    def __init__(self, sheetname):
        super().__init__()
    

# d = Animate("dino_1")

score = []
def run_game():
    global game

    game = 1 # used to make the game end with ESC, not very useful though


    t1 = Text("SPREADSHEET TUTORIAL", pos=(0,0), fontsize=36, color="yellow", bgcolor="black")
    # # IMAGES
    # dino1 = Horse("dino1", 10, 200, "white")
    # dino2 = Horse("dino2", 10, 300, "blue")
    # dino3 = Horse("dino3", 10, 400, "red")
    # dino4 = Horse("dino4", 10, 500, "yellow")
    # dino5 = Horse("dino5", 10, 600, "green")
    bg = pygame.image.load("img\\bg.png")
    dino1 = Spreadsheet("dino_green", 10, 180)
    dino2 = Spreadsheet("dino_red", 10, 280,)
    dino3 = Spreadsheet("dino_blue", 10, 380)
    dino4 = Spreadsheet("dino_orange", 10, 480)
    dino5 = Spreadsheet("dino_lightblue", 10, 580)


    run = 1
    while run:
        # screen.fill(0)
        screen.blit(bg, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 0
        surfaces.update()
        surfaces.draw(screen)
        pygame.display.flip()
        clock.tick(60)


    pygame.quit()
    sys.exit()

run_game()
