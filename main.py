# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import the connect_database function
# and the database_version variable
# from database.py into the current file
# from database import connect_database, database_version

# import everything from the module
# database.py into the current file
# from database import *

#import constants
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    # SCREEN_WIDTH = constants.SCREEN_WIDTH
    # SCREEN_HEIGHT = constants.SCREEN_HEIGHT 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    time = pygame.time.Clock()  
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updateable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        # player.update(dt)
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        # player.draw(screen)

        pygame.display.flip()
        
        #limit to 1/60th fps
        dt = time.tick(60)/1000

if __name__ == "__main__":
    main()