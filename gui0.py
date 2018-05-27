#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:07:49 2018

@author: Max
"""

from tkinter import *
from tkinter import ttk
root = Tk()

h = ttk.Scrollbar(root, orient=HORIZONTAL)
v = ttk.Scrollbar(root, orient=VERTICAL)
canvas = Canvas(root, scrollregion=(0, 0, 1000, 1000), yscrollcommand=v.set, xscrollcommand=h.set)
h['command'] = canvas.xview
v['command'] = canvas.yview
ttk.Sizegrip(root).grid(column=1, row=1, sticky=(S,E))

canvas.grid(column=0, row=0, sticky=(N,W,E,S))
h.grid(column=0, row=1, sticky=(W,E))
v.grid(column=1, row=0, sticky=(N,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

lastx, lasty = 0, 0
startx, starty = 0, 0 
endx, endy = 0, 0

def xy(event):
    global lastx, lasty
    global startx, starty
    lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)
    startx, starty = canvas.canvasx(event.x), canvas.canvasy(event.y)
    
def setColor(newcolor):
    global color
    color = newcolor
    canvas.dtag('all', 'paletteSelected')
    canvas.itemconfigure('palette', outline='white')
    canvas.addtag('paletteSelected', 'withtag', 'palette%s' % color)
    canvas.itemconfigure('paletteSelected', outline='#999999')

def addRect(event):
    global lastx, lasty
    global endx, endy
    global startx, starty
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    canvas.create_rectangle((lastx, lasty, x, y), outline=color, width=5, tags='currentRect')
    lastx, lasty = x, y
    endx, endy = x, y
    print(startx)
    print(starty)
    print(endx)
    print(endy)
    x1 = int(startx)
    x2 = int(endx)
    y1 = int(starty)
    y2 = int(endy)
    pixelList=[]
    for i in range(x1, (x2+1)):
        for j in range (y1, y2+1):
            pixelList.append([i, j])
           
    print(pixelList)
    print(startx)
    print(starty)
    print(endx)
    print(endy)
def getPixels(event):
    global endx, endy
    global startx, starty
    x1 = int(startx)
    x2 = int(endx)
    y1 = int(starty)
    y2 = int(endy)
    pixelList=[]
    count=0
    for i in range(x1, x2):
        for j in range (y1, y2):
            pixelList[count].append(i, j)
            count+=1
    print(pixelList)

def doneStroke(event):
    canvas.itemconfigure('currentRect', width=1)        
        
canvas.bind("<Button-1>", xy)
#canvas.bind("<B1-Motion>", addRect)
#canvas.bind("<B1-ButtonRelease>", getPixels)
canvas.bind("<B1-ButtonRelease>", addRect)

id = canvas.create_rectangle((10, 10, 30, 30), fill="red", tags=('palette', 'palettered'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
id = canvas.create_rectangle((10, 35, 30, 55), fill="blue", tags=('palette', 'paletteblue'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
id = canvas.create_rectangle((10, 60, 30, 80), fill="black", tags=('palette', 'paletteblack', 'paletteSelected'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))

setColor('black')
canvas.itemconfigure('palette', width=5)
gif1 = PhotoImage(file='starfield.gif')
canvas.create_image(50, 10, image=gif1, anchor=NW)
root.mainloop()