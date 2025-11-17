import pygame
from util import *

#creates zombie that moves down the lane
class Zombie(pygame.sprite.Sprite):
    def __init__(self, x=90 , y=-50, vy=3):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("kenney_platformer-characters/PNG/Zombie/Poses/zombie_stand.png")
        self.x = x
        self.y = y
        self.vy = vy
        self.rect = self.image.get_rect(topleft = (self.x, self.y))

    def update(self):
        self.y += self.vy
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image,self.rect)
    