import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    group_asteroids = pygame.sprite.Group() 
    group_shots = pygame.sprite.Group()

    Player.containers = (group_updatable, group_drawable)
    Asteroid.containers = (group_updatable, group_drawable, group_asteroids)
    AsteroidField.containers = (group_updatable)
    Shot.containers = (group_updatable, group_drawable, group_shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        for obj in group_drawable:
            obj.draw(screen)
        for obj in group_updatable:
            obj.update(dt)
        for asteroid in group_asteroids:
            if asteroid.did_collide(player):
                screen.fill("red")
                pygame.time.wait(2000)
                print("Game over!")
                sys.exit()
            
            for shot in group_shots:
                if asteroid.did_collide(shot):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

