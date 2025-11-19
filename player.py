from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SPEED, PLAYER_TURN_SPEED , PLAYER_SHOT_SPEED, PLAYER_SHOT_COOLDOWN_SECONDS
import pygame

# Player class inheriting from CircleShape
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0  # Player's rotation angle
        self.cooldown = 0  # Cooldown timer for shooting


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    
    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            "white",
            self.triangle(),
            LINE_WIDTH,
        )

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt # Rotate left
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt # Rotate right
        if keys[pygame.K_w]:
            self.move_forward(dt) # Move forward
        if keys[pygame.K_s]:
            self.move_forward(-dt) # Move backward

        if self.cooldown > 0:
            self.cooldown -= dt  # Decrease cooldown timer
        if keys[pygame.K_SPACE] and self.cooldown <= 0:
            self.shoot()  # Shoot a shot
            self.cooldown = PLAYER_SHOT_COOLDOWN_SECONDS  # Reset cooldown timer

    def move_forward(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        from shot import Shot  # Import here to avoid circular dependency
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y, direction)
        return shot
        
 