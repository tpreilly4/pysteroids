from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a = self.velocity.rotate(angle)
        b = self.velocity.rotate(-angle)

        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        other_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid.velocity = a * 1.2
        other_new_asteroid.velocity = b * 1.2
