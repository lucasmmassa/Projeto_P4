import pygame
from abstract_manager import *

# CONSTANTS
button1_width = 200
button1_height = 70
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

class Menu_Manager(Abstract_Manager):
    def __init__(self):
        self.new_manager = None
        self.change_manager = False
        self.run = True
        #self.background = pygame.transform.scale(pygame.image.load('images/circuit.jpg'),(DISPLAY_WIDTH,DISPLAY_HEIGHT))
        self.game_title = 'Will it light up?'

    def text_objects(self, text, font, color):
        surface = font.render(text,True, color)
        return surface, surface.get_rect()

    def font_config(self,size):
        return pygame.font.Font('./fonts/The Led Display St.ttf', size)

    # abstract method
    def run_screen(self,screen):
        screen.fill((0, 0, 40))
        surface, rect = self.text_objects(self.game_title, self.font_config(50),(255,255,255))
        rect.center = (DISPLAY_WIDTH/2,DISPLAY_HEIGHT*(1/4))
        screen.blit(surface,rect)
        self.check_events(screen)

    def check_events(self,screen):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.run = False

            mouse = pygame.mouse.get_pos()
            if ((DISPLAY_WIDTH / 2) - (button1_width/2))<mouse[0]<((DISPLAY_WIDTH / 2) + (button1_width/2)) and DISPLAY_HEIGHT * (1 / 2.3)<mouse[1]<DISPLAY_HEIGHT * (1 / 2.3)+button1_height:
                pygame.draw.rect(screen, (204, 0, 0),((DISPLAY_WIDTH / 2) - (button1_width/2), DISPLAY_HEIGHT * (1 / 2.3), button1_width, button1_height))
                if pygame.mouse.get_pressed()[0]:
                    self.change_manager = True
                    self.new_manager = 1

            else:
                pygame.draw.rect(screen, (100, 100, 100),((DISPLAY_WIDTH / 2) - (button1_width/2), DISPLAY_HEIGHT * (1 / 2.3), button1_width, button1_height))

            bsurf1, brect1 = self.text_objects('Play', self.font_config(30),(255,255,255))
            brect1.center = ((DISPLAY_WIDTH/2),(DISPLAY_HEIGHT * (1 / 2.3) + button1_height/2))
            screen.blit(bsurf1,brect1)

            pygame.display.update()