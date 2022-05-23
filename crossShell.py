# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:37:10 2020

@author: Jon
"""


import makeRe
import fileManagerCruss as fm
import crossSolver as c
from nltk.corpus import words
import crussParse as cp






def CrussGuiMain(design,tkresults,add_wordfile="wordlists/fortest.txt"):
    board,backtrack = c.setupBoard(design)
    board.tk_gui_setter(tkresults)
    board.update_board()
    board.set_keys()
    board.tk_set_unitarys()
    print(board.get_unitarys())
    initial_board = board.tk_gui_getter().copy()
    
    
    add_wordlist = fm.getwordlist3(add_wordfile)
    wordlist = set(words.words('en')) | add_wordlist
    get_word = makeRe.get_word("union",add_wordlist)  #defines function for preferential word choice
    solvedboard = c.solveBoard(board, backtrack, wordlist, get_word)
    solvedboard.get_clues()
    cp.crussParse(solvedboard).save_as_pdf()
    return solvedboard.tk_gui_getter(), initial_board




