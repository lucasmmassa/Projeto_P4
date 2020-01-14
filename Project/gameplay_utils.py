import pygame
from abstract_manager import *
from circuit import Circuit
from random import shuffle
import glob

# CONSTANTS
led_on = './images/led-on.png'
led_off = './images/led-off.png'
data1 = ('./normal/0/*.png', 0)   # tuples containing path and answer
data2 = ('./normal/1/*.png', 1)
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
ANSWER_WIDTH = 100
ANSWER_HEIGHT = 100
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
LEDS_IMAGES = (pygame.image.load(led_off), pygame.image.load(led_on))


def generate_circuits(list,data):
    for file in glob.glob(data[0]):
        element = Circuit(file,data[1])
        list.append(element)
    return list

# Superclass
class Gameplay_Manager(Abstract_Manager):

    def __init__(self):
        self.new_manager = None
        self.change_manager = False
        self.difficulty = None
        self.verify = False
        self.run = True
        self.actual_answer = None
        self.real_answer = None
        self.message_text = 'Will it light up?'
        self.message_config = pygame.font.Font('./fonts/The Led Display St.ttf', 50)
        self.button_config = pygame.font.Font('./fonts/The Led Display St.ttf', 30)
        self.feedback_config = pygame.font.Font('./fonts/The Led Display St.ttf', 70)
        self.rounds = 10
        self.score = 0
        self.index = 0

    def text_objects(self, text, font,color):
        surface = font.render(text,True,color)
        return surface, surface.get_rect()

    def font_config(self,size):
        return pygame.font.Font('./fonts/The Led Display St.ttf', size)

    def button(self, screen, msg, x, y, ic, ac, on_click):   # render the general buttons
        mouse = pygame.mouse.get_pos()

        if x + BUTTON_WIDTH > mouse[0] > x and y + BUTTON_HEIGHT > mouse[1] > y:
            pygame.draw.rect(screen, ac, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT))
            if pygame.mouse.get_pressed()[0]:
                self.change_manager = True
                self.new_manager = on_click
        else:
            pygame.draw.rect(screen, ic, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT))

        textSurf, textRect = self.text_objects(msg, self.button_config,(0, 0, 40))
        textRect.center = ((x + (BUTTON_WIDTH / 2)), (y + (BUTTON_HEIGHT / 2)))
        screen.blit(textSurf, textRect)

    def answer(self, screen, msg, x, y, ic, ac, on_click):   # render the answer buttons
        mouse = pygame.mouse.get_pos()

        if x + ANSWER_WIDTH > mouse[0] > x and y + ANSWER_HEIGHT > mouse[1] > y:
            pygame.draw.rect(screen, ac, (x, y, ANSWER_WIDTH, ANSWER_HEIGHT))
            if pygame.mouse.get_pressed()[0]:
                self.actual_answer = on_click
                self.verify = True
        else:
            pygame.draw.rect(screen, ic, (x, y, ANSWER_WIDTH, ANSWER_HEIGHT))

        textSurf2, textRect2 = self.text_objects(msg, self.button_config,(255,255,255))
        textRect2.center = ((x + (ANSWER_WIDTH / 2)), (y + (ANSWER_HEIGHT / 2)))
        screen.blit(textSurf2, textRect2)

    def run_screen(self,screen):
        screen.fill((255, 255, 255))
        image = self.circuits[self.index].image
        self.real_answer = self.circuits[self.index].answer
        screen.blit(image,(0,150))
        surface, rect = self.text_objects(self.message_text, self.message_config,(255, 0, 0))
        rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * (1 / 5))
        screen.blit(surface, rect)
        self.check_events(screen)

    def check_events(self,screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            # Display the Menu button
            self.button(screen,'Menu',0,0,(255, 255, 255), (51, 153, 102), 0)

            # Display the answer buttons
            self.answer(screen, 'Yes', 600, DISPLAY_HEIGHT * (1 / 2.3), (0,0,40), (255,0,0), 1)
            self.answer(screen, 'No', 600, DISPLAY_HEIGHT * (1 / 1.5), (0,0,40), (100,100,100), 0)

            # Verifies if the answer was right or wrong
            if self.verify:
                led = LEDS_IMAGES[self.real_answer]
                if self.actual_answer == self.real_answer:
                    screen.fill((0,120,0))
                    surf, rec = self.text_objects(('Right Answer!'), self.feedback_config, (255,255,255))
                    rec.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * (1 / 3.5))
                    self.score += 1  # increases the score
                else:
                    screen.fill((255,0,0))
                    surf, rec = self.text_objects(('Wrong Answer!'), self.feedback_config, (255,255,255))
                    rec.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * (1 / 3.5))
                screen.blit(surf,rec)
                screen.blit(led,(272,250))
                self.index += 1 # increases the index of the circuit list
                self.verify = False
                pygame.display.update()
                pygame.time.wait(3000)

            if self.index == self.rounds:
                screen.fill((100, 0, 255))
                surf, rec = self.text_objects(('SCORED: ' + str(self.score)+' / '+ str(self.rounds)), self.feedback_config, (255, 255, 255))
                rec.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * (1 / 2))
                screen.blit(surf, rec)
                pygame.display.update()
                pygame.time.wait(5000)
                self.new_manager = 0
                self.change_manager = True

            pygame.display.update()


# Inheritance
class Normal_Manager(Gameplay_Manager):
    def __init__(self):
        super().__init__()
        self.circuits = []
        self.circuits = generate_circuits(self.circuits,data1)
        self.circuits = generate_circuits(self.circuits, data2)
        shuffle(self.circuits)



# Inheritance
class Hard_Manager(Gameplay_Manager):

    def __init__(self):
        super().__init__()