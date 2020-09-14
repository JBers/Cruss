# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:37:10 2020

@author: Jon
"""

import crossClass
import makeRe
import backtracker
import boardDesigns
import fileManagerCruss as fm
import crossSolver as c

designB = [9,9,[(0,0),(0,1),(0,7),(0,8),(1,0),(1,8),(7,8),(0,6),(1,6),(7,6),(8,6),(7,2),(8,2),(1,1),(1,7),(0,2),(1,2),(7,0),(3,4),(4,3),(4,4),(4,5),(5,4),(7,1),(7,7),(8,0),(8,1),(8,7),(8,8)]]
board,backtrack = c.setupBoard(designB)
board.update_key(23,'backstrap')
# board.update_key(30,'breakfast')

board.update_board()
board.set_keys()
# print(board.get_board())
# print(board.get_keys())


# print(board.get_keys())
# print(board.get_board())
wordlist = fm.getwordlist('renameWordlist.txt')
solvedboard = c.solveBoard(board, backtrack, wordlist)
print(solvedboard.get_board())
solvedboard.get_clues()