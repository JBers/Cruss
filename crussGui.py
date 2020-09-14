# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 22:03:34 2020

@author: Jon
"""

import pygame
from pygame.locals import *
import numpy as np

width = 800
height = 600

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Crussword Composer')
font = pygame.font.Font(None, 16)




class Box(object):
    def __init__(self):
        self.width = 0
        self.height = 0
        self.top = 0
        self.left = 0
        self.rect.topleft = self.top,self.left
        self.rect.width = self.width
        self.rect.height = self.height
        pass
    
    def set_width(self):
        pass
    
    def selected(self,x,y):
       is_selected = pygame.Rect.collidepoint((x,y))
       pass
    
def draw_first_screen():
    pass

def draw_board():
    pass

def draw_buttons():
    pass


running = True
new = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            letter = event.unicode
        elif event.type == pygame.MOUSEBUTTONEDOWN:
            pass
        elif event.type == pygame.MOUSEBUTTONUP:
            pass
        
        
        
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))
        screen.blit(background, (0, 0))
        
        if new:
            draw_first_screen()
        else:
            draw_board()
            draw_buttons()
        
        pygame.display.flip()
        pygame.time.wait(10)
        
        
        
        
        
        
        
        