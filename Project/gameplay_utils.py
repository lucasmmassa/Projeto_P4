import pygame
from abstract_manager import *
from circuit import Circuit

# CONSTANTS
led_on = './images/led-on.png'
led_off = './images/led-off.png'
path0 = './normal/0'
path1 = './normal/1'
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100

def generate_circuits(path,answer):
    list = []
    filepath = './normal/1/1.png'
    element = Circuit(filepath,answer)
    list.append(element)
    return list

class Normal_Manager(Abstract_Manager):

    def __init__(self):
        self.new_manager = None
        self.change_manager = False
        self.difficulty = None
        self.verify = False
        self.run = True
        self.actual_answer = None
        self.real_answer = None
        self.message_text = 'Will it light up?'
        self.message_config = pygame.font.Font('./fonts/The Led Display St.ttf', 40)
        self.button_config = pygame.font.Font('./fonts/The Led Display St.ttf', 30)
        self.feedback_config = pygame.font.Font('./fonts/The Led Display St.ttf', 70)
        self.circuits1 = generate_circuits(path1,1)
        self.circuits0 = []

    def text_objects(self, text, font,color):
        surface = font.render(text,True,color)
        return surface, surface.get_rect()

    def font_config(self,size):
        return pygame.font.Font('./fonts/The Led Display St.ttf', size)

    def answer(self, screen, msg, x, y, ic, ac, on_click):
        mouse = pygame.mouse.get_pos()

        if x + BUTTON_WIDTH > mouse[0] > x and y + BUTTON_HEIGHT > mouse[1] > y:
            pygame.draw.rect(screen, ac, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT))
            if pygame.mouse.get_pressed()[0]:
                self.actual_answer = on_click
                self.verify = True
        else:
            pygame.draw.rect(screen, ic, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT))

        textSurf, textRect = self.text_objects(msg, self.button_config,(255,255,255))
        textRect.center = ((x + (BUTTON_WIDTH / 2)), (y + (BUTTON_HEIGHT / 2)))
        screen.blit(textSurf, textRect)

    def run_screen(self,screen):
        screen.fill((255, 255, 255))
        image = self.circuits1[0].image
        self.real_answer = self.circuits1[0].answer
        screen.blit(image,(0,150))
        surface, rect = self.text_objects(self.message_text, self.message_config,(0,0,40))
        rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * (1 / 5))
        screen.blit(surface, rect)
        self.check_events(screen)

    def check_events(self,screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            self.answer(screen, 'Yes', 600, DISPLAY_HEIGHT * (1 / 2.3), (0,0,40), (255,0,0), 1)
            self.answer(screen, 'No', 600, DISPLAY_HEIGHT * (1 / 1.5), (0,0,40), (100,100,100), 0)

            if self.verify:
                led = None
                if self.actual_answer == self.real_answer:
                    screen.fill((0,120,0))
                    surf, rec = self.text_objects(('Right Answer!'), self.feedback_config, (255,255,255))
                    rec.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * (1 / 3.5))
                    led = pygame.image.load(led_on)
                else:
                    screen.fill((100,100,100))
                    surf, rec = self.text_objects(('Wrong Answer!'), self.feedback_config, (255, 0, 0))
                    rec.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * (1 / 3.5))
                    led = pygame.image.load(led_off)
                screen.blit(surf,rec)
                screen.blit(led,(272,250))

            pygame.display.update()

class Hard_Manager(Abstract_Manager):

    def __init__(self):
        self.new_manager = None
        self.change_manager = False
        self.difficulty = None
        self.run = True

    def run_screen(self,screen):
        pass

    def check_events(self,screen):
        pass