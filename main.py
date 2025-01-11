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

#mport constants
from constants import *

def main():
    pygame.init()
    # SCREEN_WIDTH = constants.SCREEN_WIDTH
    # SCREEN_HEIGHT = constants.SCREEN_HEIGHT 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()