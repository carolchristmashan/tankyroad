import pygame
from util import *

class Display_HS():
    def __init__(self):
        self.title_font = pygame.font.Font('Kenney Blocks.ttf', 36)
        self.text_color = (255, 255, 255)
        self.highscore = self.title_font.render("NEW HIGH SCORE!", 1, self.text_color)
        self.highscore_rect = self.highscore.get_rect()
        self.highscore_rect = self.highscore.get_rect(center=(WIDTH//2, HEIGHT//2-30))

        self.start_time = pygame.time.get_ticks()  
        self.duration = 1000   #only display for one second                    

    def draw(self, screen):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time <= self.duration:
            screen.blit(self.highscore, self.highscore_rect)