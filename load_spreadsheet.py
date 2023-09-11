# load a spreadsheet
import pygame
import sys
# main surface
screen = pygame.display.set_mode((800, 600))
# surface 1
clock = pygame.time.Clock()


class Animate(pygame.sprite.Sprite):
    def __init__(self, sheetname):
        super().__init__()
        self.sheetname = sheetname
        self.img = pygame.image.load(f"img\\{self.sheetname}.png")
        self.nframes = 8
        self.size = [int(self.img.get_width() / self.nframes), self.img.get_height()]

        self.animations = []
        for x in range(self.nframes):
            self.frame_location = [self.size[0] * x, 0]  # so starting with 0, x moves with each iteration 80 pxl to the right
            self.img_rect = pygame.Rect(self.frame_location, self.size)
            
            self.new_img = self.img.subsurface(self.img_rect)  # not the same variable as img
            self.animations.append(self.new_img)
    

d = Animate("dino_1")


counter = 0
loop = 1
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
    if counter < d.nframes -1:
        counter +=1
    else:
        counter = 0
    screen.fill((0,0,0))
    screen.blit(d.animations[counter], (10, 150))
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()