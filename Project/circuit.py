import pygame

# CONSTANTS
IMAGE_WIDTH = 600
IMAGE_HEIGHT = 400

class Circuit:

    def __init__(self,file,answer):
        self.image = pygame.transform.scale(pygame.image.load(file),(IMAGE_WIDTH,IMAGE_HEIGHT))
        self.answer = answer