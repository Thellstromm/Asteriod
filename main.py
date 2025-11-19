import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
     
    pygame.init() # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set screen size

    clock = pygame.time.Clock()
    dt = 0


    while True: # Main game loop
        log_state() # Log the game state
        for event in pygame.event.get(): #
            if event.type == pygame.QUIT:
                return
        screen.fill("black") # Clear the screen with black color
        pygame.display.flip() # Update the full display surface to the screen
        dt = clock.tick(60) / 1000  # Amount of seconds between each loop
         # print(dt)

    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
