# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:20:57 2020

@author: Jon
"""

import re
import random



def make_regex(clue):
    
    #clue is list of form ['word','wordlength',vert or horiz,list of locations]
    #returns regex
    
    wordlength = clue[1]
    constraints = list(clue[0])
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

def find_mcv(keys):
    current = 0
    isdone = 0
    done = False
    mcv_key = 0
    for key in keys:
        letters = re.findall(r'[a-zA-Z]', keys[key][0])
        
        cvs = len(letters) / keys[key][1]
        
        if cvs == 1:
            isdone+=1
            
        elif cvs > current:
            current = cvs
            mcv_key = key
            
        # elif cvs == current:
        #     if random.random() > .5:
        #         current = cvs
        #         mcv_key = key
                
    if isdone == (len(keys)):
        done = True            
    return mcv_key, done        

def find_mcv2(keys, wordlist, memo):
    
    isdone = 0
    done = False
    current = 1000000
    current_key = 0
    current_words = []
    
    for key in keys:
        letters = list(keys[key][0])
        length = 0
        for letter in letters:
            if letter != '1':
                length +=1
        cvs = length / keys[key][1]
        
        if cvs == 1:
            isdone+=1
            
        else:
            # regex = make_regex(keys[key])
            # words = find_words(regex, wordlist)
            words = find_words2(wordlist, keys[key], memo)
            if len(words) < current:
                current = len(words)
                current_key = key
                current_words = words
                
    if isdone == (len(keys)):
        done = True

    return current_key, current_words, done            

def find_words(regex, wordlist, memo):
    
    try:
        return memo[regex]
    except:
        if type(wordlist) is set or type(wordlist) is list:
            words =  [w for w in wordlist if re.search(regex, w)]
            memo[regex] = words
        else:
            words = re.findall(regex, wordlist)
            memo[regex] = words
        
        
    return words

def find_words2(wordlist, key, memo={}):
    
    words = []
    memo_tuple = (key[0],key[2],key[3][0])
    
    try:
        return memo[key[0]]
    except:
        for word in wordlist:
            if subtractStr(word, key[0]):
                words.append(word)
        memo[key[0]] = words
    return words   

def is_words(keys, wordlist, unitarys):
    
    no_dupes_list = []
    
    for key in keys:
        
        check = True
        
        word = keys[key][0]
        # print(word)
        letters = list(word)
        
        for letter in letters:
            if letter == '1':
                check = False
                break
        if check:
            # reword = r'' + r'\b' + word + r'\b'
            # if len(find_words(reword, wordlist)) == 0:
            if len(unitarys) == 0:
                if word not in wordlist or word in no_dupes_list:
                    return False
            elif word not in wordlist and word not in unitarys or word in no_dupes_list:
                return False
        no_dupes_list.append(word)
    return True



def subtractStr(x,y):
    if len(x) == len(y):
        for i in range(len(y)):
            if y[i] == '1' or y[i] == x[i]:
                continue
            else:
                return False
        return True
    
def get_word(method = 'random',*args):
    
    if method == 'random':
        def get_rand_word(words):
            random.shuffle(words)
            return words.pop()
        return get_rand_word
    
    if method == "union":
        def get_union_word(words,*args2):           
            
            words.sort(key=lambda word:word in args[0])
            if words[-1] in args2[0]:
                try:
                    return words.pop(-2)
                except:
                    return words.pop()
            return words.pop()
        return get_union_word
    
