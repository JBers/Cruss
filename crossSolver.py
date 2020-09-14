# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:17:09 2020

@author: Jon
"""

import crossClass
import makeRe
import backtracker
import boardDesigns
import fileManagerCruss as fm

def setupBoard(design):
    
    vertical = design[0]
    horizontal = design[1]
    blocks = design[2]
    
    crossword = crossClass.Cross(vertical,horizontal)
    crossword.design_board(blocks)
    crossword.set_keys()
    
    backtrack = backtracker.Backtrack()
    
    return crossword, backtrack

    

def solveBoard(board, backtrack, wordlist):
    
    done = False
    key_track = 1000
    
    while done is False:   
        
        print(board.get_board())
        
        keys = board.get_keys()
        mcv_key, words, check = makeRe.find_mcv2(keys, wordlist)
        
        # regex = makeRe.make_regex(keys[mcv_key])
        # # print(f'Searching on clue {mcv_key} : {keys[mcv_key][0]}')
        # words = makeRe.find_words(regex, wordlist)
        
        if check:
            print('checking if done...')
            if makeRe.is_words(keys, wordlist):
                done = True
                print('done')
                return board
            print('backtracking on is_words')
            words, board_prev, mcv_key = backtrack.getBacktrack()
            # backtrack.cleanBacktrack()
            # input('Continue? \n')
            board.set_board(board_prev)
            board.set_keys()
            
        
        
        # print(f'Saving board.')
        if len(words) == 0:
            
            print('backtracking...')
            
            words, board_prev, mcv_key = backtrack.getBacktrack()

            print(f'Backtracking to clue {mcv_key}')
            # backtrack.cleanBacktrack()
            print(f'Current length of words: {len(words)}, for clue {mcv_key} : {keys[mcv_key][0]}')
            
            board.set_board(board_prev)
            board.set_keys()
            # print(board.get_board())
            # input('Continue? \n')
            
         
            
        word = makeRe.get_rand_word(words)
        # word = words.pop()
        print(f'Trying {word} in clue {mcv_key}.') 
        
        if mcv_key != key_track:
            backtrack.setBacktrack(board.get_board(),words,mcv_key)
        
        board.update_key(mcv_key,word)
        board.update_board()
        board.set_keys()
        
        
            
        key_track = mcv_key  
    
    return board

