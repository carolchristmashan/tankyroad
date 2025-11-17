import pygame
from util import *
from random import randint
from background import background_maker
from warrior import Warrior
from labels import *
from titlescreen import Title_Screen
from zombie import Zombie
pygame.init()

#screen properites
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock() 
running = True

#####################################################################################



#####################################################################################

#potential lanes that the zombie can blit into
lanes = [123,380,637,894]

#create zombie enemies
zombie_enemy = Zombie()
zombie_group = pygame.sprite.Group()
for i in range(5):
    # make a new zombie and add to sprite group
    lane_spawn = randint(0,len(lanes)-1)
    zombie_group.add(Zombie(x=lanes[lane_spawn], y=0))

#create character
warrior_character = Warrior(zombie_group)

#creates opening game page
time_keep = Time_Labels()
title = Title_Screen()
state = "title"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #title screen with opening game message
        if state == "title":
            title.draw(screen)
        #if player presses enter, begin running game
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            state = "game"
            t_zero = pygame.time.get_ticks() #time elapsed on welcome screen
        if state == "game":
            warrior_character.check_event(event)
    
    if state == "game":
        #set game background
        screen.fill((0, 0, 0))
        background_maker(screen)

        #set warrior character
        warrior_character.update()
        warrior_character.draw(screen)

        #create lives
        life_count = Lives()
        life_count.draw(screen)

        #create zombie enemy
        zombie_group.update()
        zombie_group.draw(screen)  

        #displays running time
        elapsed_time = (pygame.time.get_ticks() - t_zero) // 1000 #total run time - time elapsed on welcome screen
        mins, secs = divmod(elapsed_time, 60)
        time_keep.update_time(f"{mins:02}:{secs:02}")
        time_keep.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()