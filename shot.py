from constants import PLAYER_SHOT_SPEED, SHOT_RADIUS
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, radius=SHOT_RADIUS)  # Small radius for the shot
        self.velocity = direction.normalize() * PLAYER_SHOT_SPEED  # High speed in the given direction

    def draw(self, screen):
       
        pygame.draw.circle(
            screen,
            "yellow",
            self.position,
            self.radius
        )

    def update(self, dt):
        self.position += self.velocity * dt
