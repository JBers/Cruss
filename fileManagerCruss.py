# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:58:42 2020

@author: Jon
"""



def getwordlist(wordlist_file):
    
    with open(wordlist_file, 'r') as f:
        wordlist = f.read().lower()
        
    return wordlist

def getwordlist2(wordlist_file):
    
    wordlist=[]
    with open(wordlist_file, 'r') as f:
        for line in f:
            wordlist.append(line.rstrip('\n'))
        
    return set(wordlist)

def getwordlist3(wordlist_file):
    
    with open(wordlist_file, 'r',errors='ignore') as f:
        text = f.read()
        newlist = text.split()
        add_wordlist = set(filter(lambda s: len(s)>0,map(clean,newlist)))
    return add_wordlist  

def add_banned(banned_file, banned_words):
    
    with open(banned_file, 'a') as f:
        for word in banned_words:
            word = word + '\n'
            f.write(word)
    return

def update_wordlist(wordlist1, wordlist2, arg):
    #wordlist1 should be the main wordlist to be modified
    #wordlist2 should be the modifying wordlist 
    #arg = True for add
    #arg = False for subtract
    
    if arg:
        with open(wordlist1, 'r') as f1:
            f1_list = f1.readlines()
        with open(wordlist1, 'a') as f1:           
            with open(wordlist2, 'r') as f2:
                f1.write('\n')
                for line in f2:
                    if line not in f1_list:                        
                        f1.write(line.lower())
    
    else:
        
        with open('renameWordlist.txt', 'w') as f1:
            with open(wordlist1, 'r') as f2:
                mainwords = f2.readlines()
            with open(wordlist2, 'r') as f3:
                badwords = f3.readlines()
            for word in mainwords:
                if word not in badwords:
                    f1.write(word.lower())
                    
                    
def clean(xx):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    newword=""
    for letter in xx.lower():
        if letter in alphabet:
            newword+=letter
    return newword

# update_wordlist('renameWordlist.txt', 'wordlists/Misc_Wordlists/geographic.txt', True)

# y =getwordlist3('wordlists/computerywords.txt')
# print(y)



# regex = r'\b[a-z][a-z][a-z]o\b'
# words =  [w for w in y if re.search(regex, w)]
# print(words)