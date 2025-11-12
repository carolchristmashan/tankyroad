import pygame
from util import *

class Title_Screen():
    def __init__(self):
        self.title_font = pygame.font.Font('Kenney Blocks.ttf', 36)
        self.instructions_font = pygame.font.Font('Kenney Blocks.ttf', 24)
        self.text_color = (255, 255, 255)
        self.title_surface = self.title_font.render("Welcome to the Jungle", 1, self.text_color)
        self.instructions_surface = self.instructions_font.render("Press enter to play", 1, self.text_color)
        self.title_rect = self.title_surface.get_rect()
        self.title_rect = self.title_surface.get_rect(center=(WIDTH//2, HEIGHT//2-30))
        self.instructions_rect = self.instructions_surface.get_rect()
        self.instructions_rect = self.instructions_surface.get_rect(center=(WIDTH//2, HEIGHT//2+20))

    def draw(self, screen):
        screen.blit(self.title_surface, self.title_rect)
        screen.blit(self.instructions_surface, self.instructions_rect)