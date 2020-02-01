import pygame
from abstract_manager import *

# CONSTANTS
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 70
IMAGE_WIDTH = 620
IMAGE_HEIGHT = 370

def generate_examples_circuits():
    return 1

class Tutorial_Manager(Abstract_Manager):
    def __init__(self):
        self.new_manager = None
        self.change_manager = False
        self.run = True
        self.message_text = 'Tutorial'
        self.message_config = pygame.font.Font('./fonts/The Led Display St.ttf', 50)
        self.button_config = pygame.font.Font('./fonts/The Led Display St.ttf', 30)

    def text_objects(self, text, font,color):
        surface = font.render(text,True,color)
        return surface, surface.get_rect()

    def font_config(self,size):
        return pygame.font.Font('./fonts/The Led Display St.ttf', size)

    def button(self, screen, msg, x, y, ic, ac, b_width, b_height, on_click):
        mouse = pygame.mouse.get_pos()

        if x + b_width > mouse[0] > x and y + b_height > mouse[1] > y:
            pygame.draw.rect(screen, ac, (x, y, b_width, b_height))
            if pygame.mouse.get_pressed()[0]:
                self.change_manager = True
                self.new_manager = on_click
        else:
            pygame.draw.rect(screen, ic, (x, y, b_width, b_height))

        textSurf, textRect = self.text_objects(msg, self.button_config, (255, 255, 255))
        textRect.center = ((x + (b_width / 2)), (y + (b_height / 2)))
        screen.blit(textSurf, textRect)

    def run_screen(self,screen):
        screen.fill((0,0,150))
        surface, rect = self.text_objects(self.message_text, self.message_config,(255,255,255))
        rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * (1 / 4))
        screen.blit(surface, rect)
        self.check_events(screen)

    def check_events(self, screen):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            file_path = './images/tutorial/tutorial_info.png'
            image_info = pygame.transform.scale(pygame.image.load(file_path),(IMAGE_WIDTH,IMAGE_HEIGHT))

            screen.blit(image_info, (80,190))

            self.button(screen, 'Back', 10, 10, (100, 100, 100),(51, 153, 102), BUTTON_WIDTH, BUTTON_HEIGHT,0)
            self.button(screen, 'Gates', 100, 370, (100,100,100), (51, 153, 102), BUTTON_WIDTH, BUTTON_HEIGHT,0)
            self.button(screen, 'Example', 100, 480, (100, 100, 100), (51, 153, 102), BUTTON_WIDTH, BUTTON_HEIGHT,5)

            pygame.display.update()


class Examples_Manager(Abstract_Manager):
    def __init__(self):
        self.example_circuits = []
        self.new_manager = None
        self.change_manager = False
        self.run = True
        self.message_text = 'Tutorial'
        self.message_config = pygame.font.Font('./fonts/The Led Display St.ttf', 50)
        self.button_config = pygame.font.Font('./fonts/The Led Display St.ttf', 30)

    def text_objects(self, text, font, color):
        surface = font.render(text, True, color)
        return surface, surface.get_rect()

    def font_config(self, size):
        return pygame.font.Font('./fonts/The Led Display St.ttf', size)

    def button(self, screen, msg, x, y, ic, ac, b_width, b_height, on_click):
        mouse = pygame.mouse.get_pos()

        if x + b_width > mouse[0] > x and y + b_height > mouse[1] > y:
            pygame.draw.rect(screen, ac, (x, y, b_width, b_height))
            if pygame.mouse.get_pressed()[0]:
                self.change_manager = True
                self.new_manager = on_click
        else:
            pygame.draw.rect(screen, ic, (x, y, b_width, b_height))

        textSurf, textRect = self.text_objects(msg, self.button_config,(255,255,255))
        textRect.center = ((x + (b_width / 2)), (y + (b_height / 2)))
        screen.blit(textSurf, textRect)

    def move_examples(self, screen, msg, x, y, ic, ac, b_width, b_height, on_click):
        mouse = pygame.mouse.get_pos()

        if x + b_width > mouse[0] > x and y + b_height > mouse[1] > y:
            pygame.draw.rect(screen, ac, (x, y, b_width, b_height))
            if pygame.mouse.get_pressed()[0]:
                self.new_manager = on_click
        else:
            pygame.draw.rect(screen, ic, (x, y, b_width, b_height))

        textSurf, textRect = self.text_objects(msg, self.button_config,(255,255,255))
        textRect.center = ((x + (b_width / 2)), (y + (b_height / 2)))
        screen.blit(textSurf, textRect)

    def run_screen(self,screen):
        screen.fill((0,0,150))
        surface, rect = self.text_objects(self.message_text, self.message_config,(255,255,255))
        rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * (1 / 4))
        screen.blit(surface, rect)
        self.check_events(screen)

    def check_events(self, screen):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            file_path = './images/tutorial/tutorial_info.png'
            image_info = pygame.transform.scale(pygame.image.load(file_path),(IMAGE_WIDTH,IMAGE_HEIGHT))

            screen.blit(image_info, (80,190))

            self.button(screen, 'Menu', 10, 10, (100, 100, 100),(51, 153, 102), BUTTON_WIDTH, BUTTON_HEIGHT,0)
            self.button(screen, '<', 200, 550, (100,100,100), (51, 153, 102), BUTTON_WIDTH - 100, BUTTON_HEIGHT - 50, 0)
            self.button(screen, '>', 500, 550, (100, 100, 100), (51, 153, 102), BUTTON_WIDTH - 100, BUTTON_HEIGHT - 50,0)


            pygame.display.update()