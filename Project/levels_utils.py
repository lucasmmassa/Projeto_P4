import pygame
from abstract_manager import *

class Levels_Manager(Abstract_Manager):

    def __init__(self):
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
