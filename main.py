import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables, shots)


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        screen.fill("black")
        dt = clock.tick(60) / 1000
        
        for updatable in updatables:
            updatable.update(dt)

        for shot in shots:
            for asteroid in asteroids:
                if shot.checkcollisions(asteroid):
                    shot.kill()
                    asteroid.split()
        

        for asteroid in asteroids:
            if asteroid.checkcollisions(player):
                print("Game over!")
                sys.exit()

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        



if __name__ == "__main__":
    main()