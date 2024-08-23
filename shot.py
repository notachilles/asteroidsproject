from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

import pygame

class Shot(CircleShape):
    def __init__(self, x, y, angle):
        super().__init__(x, y, SHOT_RADIUS)  # Initialize with x, y and radius
        self.position = pygame.Vector2(x,y)

        # Setup velocity vector
        self.velocity = pygame.Vector2(0, 1).rotate(-angle) * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    

    def update(self, dt):        
        move_vector = self.velocity * dt
        self.position += move_vector

        # Remove the shot if it goes off-screen
        # screen_rect = pygame.display.get_surface().get_rect()
        # if not screen_rect.collidepoint(self.x, self.y):
        # self.kill()  # Assuming you have this method to handle removal