import pygame
from levels_utils import *
from menu_utils import *
from managers_handler import *
from pygame import mixer


# initialize pygame
pygame.init()
mixer.init()
pygame.font.init()

# create screen
screen = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))

# game title on the window
pygame.display.set_caption('Will it light up?')

# initialize the events manager
manager = Menu_Manager()

# background sounds
mixer.music.load('sound/Soft-electronic-ambient-background-music.mp3')

# mixer.music.load('sound/Electronic-ambient-background-beat.mp3')

mixer.music.play(-1)

while manager.run:
    manager.run_screen(screen)
    if manager.change_manager:
        index = manager.new_manager
        manager = manager_list[index]()
