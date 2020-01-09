import pygame
from abstract_manager import *

# CONSTANTS
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

class Levels_Manager(Abstract_Manager):

    def __init__(self):
        self.new_manager = None
        self.change_manager = False
        self.difficulty = None
        self.run = True

    # override
    def run_screen(self,screen):
        screen.fill((100,20,0))
        self.check_events(screen)

    # override
    def check_events(self,screen):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            pygame.display.update()