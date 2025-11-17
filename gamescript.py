import pygame
import json
import os
from util import *
from random import randint
from background import background_maker
from warrior import Warrior
from labels import *
from titlescreen import Title_Screen
from zombie import Zombie
from gameoverscreen import Game_Over
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

#create lives
life_count = Lives()

#access saved high scores list, if no high scores create empty list (json info will be dumped into high score list, which will be local list that gamescript accesses)
if os.path.exists("savedhighscores.json"):
    with open("savedhighscores.json", "r") as f:
        high_scores = json.load(f)
else:
    high_scores = []

#create character
warrior_character = Warrior(zombie_group, life_count)

#creates opening game page
time_keep = Time_Labels()
title = Title_Screen()
gameover = Game_Over(high_scores)
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
        save_score = True
        #set game background
        screen.fill((0, 0, 0))
        background = background_maker()
        screen.blit(background, (0,0))

        #set warrior character
        warrior_character.update()
        warrior_character.draw(screen)

        #create zombie enemy
        zombie_group.update()
        zombie_group.draw(screen)  

        #draws updated life count
        life_count.draw(screen)

        #displays running time
        elapsed_time = (pygame.time.get_ticks() - t_zero) // 1000 #total run time - time elapsed on welcome screen
        mins, secs = divmod(elapsed_time, 60)
        time_keep.update_time(f"{mins:02}:{secs:02}")
        time_keep.draw(screen)
    
        #when three lives run out, end game
        if len(life_count.lives) == 0:
            state = "game_over"

    #ends game:grayscale screenshot of last position with game over text, top three high scores and option to restart game
    if state == "game_over":
        #save score (time value)
        if save_score == True:
            score = elapsed_time
            high_scores.append(score)
            with open ("savedhighscores.json", "w") as f:
                json.dump(high_scores, f)
            save_score = False

        #display game over screen
        die_screen = screen.copy()
        gray_background = pygame.transform.grayscale(die_screen)
        screen.blit(gray_background, (0,0))
        gameover.draw(screen)

        #restart game if player presses enter
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            #reset life count & time
            life_count = Lives()
            clock = pygame.time.Clock() 
            state = "game"

    pygame.display.flip()
    clock.tick(60)