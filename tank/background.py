import pygame
from util import *
from random import randint

def background_maker(screen):
    background = pygame.Surface((WIDTH, HEIGHT))

    road = pygame.image.load("game_files/tileGrass_roadNorth.png")
    grass = pygame.image.load("game_files/tileGrass2.png")
    big_bush = pygame.image.load("game_files/treeGreen_large.png")
    small_bush = pygame.image.load("game_files/treeGreen_small.png")

    tile_width = road.get_width()
    tile_height = road.get_height()

    for y in range(0,HEIGHT, tile_height):
        background.blit(grass,(0,y))
        

    for i,x in enumerate(range(0, WIDTH, tile_width)):
        if i%2 == 0:
            background.blit(road,(x+(tile_width/2),0))
        else:
            background.blit(grass,(x+(tile_width/2),0))
        for y in range(0, HEIGHT, tile_height):
            if i%2 == 0:
                background.blit(road,(x+(tile_width/2),y))
            else:
                background.blit(grass,(x+(tile_width/2),y))

    background.blit(small_bush,(10, 100))

    background.blit(big_bush,(tile_width+50, 200))
    background.blit(small_bush,(tile_width+50, 160))

    background.blit(small_bush,(tile_width+120,555))

    background.blit(big_bush,(tile_width*2+180, 450))
    background.blit(small_bush,(tile_width*2+260, 525))

    background.blit(big_bush,(tile_width*3+320, 75))
    background.blit(small_bush,(tile_width*3+375, 30))

    background.blit(small_bush,(tile_width*3+320, 400))
    background.blit(small_bush,(tile_width*3+375, 420))

    background.blit(small_bush,(WIDTH-50, 370))
    screen.blit(background,(0,0))



