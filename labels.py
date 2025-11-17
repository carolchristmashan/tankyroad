import pygame
from util import *

#creates time & life count

class Time_Labels():
    def __init__(self, x=WIDTH-20, y=20):
        #time display
        self.text_font = pygame.font.Font('Kenney Blocks.ttf', 36)
        self.text_color = (255, 255, 255)
        self.score_surface = self.text_font.render(str(pygame.time.get_ticks() // 1000), 1, self.text_color)
        self.title_rect = self.score_surface.get_rect()
        self.title_rect_center = (40, 40)

    def update_time(self, time):
        self.score_surface = self.text_font.render(f"{time}", 1, self.text_color)

    def draw(self, screen):
        screen.blit(self.score_surface, ((20,20)))

class Lives():
    def __init__(self, x=WIDTH-20, y=20):
        #life display
        self.life1 = pygame.image.load("kenney_board-game-icons/PNG/Double (128px)/skull.png")
        self.life2 = pygame.image.load("kenney_board-game-icons/PNG/Double (128px)/skull.png")
        self.life3 = pygame.image.load("kenney_board-game-icons/PNG/Double (128px)/skull.png")
        self.life1 = pygame.transform.rotozoom(self.life1, 0, 0.3)
        self.life2 = pygame.transform.rotozoom(self.life2, 0, 0.3)
        self.life3 = pygame.transform.rotozoom(self.life3, 0, 0.3)
        self.life1_x = x
        self.life1_y = y
        self.life2_x = x
        self.life2_y = y
        self.life3_x = x
        self.life3_y = y
        self.lives = [self.life1, self.life2, self.life3]

    def draw(self, screen):
        counter = 1
        for i in range(0,len(self.lives)):
            screen.blit(self.lives[i], ((WIDTH-(60*counter),20)))
            counter = counter + 1


    