import pygame
from util import *

#title screen when game begins

class Game_Over():
    def __init__(self, high_scores):
        #display "game over" text
        self.gameover_font = pygame.font.Font('Kenney Blocks.ttf', 60)
        self.text_color = (255, 255, 255)
        self.gameover_surface = self.gameover_font.render("GAME OVER", 1, self.text_color)
        self.title_rect = self.gameover_surface.get_rect(center=(WIDTH//2, (HEIGHT//2)-100))

        #display "high score" text
        self.highscore_font = pygame.font.Font('Kenney Blocks.ttf', 30)
        self.highscore_surface = self.highscore_font.render("HIGH SCORES:", 1, self.text_color)
        self.highscore_rect = self.highscore_surface.get_rect(center=(WIDTH//2, (HEIGHT//2)-36))

        #display high scores
        high_scores.sort(reverse=True)
        self.high_scores = high_scores
        print(self.high_scores)
        self.scores_to_display = []
        self.score_font = pygame.font.Font('Kenney Blocks.ttf', 30)

        #iterates for top three scores
        for i in range(3):
            #verifies that there are at least three scores in list to avoid error (first few runs won't have three scores)
            if i < len(high_scores):
                #convert top three times from high score list to min/sec display
                mins, secs = divmod(self.high_scores[i], 60)
                actual_score = (f"{mins:02}:{secs:02}")
            else:
                actual_score = "--:--"
            #create new score surface specific to score
            actual_score_surface = self.score_font.render(actual_score, 1, self.text_color)
            #get rect of each high score surface so displays in a horiztonal lsit format
            actual_score_rect = actual_score_surface.get_rect(center=(WIDTH//2, (HEIGHT//2)+(35*i)))
            #append to list of now formatted top three scores to actually display
            self.scores_to_display.append((actual_score_surface, actual_score_rect))

        #display enter to play again
        self.restart_font = pygame.font.Font('Kenney Blocks.ttf', 30)
        self.restart_surface = self.restart_font.render("press enter to restart", 1, self.text_color)
        self.restart_rect = self.restart_surface.get_rect(center=(WIDTH//2, (HEIGHT-227)))

    def draw(self, screen):
        #display GMAE OVER & HIGH SCORE & PRESS ENTER TO RESTART:
        screen.blit(self.gameover_surface, self.title_rect)
        screen.blit(self.highscore_surface, self.highscore_rect)
        screen.blit(self.restart_surface, self.restart_rect)

        #displays list of formatted top three scores
        for surface,rect in self.scores_to_display:
            screen.blit(surface,rect)