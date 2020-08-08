import pygame
import glob


class MySprite(pygame.sprite.Sprite):
    def __init__(self, action="jump", location=(0, 0)):
        super(MySprite, self).__init__()
        self.action = action
        self.index = 0
        # if you use more istance with the same image
        # if MySprite.image is None
        self.list_surfaces = self.ordered_list_of_surfaces()
        self.image = self.list_surfaces[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = location

    def update(self):
        self.index += .5
        if self.index >= len(self.list_surfaces):
            self.index = 0
        self.image = self.list_surfaces[int(self.index)]

    def ordered_list_of_surfaces(self):
        "Ordered images i list_of_surfaces"
        im = glob.glob(f"png\\{self.action}*.png")
        self.los = [
            pygame.image.load(img)
            for img in glob.glob(f"png\\{self.action}*.png")
            if len(img) == len(im[0])]
        self.los2 = [
            pygame.image.load(img)
            for img in glob.glob(f"png\\{self.action}*.png")
            if len(img) != len(im[0])]
        self.los.extend(self.los2)
        return self.los


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Trace")
    idle = MySprite("Idle", (0, 0))
    jump = MySprite("Jump", (200, 0))
    walk = MySprite("Walk", (400, 0))
    run = MySprite("Run", (600, 0))
    sprites = idle, jump, walk, run
    # bck = pygame.Surface((my_sprite.size))
    # bck.fill((0,0,0))
    # add my sprite to my_group
    my_group = pygame.sprite.Group(sprites)
    clock = pygame.time.Clock()
    loop = 1
    while loop:
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # action = "jump"
                    pass

        my_group.update()
        # my_group.clear(screen, bgd)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()


SIZE = WIDTH, HEIGHT = 1200, 600
FPS = 60
# im1 = pygame.image.load(glob.glob(f"png\\*.png")[0])
# size = im1.get_size()
# bgd = pygame.Surface(SIZE)

if __name__ == '__main__':
    main()
