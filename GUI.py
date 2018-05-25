#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 19:24:22 2018

@author: parkershankin-clarke
"""

import tkinter as tk

from PIL import ImageTk, Image

class GUI : 
    
#    def __init__(self,path):
#        self.path = path
#    
#    def createAndShowGUI(self,path) :
#        
#        #This creates the main window of an application
#        window = tk.Toplevel()
#        window.title("Join")
#        window.geometry("300x300")
#        window.configure(background='grey')
#
#        
#        #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
#        img = ImageTk.PhotoImage(Image.open(path))
#        
#        #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
#        panel = tk.Label(window, image = img)
#        
#        #The Pack geometry manager packs widgets in rows or columns.
#        panel.pack(side = "bottom", fill = "both", expand = "yes")
#        
#        #Start the GUI
#        window.mainloop()
#        
#        place = GUI('test.png')
#        

        path = 'test.png'
        
        #This creates the main window of an application
        window = tk.Toplevel()
        window.title("Join")
        window.geometry("300x300")
        window.configure(background='grey')

        
        #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img = ImageTk.PhotoImage(Image.open(path))
        
        #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        panel = tk.Label(window, image = img)
        
        #The Pack geometry manager packs widgets in rows or columns.
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        
        #Start the GUI
        window.mainloop()
        