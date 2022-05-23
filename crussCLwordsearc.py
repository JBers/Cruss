# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 15:06:45 2021

@author: Jon
"""

import re
import fileManagerCruss as fm
from nltk.corpus import words


def wordsearch(add_wordfile='wordlists/computerywords.txt'):
    
    pattern = input("String to search on? example: 11a1b \n")
    add_wordlist = fm.getwordlist3(add_wordfile)
    wordlist = set(words.words('en')) | add_wordlist
    regex = make_regex(pattern)
    output = [w.lower() for w in wordlist if re.search(regex, w)]
    output.sort()
    print(output)
    
def make_regex(pattern):
    
    
    wordlength = len(pattern)
    constraints = list(pattern)
    s = r''
    w = '[a-zA-Z]'

    s = s + r'\b'
    for i in range(wordlength):
        if constraints[i] == '1':
            s = s + w
        else:
            s = s + constraints[i]
    s = s + r'\b'
    
    return s

if __name__ == "__main__":
    wordsearch()
    