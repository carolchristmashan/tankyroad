import pygame
from util import *
from random import randint
from labels import Lives

class Warrior(pygame.sprite.Sprite):
    def __init__(self,zombie_group, life_count, x=125 , y=HEIGHT-115):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("kenney_platformer-characters/PNG/Soldier/Poses/soldier_cheer1.png")
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.score = 0
        self.lane_width = 257
        self.x_right_bound = 896
        self.x_left_bound = 125
        self.zombie_group = zombie_group
        self.life_count = life_count
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            #right
            if event.key == pygame.K_RIGHT and self.x < self.x_right_bound:
                self.x += self.lane_width
            #left
            if event.key == pygame.K_LEFT and self.x > self.x_left_bound:
                self.x -= self.lane_width

    def update(self):
        # update the rect
        self.rect.center = (self.x, self.y)

        #check if collides with zombie
        zombie_collide = pygame.sprite.spritecollide(self, self.zombie_group,0)
        if zombie_collide:
            print("hit character")
            self.life_count.lives.pop()
            for z in zombie_collide:
                z.kill()
                
            