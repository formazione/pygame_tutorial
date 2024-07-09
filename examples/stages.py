import pygame
import sys



# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cosmic Rescue: A Parent's Quest")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load images (replace with your own image files)
parent_img = pygame.Surface((50, 50))  # Placeholder for parent alien
parent_img.fill((0, 255, 0))  # Green rectangle for now
baby_img = pygame.Surface((30, 30))  # Placeholder for baby alien
baby_img.fill((0, 0, 255))  # Blue rectangle for now
villain_img = pygame.Surface((50, 50))  # Placeholder for villain
villain_img.fill((255, 0, 0))  # Red rectangle for now

# Initial positions
parent_pos = [WIDTH // 4, HEIGHT - 100]
baby_pos = [WIDTH // 2, HEIGHT - 150]
villain_pos = [WIDTH, HEIGHT - 100]  # Start off-screen

# Game states
INTRO = 0
TUTORIAL = 1
VILLAIN_ENTER = 2
BABY_TAKEN = 3
game_state = INTRO

# Game loop
clock = pygame.time.Clock()
running = True

def show(text, size=36, color=WHITE, pos=None):
        font = pygame.font.Font(None, size)
        mytext = font.render(text, True, color)
        if pos == None:
            pos = (WIDTH // 2 - mytext.get_width() // 2, HEIGHT // 2)
        screen.blit(mytext, pos)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_state += 1  # Progress the scene
                print(game_state)
                match game_state:
                    case 1: print("TUTORIAL")
                    case 2: print("VILLAIN_ENTER")
                    case 3: print("BABY_TAKEN")

    screen.fill(BLACK)  # Clear the screen

    # Draw characters
    screen.blit(parent_img, parent_pos)
    if game_state < BABY_TAKEN:
        screen.blit(baby_img, baby_pos)
    if game_state >= VILLAIN_ENTER:
        screen.blit(villain_img, villain_pos)

    # Update scene based on game state
    if game_state == INTRO:
        show("INTRO")
        show("A peaceful night shattered", pos=(10,10))
    elif game_state == TUTORIAL:
        show("Use arrow keys to move. Press SPACE to jump.")
    elif game_state == VILLAIN_ENTER:
        villain_pos[0] -= 5  # Move villain towards baby
        if villain_pos[0] <= baby_pos[0]:
            game_state = BABY_TAKEN
    elif game_state == BABY_TAKEN:
        show("Your child has been taken")


    pygame.display.flip()
    clock.tick(60)  # 60 FPS

# pygame.quit()
sys.exit()