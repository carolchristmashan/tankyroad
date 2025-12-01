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
from newhighscore import Display_HS
pygame.init()
pygame.mixer.init()

#screen properites
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock() 
running = True

#music load for intro screen
pygame.mixer.music.load("intromusic.mp3")
#####################################################################################

#####################################################################################

#create zombie enemies & parameters for time to spawn randomly
zombie_enemy = Zombie()
zombie_group = []
zombie_spawn_time = 500
last_zombie_spawn = 0
zombie_sound = pygame.mixer.Sound("zombie.mp3")
zombie_sound.set_volume(0.4)

#potential lanes that the zombie can blit into
lanes = [123,380,637,894]

#create lives
life_count = Lives()

#access saved high scores list, if no high scores create empty list (json info will be dumped into high score list, which will be local list that gamescript accesses)
if os.path.exists("savedhighscores.json"):
    with open("savedhighscores.json", "r") as f:
        high_scores = json.load(f)
else:
    high_scores = []
HS_trigger = False

#creates opening game page
time_keep = Time_Labels()
title = Title_Screen()
high_scores.sort(reverse=True)
gameover = Game_Over(high_scores)
state = "title"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #title screen with opening game message
        if state == "title":
            title.draw(screen)
            #play apoaloypse alarm blaring intro music
            pygame.mixer.music.play(-1)

        #if player presses enter, begin running game
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            state = "game"
            #reset lives & time
            t_zero = pygame.time.get_ticks()
            life_count = Lives()
            #warrior character
            zombie_group = pygame.sprite.Group()
            warrior_character = Warrior(zombie_group, life_count)
            save_score = True
            #play creepy apoclypse music
            pygame.mixer.music.load("gamemusic.mp3")
            pygame.mixer.music.play(-1)

        if state == "game":
            warrior_character.check_event(event)
    
    if state == "game":
        #create zombies at random times
         #play zombie sound effect
        current_time = pygame.time.get_ticks()
        if current_time - last_zombie_spawn > zombie_spawn_time:
            #play zombie sound, but check so sound doenst play again if already playing (from zombie already spawned)
            if not pygame.mixer.Channel(1).get_busy():
                pygame.mixer.Channel(1).play(zombie_sound)
            #spawn zombie
            lane_spawn = randint(0, len(lanes)-1)
            zombie_group.add(Zombie(x=lanes[lane_spawn], y=0))
            last_zombie_spawn = current_time
            zombie_spawn_time = randint(600,1000) #next zombie spawn between .6 and 1 second

        save_score = True
        #set game background
        screen.fill((0, 0, 0))
        background = background_maker()
        screen.blit(background, (0,0))

        #set warrior character
        warrior_character.update(event)
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
        if elapsed_time > high_scores[0] and HS_trigger == False:
            HS_alert = Display_HS()
            HS_alert.draw(screen)
            HS_trigger = True
            pygame.mixer.music.load("highscore.mp3")
            pygame.mixer.music.play()
        
        if HS_trigger:
            HS_alert.draw(screen)
    
        #when three lives run out, end game
        if len(life_count.lives) == 0:
            state = "game_over"

    #ends game:grayscale screenshot of last position with game over text, top three high scores and option to restart game
    if state == "game_over":
        #save score (time value)
        if save_score == True:
            score = elapsed_time
            high_scores.append(score)
            high_scores.sort(reverse = True)
            with open ("savedhighscores.json", "w") as f:
                json.dump(high_scores, f)
            save_score = False
            pygame.mixer.music.load("gameover.mp3")
            pygame.mixer.music.play()

        #display game over screen
        gameover = Game_Over(high_scores)
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