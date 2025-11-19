import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from astroidfield import AsteroidField
from logger import log_event
import sys
from shot import Shot

def main():

    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}") 

    pygame.init() # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set screen size

    clock = pygame.time.Clock()
    dt = 0

    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

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
        for shot in shots:
            for astriod in asteroids:
                if shot.collide_with(astriod):
                    log_event("asteroid_shot")
                    astriod.split()
                    shot.kill()

        pygame.display.flip() # Update the full display surface to the screen
        dt = clock.tick(60) / 1000  # Amount of seconds between each loop
    




if __name__ == "__main__":
    main()
