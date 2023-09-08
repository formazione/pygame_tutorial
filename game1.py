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
				print(f"{self.horsename } wins!!!!")
		else:
			self.time += 1
			if self.time > 200:
				run = 0


game = 1
horse1 = Horse("horse1", 10, 100, "white")
horse2 = Horse("horse2", 10, 200, "blue")
horse3 = Horse("horse3", 10, 300, "red")
horse4 = Horse("horse4", 10, 400, "yellow")
horse5 = Horse("horse5", 10, 500, "green")



run = 1
while run:
	screen.fill(0)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = 0
	horses.update()
	horses.draw(screen)
	pygame.display.flip()
	clock.tick(60)


pygame.quit()
sys.exit()