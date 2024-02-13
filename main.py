import pygame
import sys
import random
import asyncio
import os

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
width = 1500
height = 800
size = width, height

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

surfaces = pygame.sprite.Group()
winners = pygame.sprite.Group()
class Horse(pygame.sprite.Sprite):
    def __init__(self, dinoname, x, y):
        super().__init__()
        # self.image = pygame.Surface((50,50))
        self.dinoname = dinoname
        # self.image = pygame.image.load(f"img\\{self.dinoname}.png")
        # self.rect = self.image.get_rect()
        # self.rect.x = x
        # self.rect.y = y
        # # print(self.rect.w)
        # self.time = 0
        surfaces.add(self)


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
            # self.image.fill(0)
            self.kill()


class Spreadsheet(Horse):
    def __init__(self, sheetname, action, nframes, x, y, button):
        super().__init__(sheetname, x, y)
        # self.image = pygame.image.load(f"img\\{dinoname}.png")
        self.sheetname = sheetname
        self.img = pygame.image.load(f"img\\{self.sheetname}.png")
        self.nframes = nframes
        self.timer = 0
        self.rect = self.img.get_rect()
        self.size = [int(self.rect.w / self.nframes), self.rect.h]
        self.rect.x = x
        self.rect.y = y
        self.action = action

        self.x = x
        self.y = y
        self.win = 0
        color = self.sheetname.split("_")[1]
        self.color = color
        self.move = 0
        self.dict_images = {}
        self.dict_images[f"{action}r"] = []
        self.dict_images[f"{action}l"] = []
        self.action = action
        self.list_images(self.action)
        self.pause_idle = 0
        self.score = 0
        self.button = button

    

    def add_animation(self, sheetname, action, nframes, x, y):
        self.img = pygame.image.load(f"img\\{sheetname}.png")
        self.nframes = nframes
        self.dict_images[f"{action}r"] = []
        self.dict_images[f"{action}l"] = []
        self.action = action
        self.list_images(self.action)


    def list_images(self, action):
    # Getting images from single image
        for k in action+"r", action+"l":
            for x in range(self.nframes):
                self.frame_location = [self.size[0] * x, 0]  # so starting with 0, x moves with each iteration 80 pxl to the right
                self.img_rect = pygame.Rect(self.frame_location, self.size)
                # IMMAGINI VERSO DESTRA
                if k[-1] == "r": 
                    self.image = self.img.subsurface(self.img_rect)  # not the same variable as img
                    self.dict_images[k].append(self.image)
                # IMMAGINI VERSO SINISTRA
                if k[-1] == "l":
                    self.image = pygame.transform.flip(self.img.subsurface(self.img_rect),1,0)
                    self.dict_images[k].append(self.image)



    def animate_run(self, key, speed):
        if self.timer < self.nframes - 4:
            self.timer += .1*speed  #.1
        else:
            self.timer = 0
        timer = int(self.timer)
        self.image = self.dict_images[key][timer]


    def animate_pause(self, key, speed):
        if self.timer < self.nframes - 1:
            self.timer += .1*speed  #.1
        else:
            self.timer = 0
        timer = int(self.timer)
        self.image = self.dict_images[key][timer]


    def animate(self, key, speed):
        global game


        if game:
            self.animate_run(key, speed)
                    # if game: # NEL GIOCO SI MUOVONO A SINISTRA
        else:
            self.animate_pause(key, speed)
            # else:
        #     pass
            # animation when the game is ended (stop for 100 sec and then return back)



    def victory(self):
        global game

        game = 0
        name = self.dinoname.split("_")[1]

        # t2 = Text(f"{name} wins!",
        #         pos=(width // 2, self.rect.y+20),
        #         fontsize=36,
        #         color="white", bgcolor=self.color)

        self.score += 1
        self.button.x += 10
        # winners.add(self)
        # print(dir(winners))
        # print(winners.has(dino1))
        # self.time = 0
        print(self.color, self.score)


    def update(self):
        global game
        if game:       #    UNTIL 1.400:  move & animate
            if self.rect.x < 1400:
                self.animate("runr", random.randrange(0, 6))
                self.rect.x += random.randrange(2, 6) #self.time                 __
            else:       # ELSE... you won!                                      _||_
                self.victory()                               #                   ()-
                # I SHOULD PUT GAME = 0 HERE ?????    *********************BUG _/[]\,
        else:                                                    #           ..._/\_...
            # # SI TORNA INDIETRO DOPO 100 TIME
            # self.time += 1
            # if self.time < 100:
            #     self.animate("idler", random.randrange(0, 2))
            # else: # dopo 3 secondi tornano indietro alla linea di partenza
            #     # ################ CORSA INDIETRO ############################
            if self.rect.x > 30:
                self.animate("runl", random.randrange(2, 6))
                self.rect.x -= 20 # velocità di ritorno ramdom come all'andata
            else: # arrivati alla linea di partenza dovrebbe animarsi l'idle e fermarsi
                self.animate("idler", random.randrange(0, 2))
                # self.time = 0
                    
                    # self.move = 0


            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                # surfaces.clear()
                game = 1
                # main()

