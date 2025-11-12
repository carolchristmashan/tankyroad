import pygame
from util import *
from random import randint
from background import background_maker
from warrior import Warrior
from text import Labels
from titlescreen import Title_Screen
pygame.init()

#screen properites
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock() 
running = True

#####################################################################################





#####################################################################################

warrior_character = Warrior()
time_keep = Labels()
title = Title_Screen()
state = "title"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if state == "title":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                state = "game"
                t_zero = pygame.time.get_ticks()
        elif state == "game":
            warrior_character.check_event(event)
            

    screen.fill((0, 0, 0))  # clear screen

    if state == "title":
        title.draw(screen)
    elif state == "game":
        background_maker(screen)
        warrior_character.update()
        warrior_character.draw(screen)

        elapsed_time = (pygame.time.get_ticks() - t_zero) // 1000
        mins, secs = divmod(elapsed_time, 60)
        time_keep.update_time(f"{mins:02}:{secs:02}")
        time_keep.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()