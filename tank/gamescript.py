import pygame
from util import *
from random import randint
from background import background_maker
from warrior import Warrior
from text import Labels
pygame.init()

#screen properites
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

#####################################################################################

#####################################################################################

warrior_character = Warrior()
time_keep = Labels()

while running:
    background_maker(screen)
    # poll for events

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        warrior_character.check_event(event)
        warrior_character.update()
        if event.type == pygame.QUIT:
            running = False
    warrior_character.draw(screen)

    #print time
    elapsed_time = pygame.time.get_ticks() // 1000 #gets time from ms to s
    mins = elapsed_time // 60
    secs = elapsed_time % 60
    time_keep.update_time(f"{mins:02}:{secs:02}")
    time_keep.draw(screen)

    # flip() the display to put your work on screen
  
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()