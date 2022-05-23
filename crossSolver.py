# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:17:09 2020

@author: Jon
"""

import crossClass
import makeRe
import backtracker


def setupBoard(design):
    
    vertical = design.get_vertical()
    horizontal = design.get_horizontal()
    blocks = design.get_blocks()
    
    crossword = crossClass.Cross(vertical,horizontal)
    crossword.design_board(blocks)
    crossword.set_keys()
    
    backtrack = backtracker.Backtrack()
    
    return crossword, backtrack

    

def solveBoard(board, backtrack, wordlist, get_word):
    
    done = False
    first = True
    key_track = 1000
    
    
    while done is False:   
        
        
        
        keys = board.get_keys()
        mcv_key, words, check = makeRe.find_mcv2(keys, wordlist, backtrack.getMemotrack())
        if first:
            backtrack.setBacktrack(board.get_board(),words,mcv_key)
            first = False
        
        if check:
            print('checking if done...')
            if makeRe.is_words(keys, wordlist, unitarys = board.get_unitarys()):
                done = True
                print('done')
                return board
            # print('backtracking on is_words')
            words, board_prev, mcv_key = backtrack.getBacktrack()
            
            board.set_board(board_prev)
            board.set_keys()
            
        
        
        # print(f'Saving board.')
        if len(words) == 0:
            
            # print('backtracking...')
            try:
                words, board_prev, mcv_key = backtrack.getBacktrack()

                # print(f'Backtracking to clue {mcv_key}')
                
                # print(f'Current length of words: {len(words)}, for clue {mcv_key} : {keys[mcv_key][0]}')
                
                board.set_board(board_prev)
                board.set_keys()
                
            except TypeError:
                print("No solution found")
                return board
             
        no_dupes = [keys[key][0] for key in keys if '1' not in keys[key][0]]
        
        word = get_word(words,no_dupes)
    
        
        # print(f'Trying {word} in clue {mcv_key}.') 
        # input("Press NE")
        
        if mcv_key != key_track:
            backtrack.setBacktrack(board.get_board(),words,mcv_key)
        
        board.update_key(mcv_key,word)
        board.update_board()
        board.set_keys()
        
        
            
        key_track = mcv_key  
    
    return board

