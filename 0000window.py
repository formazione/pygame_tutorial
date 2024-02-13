import pygame
import sys
from filedata import *


def quit():
	''' user wants to quit '''
	write("window.txt", f"Today is another {today()}")
	print("\npygame still active")
	print("Game.screen = ", Game.screen, "\n")
	print("Game.clock = ", Game.clock, "\n")
	print("pygame is quitted with pygame.quit()")
	pygame.quit()
	print("Game.screen = ", Game.screen, "\n")
	print("\nExit from pygame\n\n")
	print("Now we close Python with sys.exit()")
	sys.exit()


def user_events():
	''' Let's get user's interaction with input devices '''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quit()
	pygame.display.flip()
	Game.clock.tick(60)


class Game:
	# here we go.... forever... until user quits
	pygame.init()
	screen = pygame.display.set_mode((600, 400))
	clock = pygame.time.Clock()
	pygame.display.set_caption("Press Esc to quit")
	

class Mainloop:
		while True:
			user_events()