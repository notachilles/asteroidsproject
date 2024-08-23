from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity_x=0, velocity_y=0):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(velocity_x, velocity_y)



    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_velocity1 = self.velocity.rotate(random_angle)
            new_velocity2 = self.velocity.rotate(-random_angle)
            new_velocity1 *= 1.2
            new_velocity2 *= 1.2

            new1 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity1.x, new_velocity1.y)
            new2 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity2.x, new_velocity2.y)

        
        
