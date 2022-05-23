# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 11:36:31 2021

@author: Jon
"""


class crussParse(object):
    
    def __init__(self,solvedboard):
        
        self.solvedboard = solvedboard
        self.vert,self.horiz = solvedboard.get_dims()
        self.to_parse = solvedboard.tk_gui_getter()
        self.keys = solvedboard.get_keys()
        
    def parse_for_latex(self):
        
        parsed_board = ""
        num=1
        starts=[]
        
        for key in self.keys:
            starts.append(self.keys[key][3][0])
        
        for key in self.to_parse:
            if self.to_parse[key] == "0":
                parsed_board += "|*"
            elif key in starts:
                parsed_board += f"|[{num}]{self.to_parse[key].upper()}"
                num+=1
            else:
                parsed_board += f"|{self.to_parse[key].upper()}"
            if key[1] == (self.vert - 1):
                parsed_board += "|."
                
        return parsed_board
    
    def save_as_pdf(self):
        
        replaceKV = {}
        
        with open('crussTemplate.tex') as f:
             template = f.read()
            
             replaceKV['$vert$'] = f'{self.vert}'
             replaceKV['$horiz$'] = f'{self.horiz}'
             replaceKV['$solvedboard$'] = self.parse_for_latex()
             
             for k,v in replaceKV.items():
                 
                 template = template.replace(k,v)
                 
                 
        with open('RenameThisCruss.tex','w') as output:
             output.write(template)
                
                