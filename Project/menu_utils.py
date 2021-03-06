import pygame
from abstract_manager import *

# CONSTANTS
button1_width = 200
button1_height = 70
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 70

class Menu_Manager(Abstract_Manager):
    def __init__(self):
        self.new_manager = None
        self.change_manager = False
        self.run = True
        self.background = pygame.transform.scale(pygame.image.load('images/background.png'),(DISPLAY_WIDTH,DISPLAY_HEIGHT))
        self.game_title = 'Will it light up?'
        self.button_config = pygame.font.Font('./fonts/The Led Display St.ttf', 30)

    def text_objects(self, text, font, color):
        surface = font.render(text,True, color)
        return surface, surface.get_rect()

    def font_config(self,size):
        return pygame.font.Font('./fonts/The Led Display St.ttf', size)

    def button(self, screen, msg, x, y, ic, ac, on_click):
        mouse = pygame.mouse.get_pos()

        if x + BUTTON_WIDTH > mouse[0] > x and y + BUTTON_HEIGHT > mouse[1] > y:
            pygame.draw.rect(screen, ac, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT))
            if pygame.mouse.get_pressed()[0]:
                self.change_manager = True
                self.new_manager = on_click
        else:
            pygame.draw.rect(screen, ic, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT))

        textSurf, textRect = self.text_objects(msg, self.button_config,(255,255,255))
        textRect.center = ((x + (BUTTON_WIDTH / 2)), (y + (BUTTON_HEIGHT / 2)))
        screen.blit(textSurf, textRect)

    # abstract method
    def run_screen(self,screen):
        #screen.fill((0, 0, 40))
        screen.blit(self.background,(0,0))
        surface, rect = self.text_objects(self.game_title, self.font_config(50),(255,255,255))
        rect.center = (DISPLAY_WIDTH/2,DISPLAY_HEIGHT*(1/4))
        screen.blit(surface,rect)
        self.check_events(screen)

    def check_events(self,screen):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.run = False

            self.button(screen, 'Play', 300, 250, (100,100,100), (240,0,5), 1)
            self.button(screen, 'Tutorial', 300, 350, (100,100,100), (23,153, 97), 4)

            # mouse = pygame.mouse.get_pos()
            # if ((DISPLAY_WIDTH / 2) - (button1_width/2))<mouse[0]<((DISPLAY_WIDTH / 2) + (button1_width/2)) and DISPLAY_HEIGHT * (1 / 2.3)<mouse[1]<DISPLAY_HEIGHT * (1 / 2.3)+button1_height:
            #     pygame.draw.rect(screen, (204, 0, 0),((DISPLAY_WIDTH / 2) - (button1_width/2), DISPLAY_HEIGHT * (1 / 2.3), button1_width, button1_height))
            #     if pygame.mouse.get_pressed()[0]:
            #         self.change_manager = True
            #         self.new_manager = 1
            #
            # else:
            #     pygame.draw.rect(screen, (100, 100, 150),((DISPLAY_WIDTH / 2) - (button1_width/2), DISPLAY_HEIGHT * (1 / 2.3), button1_width, button1_height))
            #
            # bsurf1, brect1 = self.text_objects('Play', self.font_config(30),(255,255,255))
            # brect1.center = ((DISPLAY_WIDTH/2),(DISPLAY_HEIGHT * (1 / 2.3) + button1_height/2))
            # screen.blit(bsurf1,brect1)

            pygame.display.update()