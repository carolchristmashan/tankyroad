import pygame
from util import *
from random import randint
from background import background_maker
pygame.init()

#screen properites
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

background_maker()

#####################################################################################


#####################################################################################


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # flip() the display to put your work on screen
  
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()