class Button(pygame.sprite.Sprite):
    ''' Create a button clickable with changing hover color'''

    def __init__(self,
                text,
                position,
                size,
                colors="white on blue",
                hover_colors="red on green",
                style=1, borderc=(255,255,255),
                command=lambda: print("No command activated for this button")):

        # the hover_colors attribute needs to be fixed
        super().__init__()
        self.text = text
        self.command = command
        # --- colors ---
        self.colors = colors
        self.original_colors = colors
        self.fg, self.bg = self.colors.split(" on ")
        if hover_colors == "red on green":
            self.hover_colors = f"{self.bg} on {self.fg}"
        else:
            self.hover_colors = hover_colors
        self.style = style
        self.borderc = borderc # for the style2
        # font
        self.font = pygame.font.SysFont("Arial", size)
        self.render()
        self.x, self.y, self.w , self.h = self.image.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        self.pressed = 1
        surfaces.add(self)

    def render(self):
        ''' create the surface with a text in self.image '''
        # add * to the text if you want an image on the button
        if "*" not in self.text:
            self.image = self.font.render(self.text, 1, self.fg)
        else:
            self.text = self.text.replace("*","")
            self.image = pygame.image.load(f"img\\{self.text}.png")



    def update(self):
        ''' called by buttons.update, the group of buttons '''
        self.fg, self.bg = self.colors.split(" on ")
        if self.style == 1:
            self.draw_button1()
        elif self.style == 2:
            self.draw_button2()
        self.hover()
        self.click()

    def draw_button1(self):
        ''' draws 4 lines around the button and the background '''
        # horizontal up
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y), (self.x + self.w , self.y), 5)
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y - 2), (self.x, self.y + self.h), 5)
        # horizontal down
        pygame.draw.line(screen, (50, 50, 50), (self.x, self.y + self.h), (self.x + self.w , self.y + self.h), 5)
        pygame.draw.line(screen, (50, 50, 50), (self.x + self.w , self.y + self.h), [self.x + self.w , self.y], 5)
        # background of the button
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w , self.h))  

    def draw_button2(self):
        ''' a linear border '''
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w , self.h))
        pygame.gfxdraw.rectangle(screen, (self.x, self.y, self.w , self.h), self.borderc)

    def hover(self):
        ''' checks if the mouse is over the button and changes the color if it is true '''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            # you can change the colors when the pointer is on the button if you want
            self.colors = self.hover_colors
            # pygame.mouse.set_cursor(*pygame.cursors.diamond)
        else:
            self.colors = self.original_colors
            
        self.render()

    def click(self):
        ''' checks if you click on the button and makes the call to the action just one time'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                # print("Execunting code for button '" + self.text + "'")
                self.command()
                self.pressed = 0
            if pygame.mouse.get_pressed() == (0,0,0):
                self.pressed = 1
    

# d = Animate("dino_1")




#                   MUSIC

pygame.mixer.init()
# start123 = pygame.mixer.Sound("music\\004.mp3")

# def start_voice():
#     pygame.mixer.quit()
#     pygame.mixer.init()
    
#     if not pygame.mixer.get_busy():
#         start123.play()

def start():
    global game, bg, bg1, bg2
    bg = random.choice([bg1,bg2])
    game = 1

butg = Button("   ", (0,0), 10, command=start, colors="white on green")
butr = Button("   ", (0,15), 10, command=start, colors="white on red")
butb = Button("   ", (0,30), 10, command=start, colors="white on blue")
buto = Button("   ", (0,45), 10, command=start, colors="white on orange")
butl = Button("   ", (0,60), 10, command=start, colors="white on lightblue")
# butimg = Button("*horse1", (0,80), 10, command=start, colors="white on lightblue")

dino1 = Spreadsheet("dino_green", "run", 8, 10, 180, butg)
dino2 = Spreadsheet("dino_red", "run", 8, 10, 280, butr)
dino3 = Spreadsheet("dino_blue", "run", 8, 10, 380, butb)
dino4 = Spreadsheet("dino_orange", "run", 8, 10, 480, buto)
dino5 = Spreadsheet("dino_lightblue", "run", 8, 10, 580, butl)

# # # add_animation
dino1.add_animation("idle_green", "idle", 8, 10, 100)
dino2.add_animation("idle_red", "idle", 8, 10, 280,)
dino3.add_animation("idle_blue", "idle", 8, 10, 380)
dino4.add_animation("idle_orange", "idle", 8, 10, 480)
dino5.add_animation("idle_lightblue", "idle", 8, 10, 580)



game = 0 # used to make the game end with ESC, not very useful though

async def main():
    global game, dino1, dino2, dino3, dino4, dino5, tabel, tabel_rect

    tabel = pygame.Surface((50,300))
    tabel_rect = tabel.get_rect()
    tabel.fill("cyan")
    score = []
    lastahead = ""
    bg1 = pygame.image.load("img\\bg.png")
    bg2 = pygame.image.load("img\\bg2.png")
    bg = random.choice([bg1,bg2])
    run = 1
    while run:
        screen.blit(bg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 0
        # print(clock.get_fps())
        # t3 = Text(str(clock.get_fps()),
        #         pos=(0, 200),
        #         fontsize=24,
        #         color="white", bgcolor="black")
        surfaces.update()
        surfaces.draw(screen)
        pygame.display.flip()
        await asyncio.sleep(0)
        clock.tick(60)
    pygame.quit()
    sys.exit()


asyncio.run(main())
