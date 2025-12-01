import pygame
from util import *

#creates zombie that moves down the lane
class Zombie(pygame.sprite.Sprite):
    def __init__(self, x=90 , y=-50, vy=3):
        pygame.sprite.Sprite.__init__(self)
        self.walk1 = pygame.image.load("kenney_platformer-characters/PNG/Zombie/Poses/zombie_walk1.png")
        self.walk2 = pygame.image.load("kenney_platformer-characters/PNG/Zombie/Poses/zombie_walk2.png")
        self.zombie_walking = [self.walk1, self.walk2]
        self.x = x
        self.y = y
        self.vy = vy
        self.rect = self.walk1.get_rect(topleft = (self.x, self.y))
        self.walk_time = 0
        self.walk_time_switch = 250
        self.current_frame = 0

    def update(self):
        #animated walk
        self.y += self.vy
        self.rect.center = (self.x, self.y)
        self.current_time = pygame.time.get_ticks()
        if (self.current_time - self.walk_time) > self.walk_time_switch:
            self.current_frame = (self.current_frame + 1) % len(self.zombie_walking)
            self.image = self.zombie_walking[self.current_frame]
            self.walk_time = self.current_time


    def draw(self, screen):
        screen.blit(self.image,self.rect)
    