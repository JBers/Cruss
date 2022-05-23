# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 16:42:11 2021

@author: Jon
"""

import tkinter as tk
from functools import partial
import boardDesigns as bd
from crossShell import CrussGuiMain

class Board(tk.Frame):
    def __init__(self, parent, bdObject, modeb = False, modec = False):
        tk.Frame.__init__(self, parent)
        
        self.bdObject = bdObject
        self.entry = {}
        self.rows = bdObject.get_vertical()
        self.columns = bdObject.get_horizontal()
        self.modeb = modeb
        self.modec = modec
        self.blocks = bdObject.get_blocks()
        self.sym_dict = self.make_sym_dict()

        # register a command to use for validation
        vcmd = (self.register(self._validate), "%P")

        if modeb:
            for row in range(self.rows):
                for column in range(self.columns):
                    index = (row, column)
                    e = tk.Button(self,width=3)
                    e.config(command= partial(self.set_block,index,e))
                    e.grid(row=row,column=column)
                    self.entry[index] = e
        else:
            for row in range(self.rows):
                for column in range(self.columns):
                    index = (row, column)
                    if index in self.blocks:
                        e = tk.Entry(self, bg='gray5', state = "disabled", justify = "center", width=3, validate="key", validatecommand=vcmd)
                        e.grid(row=row, column=column)
                        self.entry[index] = e
                    else:
                        e = tk.Entry(self, justify = "center", width=3, validate="key", validatecommand=vcmd)
                        e.grid(row=row, column=column)
                        self.entry[index] = e
       
       

    def get(self):
        
        result = {}
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                if index in self.blocks:
                    result[index] = 0
                elif self.entry[index].get() == '':
                    result[index] = 1
                else:
                    result[index] = self.entry[index].get()
               
        return result
    
    def set_solution(self, solution):
        
        for key in solution:
            self.entry[key].insert(0,solution[key])
    
    def set_block(self,index,e):
        
        if self.modec:
            symdex = self.sym_dict[index]
            syme = self.entry[symdex]
            if symdex != index:
                if symdex in self.blocks:
                    syme.config(bg="SystemButtonFace")
                    self.blocks.remove(symdex)
                else:
                    syme.config(bg="gray0")
                    self.blocks.append(symdex)
        
        if index in self.blocks:
            e.config(bg="SystemButtonFace")
            self.blocks.remove(index)
        else:
            e.config(bg="gray0")
            self.blocks.append(index)
        
    def make_sym_dict(self):
        
        X = {}

        x = [(i,j) for i in range(self.rows)
               for j in range(self.columns)]
        l = len(x) -1
        for h in x:
            X[h] = x[l]
            l-=1
            
        return X


    def _validate(self, entry):
        
        if entry.strip() == "":
            return True
        elif entry.isalpha() and (len(entry) == 1):
            return True
        else:
            self.bell()
            return False
        
    
class SizeSelector(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.board_size = tk.IntVar()
        self.size5 = tk.Radiobutton(self, text = "5x5", variable=self.board_size,value=5)
        self.size5.pack(side="top")
        self.size7 = tk.Radiobutton(self, text = "7x7", variable=self.board_size,value=7)
        self.size7.pack(side="top")
        self.size9 = tk.Radiobutton(self, text = "9x9", variable=self.board_size,value=9)
        self.size9.pack(side="top")
        self.size9 = tk.Radiobutton(self, text = "11x11", variable=self.board_size,value=11)
        self.size9.pack(side="top")
        self.size9 = tk.Radiobutton(self, text = "15x15", variable=self.board_size,value=15)
        self.size9.pack(side="top")
        
    def get_size(self):
        return self.board_size
    
class BlockPlacement(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.b = tk.BooleanVar()
        self.c = tk.BooleanVar()
        self.blockplace = tk.Checkbutton(self,text = "Block Placement Mode", variable = self.b)
        self.blockplace.pack()
        self.blockplace1 = tk.Checkbutton(self,text = "With Symmetry",variable= self.c)
        self.blockplace1.pack()
        
        
    def get_state(self):
        return self.b.get(),self.c.get()
    
class CrussGui(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        self.current_board = bd.Design()
        self.prev_board = {}
        
        self.sizeselector = SizeSelector(self)
        
        self.sizeselector.pack()
        self.submit = tk.Button(self, text="Create Board", command=self.on_submit)
        
        self.submit.pack(side="bottom")

    def on_submit(self):
        size = self.sizeselector.get_size()
        if size.get() != 0:
            
            self.current_board.set_horizontal(size.get())
            self.current_board.set_vertical(size.get())
            self.submit.destroy()
            self.sizeselector.destroy()
            self.radioblock = BlockPlacement(self)
            self.radioblock.pack(side = "right")
            
            self.table = Board(self,self.current_board)
            self.table.pack(side="top", fill="both", expand=True)
            
            self.solve = tk.Button(self, text="Solve",command=self.solve_it)
            self.solve.pack(side = "bottom")
            # self.change = tk.Button(self, text="Save", command=self.change_mode)
            # self.change.pack(side = "bottom")
            self.change = tk.Button(self, text="Change Mode", command=self.change_mode)
            self.change.pack(side = "bottom")
            
            
            
                
    def solve_it(self):
        
        result = self.table.get()
        output, self.prev_board = CrussGuiMain(self.current_board, result)
        self.table.set_solution(output)
        

        
    def change_mode(self):
        modeb, modec = self.radioblock.get_state()
        if modeb:
            self.table.destroy()
            self.radioblock.destroy()
            self.change.destroy()
            self.solve.destroy()
            
            self.table = Board(self,self.current_board,modeb,modec)
            self.table.pack(side="top", fill="both", expand=True)
            self.submit = tk.Button(self, text="Back to Board", command=self.change_back)
            self.submit.pack(side="bottom")
            self.design_name = tk.Entry(self)
            self.design_name.insert(0,"Name for Design")
            self.design_name.pack()
            self.saveD = tk.Button(self, text="Save Design",command=self.savedesign)
            self.saveD.pack(side = "bottom")
            
    def change_back(self):
        self.table.destroy()
        self.saveD.destroy()
        self.design_name.destroy()
        
        self.on_submit()
        
    def savedesign(self):
        print(self.design_name.get())
        self.current_board.save_design(self.design_name.get())


root = tk.Tk()
root.option_add("*Font", "28")
root.title("Cruss")
CrussGui(root).pack(side="top", fill="both")
root.mainloop()