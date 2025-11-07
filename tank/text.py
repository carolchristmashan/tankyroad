import pygame
from util import *

class Labels():
    def __init__(self):
        self.text_font = pygame.font.Font('Kenney Blocks.ttf', 36)
        self.text_color = (255, 255, 255)
        self.score_surface = self.text_font.render(str(pygame.time.get_ticks() // 1000), 1, self.text_color)
        self.title_rect = self.score_surface.get_rect()
        self.title_rect_center = (40, 40)

    def update_time(self, time):
        self.score_surface = self.text_font.render(f"{time}", 1, self.text_color)

    def draw(self, screen):
        screen.blit(self.score_surface, ((20,20)))
    