#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 21:20:14 2018

@author: parkershankin-clarke
"""
from tkinter import *
trace = 0 
import tkinter as tk
from PIL import ImageTk, Image



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


class CanvasEventsDemo: 
   

   
    def __init__(self, parent=None):
        canvas = Canvas(width=300, height=300, bg='beige') 
        canvas.pack()
        canvas.bind('<ButtonPress-1>', self.onStart) 
        canvas.bind('<B1-Motion>',     self.onGrow)  
        canvas.bind('<Double-1>',      self.onClear) 
        canvas.bind('<ButtonPress-3>', self.onMove)  
        self.canvas = canvas
        self.drawn  = None
        self.kinds = [canvas.create_oval, canvas.create_rectangle]
    def onStart(self, event):
        self.shape = self.kinds[0]
        self.kinds = self.kinds[1:] + self.kinds[:1] 
        self.start = event
        self.drawn = None
    def onGrow(self, event):                         
        canvas = event.widget
        if self.drawn: canvas.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x, event.y)
        if trace: print(objectId)
        self.drawn = objectId
    def onClear(self, event):
        event.widget.delete('all')                   
    def onMove(self, event):
        if self.drawn:                               
            if trace: print(self.drawn)
            canvas = event.widget
            diffX, diffY = (event.x - self.start.x), (event.y - self.start.y)
            canvas.move(self.drawn, diffX, diffY)
            self.start = event

if __name__ == '__main__':
    CanvasEventsDemo()
    mainloop()
