import pygame
from constants import *
from levels_utils import *
from menu_utils import *


# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))

# game title on the window
pygame.display.set_caption('Will it light up?')

# initialize the events manager
manager = Menu_Manager()

run = True
actual_manager = 0

while run:
    manager_num = manager.run_screen(screen)
    if(manager_num!=actual_manager):
        if manager_num == 0:
            manager = Menu_Manager()
        elif manager_num == 1:
            manager = Levels_Manager()
    run = manager.run
