import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from astroidfield import AsteroidField
from logger import log_event
import sys

def main():
     
    pygame.init() # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set screen size

    clock = pygame.time.Clock()
    dt = 0
    
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Create player at center of screen
    asteroid_field = AsteroidField() # Create asteroid field




    while True: # Main game loop
        log_state() # Log the game state
        for event in pygame.event.get(): #
            if event.type == pygame.QUIT:
                return
        screen.fill("black") # Clear the screen with black color

        updatable.update(dt) # Update the player state
        for sprite in drawable:
          sprite.draw(screen) # Draw the player
        for astriod in asteroids:
            if player.collide_with(astriod):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        pygame.display.flip() # Update the full display surface to the screen
        dt = clock.tick(60) / 1000  # Amount of seconds between each loop
         # print(dt)

    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
