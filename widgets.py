import pygame
import glob

'''        W I D G E T S

Text              I want an integer as max words to go next line
  |
 Label


Cloud

Examples: you can choose to blit on screen or buffer_screen
screen is the ultimate surface
buffer_screen -> screen -> blit

cloud = Cloud(buffer_screen,
                400,100,500,200)

# A TEXT
hello = Text("Hello, I am a text")
hello.render(buffer_screen, pos=(100,100))

# A LABEL
world = Label("'world', I am a label with a blue background",
    bgcolor="blue")
world.render(buffer_screen, pos=(100,200))


'''

####################################################################### TEXT
class Text:
    """ create a rendered text you can blit with blit function """

    def __init__(self, text, surface=buffer_screen, fontname="Arial", fontsize=20,
        color='white', bgcolor='', pos=(0,0), centered=0):
        ''' surface = buffer_screen or screen '''
        self.text = text
        self.pos = pos
        self.bgcolor = bgcolor
        self.surface = surface
        self.fontprint = pygame.font.SysFont(fontname, fontsize)
        self.rendered_text = self.fontprint.render(self.text, 1, color)
        self.w, self.h = self.rendered_text.get_size()
        self.x, self.y = self.pos
        if bgcolor == '':
            pass
        else:
            self.add_background()
        if centered:
            self.pos = self.x - self.w // 2, self.y - self.h //2
        self.blit()

    def add_background(self):
        self.bg = pygame.Surface(self.rendered_text.get_size())
        self.bg.fill(self.bgcolor)
        self.bg.blit(self.rendered_text, (0,0))
        self.surface.blit(self.bg, self.pos)

    def blit(self):
        ''' blit on surf '''
        self.surface.blit(self.rendered_text, self.pos)


class LongText(Text):

    def __init__(self, text):
        super().__init__(text)
        self.text = text
        if self.w + self.x > screen_w:
            print("Va fuori schermo")








######################################################################## CLOUD
class Cloud:
    def __init__(self, surface, text='hello', crect=pygame.Rect(0,0,0,0), color="white"):
        ''' surface = buffer_screen or screen '''
        self.x,self.y,self.w,self.h = crect
        self.screen = surface
        self.color = color
        self.rect = crect
        self.dir = "left"
        self.text = text


    def blit(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        match self.dir:
            case 'right':
                hw = self.w//2
                pygame.draw.polygon(self.screen, self.color,(
                        (self.x+hw, self.y+self.h),
                        (self.x+hw+30, self.y+self.h),
                        (self.x+hw+30, self.y+self.h+50)
                        ),0)
            case 'left':
                hw = self.w//2
                pygame.draw.polygon(self.screen, self.color,(
                        (self.x+hw-30, self.y+self.h),
                        (self.x+hw, self.y+self.h),
                        (self.x+hw-50, self.y+self.h+50)
                        ),0)
        print("Cloud created")

buttons = pygame.sprite.Group()
class Button(pygame.sprite.Sprite):
    ''' Create a button clickable with changing hover color'''

    def __init__(self, position, text, size,
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
        buttons.add(self)

    def render(self):
        ''' create the surface with a text in self.image '''
        self.image = self.font.render(self.text, 1, self.fg)


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
                print("Execunting code for button '" + self.text + "'")
                self.command()
                self.pressed = 0
            if pygame.mouse.get_pressed() == (0,0,0):
                self.pressed = 1


 
animations = pygame.sprite.Group()
class LoadAnimation(pygame.sprite.Sprite):
    ''' It loads a series of images into a list and iterate them
    when you don't move: idle
    when you move: walk
    move left: 
    move right: 
    '''
    def __init__(self, root, pos, size):
        super().__init__()
 
        self.images = []
        self.root = root
        self.x, self.y = self.pos = pos
        self.w, self.h = self.size = size
        # === to put the image in order === 1, 2, 3.... 9, 10, 11
        # otherwise it would go 1, 11, 12, ... 2, 3
        self.imageslist = glob.glob(f"{self.root}\\*.png")
        # print(self.imageslist)

        self.idle = self.get_images(f"{self.root}\\Idle")
        self.walk = self.get_images(f"{self.root}\\Walk")
        # self.jump = self.get_images(f"{self.root}\\Jump")
        # print(self.idle)
        self.index = 0
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.state = 0
        self.images = self.idle
        animations.add(self)

    def get_images(self, name):
        # load images of a type of animation in the right numeric order
        temp = [i for i in self.imageslist if i.startswith(f"{name}")]
        first = len(temp[0])
        idle1 = []
        idle2 = []
        for i in temp:
            if len(i) == first:
                idle1.append(i)
            else:
                idle2.append(i)
        temp = idle1 + idle2 # now the order should be correct
        temp = [pygame.image.load(i).convert() for i in temp]
        temp = [self.scale(i) for i in temp]
        return temp

    def scale(self, image):
        return pygame.transform.scale(image, (self.w, self.h))


    def user_interaction(self):
        ''' called by update of this class '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                # IF YOU PRESS RIGHT PLAYER WALKS (see update method)
                if event.key == pygame.K_RIGHT:
                    self.state = 1
                # IF YOU PRESS UP PLAYER JUMPS (see update method)
                if event.key == pygame.K_UP:
                    self.state = 2
            # WHEN YOU DO not HOLD key it goes back to IDLE
            if event.type == pygame.KEYUP:
                self.state = 0




    def update(self):
        # CHECK KEY PRESSED
        # self.user_interaction()

        if self.state == 0:
                self.images = self.idle
        # YOU PRESS RIGHT ARROW: WALKS
        elif self.state == 1:
                self.images = self.walk
        # YOU PRESS UP, JUMPS
        elif self.state == 2:
                self.images = self.jump

        # ITERATE THROUGH IMAGES FOR ANIMATION
        if int(self.index) >= len(self.images):
                self.index = 0
        self.image = self.images[int(self.index)]
        self.index += .3



sprites = pygame.sprite.Group()
class Image(pygame.sprite.Sprite):
    ''' load an image and place it at x,y '''
    def __init__(self, path, x, y):
        super().__init__()
        self.path = path
        self.x = x
        self.y = y
        self.load()
        self.visible = True
        sprites.add(self)

    def load(self):

        self.image = pygame.image.load(self.path)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        if not self.visible:
            self.kill()



def help(subject):
    print(subject.__doc__)


def buttons_kill():
    for button in buttons:
        button.kill()


def get_globals():
    x =  [i for i in globals()]
    for i in x:
        print(i)
