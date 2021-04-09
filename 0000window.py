import pygame
import sys



def quit():
	''' user wants to quit '''
	pygame.quit()
	print("\nExit from pygame\n\n")
	sys.exit()


def user_events():
	''' Let's get user's interaction with input devices '''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		if event.type == pygame.KEYDOWN:
			if event.type == pygame.K_ESCAPE:
				quit()


class Game:
	# here we go.... forever... until user quits
	pygame.init()
	screen = pygame.display.set_mode((600, 400))
	pygame.display.set_caption("Press Esc to quit")
	

class Mainloop:
		while True:
			user_events()
