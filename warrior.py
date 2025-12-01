import pygame
from util import *
from random import randint
from labels import Lives

class Warrior(pygame.sprite.Sprite):
    def __init__(self,zombie_group, life_count, x=125 , y=HEIGHT-115):
        pygame.sprite.Sprite.__init__(self)
        self.walk1 = pygame.image.load("kenney_platformer-characters/PNG/Soldier/Poses/soldier_walk1.png")
        self.walk2 = pygame.image.load("kenney_platformer-characters/PNG/Soldier/Poses/soldier_walk2.png")
        self.jump1 = pygame.image.load("kenney_platformer-characters/PNG/Soldier/Poses/soldier_idle.png")
        self.jump2 = pygame.image.load("kenney_platformer-characters/PNG/Soldier/Poses/soldier_jump.png")
        self.hurt = pygame.image.load("kenney_platformer-characters/PNG/Soldier/Poses/soldier_hurt.png")
        self.warrior_walking = [self.walk1, self.walk2]
        self.warrior_jump = [self.jump1, self.jump2]
        self.x = x
        self.y = y
        self.rect = self.walk1.get_rect()
        self.rect.topleft = (x,y)
        self.score = 0
        self.lane_width = 257
        self.x_right_bound = 896
        self.x_left_bound = 125
        self.zombie_group = zombie_group
        self.life_count = life_count
        self.rect = self.walk1.get_rect(topleft = (self.x, self.y))
        self.walk_time = 0
        self.walk_time_switch = 250
        self.current_frame = 0
        self.is_hurt = False
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            #right
            if event.key == pygame.K_RIGHT and self.x < self.x_right_bound:
                self.x += self.lane_width
                self.current_time = pygame.time.get_ticks()
                if (self.current_time - self.walk_time) > self.walk_time_switch:
                    self.current_frame = (self.current_frame + 1) % len(self.warrior_jump)
                    self.image = self.warrior_jump[self.current_frame]
                    self.walk_time = self.current_time
            #left
            if event.key == pygame.K_LEFT and self.x > self.x_left_bound:
                self.x -= self.lane_width

    def update(self, event):
        # update the rect
        self.rect.center = (self.x, self.y)
        #walking animation
        self.current_time = pygame.time.get_ticks()
        if (self.current_time - self.walk_time) > self.walk_time_switch:
            self.current_frame = (self.current_frame + 1) % len(self.warrior_walking)
            self.image = self.warrior_walking[self.current_frame]
            self.walk_time = self.current_time
        #display hurt image if condition true
        if self.is_hurt == True:
            if pygame.time.get_ticks() < self.hold_hurt_time:
                self.image = self.hurt
                return
            else:
                self.is_hurt = False 
                self.walk_time = pygame.time.get_ticks() 

        #check if collides with zombie
        zombie_collide = pygame.sprite.spritecollide(self, self.zombie_group,0)
        if zombie_collide:
            print("hit character")
            collide_sound = pygame.mixer.Sound("warrior.mp3")
            collide_sound.play()
            #take off a life from display & remove zombie
            self.life_count.lives.pop()
            for z in zombie_collide:
                z.kill()
            #set conditions to display hurt image
            self.is_hurt = True
            self.hold_hurt_time = pygame.time.get_ticks() + 200
            self.time = pygame.time.get_ticks()
            self.image = self.hurt
    
                
            
