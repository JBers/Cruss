# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 11:10:18 2020

@author: Jon
"""
import numpy as np

class Cross(object):
    
    def __init__(self, vert, horiz):
        self.vert = vert
        self.horiz = horiz
        self.board = np.ones((self.vert, self.horiz), dtype = np.unicode_)
        self.keys = {}
        
    def design_board(self, blocks):
        
        for block in blocks:
            self.board[block] = 0


    def set_keys(self):
        
        clue = 0
        word = ''
        for j in range(self.horiz):
            wordlength = 0
            clue +=1
            word = ''
            loc = []
            for i in range(self.vert):
                if self.board[(i,j)] != '0':
                    wordlength+=1
                    word = word + self.board[(i,j)]
                    loc.append((i,j))
                elif wordlength !=0:
                    self.keys[clue] = [word,wordlength,'vertical',loc, False]
                    wordlength = 0
                    clue +=1
                    word = ''
                    loc = []
            if wordlength !=0:
                self.keys[clue] = [word,wordlength,'vertical',loc, False]
                
        for i in range(self.vert):
            wordlength = 0
            clue +=1
            word = ''
            loc = []
            for j in range(self.horiz):
                if self.board[(i,j)] != '0':
                    wordlength+=1
                    word = word + self.board[(i,j)]
                    loc.append((i,j))
                elif wordlength !=0:
                    self.keys[clue] = [word,wordlength,'horizontal',loc, False]
                    wordlength = 0
                    clue +=1
                    word = ''
                    loc = []
            if wordlength !=0:
                self.keys[clue] = [word,wordlength,'horizontal',loc, False]
          
        return self.keys

    def get_keys(self):
        return self.keys  
    
    def update_keys(self, keys):
        self.keys = keys
        return
    
    def get_clues(self):
      
        for key in self.keys:
            print(f'{key:4} {self.keys[key][0]:15}{self.keys[key][2]:12}{self.keys[key][3][0]}')
        
    def update_key(self, key, word):
        self.keys[key][0] = word
        self.keys[key][4] = True
        return
    
    def update_board(self):
        for key in self.keys:
            letters = list(self.keys[key][0])
            locations = self.keys[key][3]
            if self.keys[key][4]:
                for i in range(len(letters)):
                    self.board[locations[i]] = letters[i]
                self.keys[key][4] = False
        return

    def get_board(self):
        return self.board 

    def set_board(self,board):
        self.board = np.array(board, dtype = np.unicode_)
        
