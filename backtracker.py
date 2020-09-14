# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:13:28 2020

@author: Jon
"""

import numpy as np


class Backtrack(object):
    
    def __init__(self):
        
        self.board_history = {}
        self.mcv_words_history = {}
        self.mcv_key_history = {}
        self.bookmark = 0
        
    def setBacktrack(self, board, words, mcv_key):
        
        
        self.board_history[self.bookmark] = np.array(board, dtype = np.unicode_)
        self.mcv_words_history[self.bookmark] = words
        self.mcv_key_history[self.bookmark] = mcv_key
        self.bookmark +=1
    
    def getBacktrack(self):
        
        for bookmark in range((self.bookmark)-1, -1, -1) :
            
            if len(self.mcv_words_history[bookmark]) >= 1:
                print(f'bookmark: {bookmark}')
                
                # self.bookmark = bookmark
                return self.mcv_words_history[bookmark] , self.board_history[bookmark], self.mcv_key_history[bookmark]
                                                                            
    def cleanBacktrack(self):
        
        bookmark = self.bookmark + 1
        
        try:
            self.board_history.pop(bookmark)
            self.mcv_words_history.pop(bookmark)
            self.mcv_key_history.pop(bookmark)
            bookmark +=1
        except KeyError:
            return
        