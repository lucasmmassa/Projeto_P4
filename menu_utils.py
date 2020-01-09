import pygame
from levels_utils import *
from abstract_manager import *
from constants import *

# CONSTANTS
button1_width = 200
button1_height = 70

class Menu_Manager(Abstract_Manager):
    def __init__(self):
        self.run = True
        #self.background = pygame.transform.scale(pygame.image.load('images/circuit.jpg'),(DISPLAY_WIDTH,DISPLAY_HEIGHT))
        self.game_title = 'Will it light up?'
        self.title_config = pygame.font.Font('./fonts/The Led Display St.ttf', 50)
        self.button1_text = 'Play'
        self.button1_font = pygame.font.Font('./fonts/The Led Display St.ttf', 30)

    def text_objects(self, text, font):
        surface = font.render(text,True,(255,255,255))
        return surface, surface.get_rect()

    # abstract method
    def run_screen(self,screen):
        screen.fill((0,0,0))
        surface, rect = self.text_objects(self.game_title, self.title_config)
        rect.center = (DISPLAY_WIDTH/2,DISPLAY_HEIGHT*(1/4))
        screen.blit(surface,rect)
        pygame.draw.rect(screen, (100, 100, 100), ((DISPLAY_WIDTH / 2) - (button1_width / 2), DISPLAY_HEIGHT * (1 / 2.3), button1_width, button1_height))

        manager_num = self.check_events(screen)
        return manager_num


    def check_events(self,screen):
        manager_num = 0

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.run = False

            mouse = pygame.mouse.get_pos()
            if ((DISPLAY_WIDTH / 2) - (button1_width/2))<mouse[0]<((DISPLAY_WIDTH / 2) + (button1_width/2)) and DISPLAY_HEIGHT * (1 / 2.3)<mouse[1]<DISPLAY_HEIGHT * (1 / 2.3)+button1_height:
                pygame.draw.rect(screen, (204, 0, 0),((DISPLAY_WIDTH / 2) - (button1_width/2), DISPLAY_HEIGHT * (1 / 2.3), button1_width, button1_height))
                if pygame.mouse.get_pressed()[0]:
                    manager_num = 1

            else:
                pygame.draw.rect(screen, (100, 100, 100),((DISPLAY_WIDTH / 2) - (button1_width/2), DISPLAY_HEIGHT * (1 / 2.3), button1_width, button1_height))

            bsurf1, brect1 = self.text_objects(self.button1_text,self.button1_font)
            brect1.center = ((DISPLAY_WIDTH/2),(DISPLAY_HEIGHT * (1 / 2.3) + button1_height/2))
            screen.blit(bsurf1,brect1)

            pygame.display.update()

        return manager_num