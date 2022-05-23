# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:40:35 2020

@author: Jon
"""

import json

class Design(object):
    
    def __init__(self, vertical = None, horizontal = None, blocks = []):
        
        self.vertical = vertical
        self.horizontal = horizontal
        self.blocks = blocks
        
    def set_vertical(self, vert):
        
        self.vertical = vert

    def get_vertical(self):
        
        return self.vertical
    
    def set_horizontal(self,horiz):
        
        self.horizontal = horiz
    
    def get_horizontal(self):
        
        return self.horizontal
    
    def set_blocks(self, blocks):
        
        for block in blocks:
            if block not in self.blocks:
                self.blocks.append(block)
                
    def reset_blocks(self):
        
        self.blocks = []
        
    def remove_block(self,rmblocks):
        
        temp = []
        
        for block in self.blocks:
            if block not in rmblocks:
                temp.append(block)
                
        self.blocks = temp
    
    def get_blocks(self):
        
        return self.blocks
    
    def save_design(self, designname, design_file = "designBs.json"):
        
        designs = {}
        
        designs[designname] = [self.vertical,self.horizontal,self.blocks]
        try:
            with open(design_file) as f:
                
                temp = json.load(f)
                
            designs.update(temp)
        finally:
            with open(design_file, 'w') as f:
                json.dump(designs,f)
            
    @classmethod
    def load_design(cls, designname, design_file = "designBs.json"):
        
        with open(design_file,'r') as f:
            designs = json.load(f)
            
        design = designs[designname]
        
        return cls(design[0],design[1],[(i[0],i[1]) for i in design[2]])
    
    @staticmethod
    def list_designs(design_file = "designBs.json"):
        
        with open(design_file, 'r') as f:
            designs = json.load(f)
            
        return list(designs)
            
    
    
    