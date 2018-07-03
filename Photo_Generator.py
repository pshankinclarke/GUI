#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 00:17:59 2018

@author: parkershankin-clarke
"""
from PIL import Image, ImageDraw
import random
import numpy as np




img = Image.new('RGB', (600, 600), color = (random.randint(0,256), random.randint(0,256), random.randint(0,256)))
count =0 
d = ImageDraw.Draw(img)
d.text((10,10),"", fill=(255,255,0))

pixy = img.load()

def get_area(height,width) :
    area = height* width 
    return area



for count in range(2):
    xS = random.randint(0,600)
    xE = random.randint(0,600)
    yS = random.randint(0,600)
    yE = random.randint(0,600)
    while(xE<=xS):
        xS = random.randint(0,600)
        
    while(yE<=yS):
        yS = random.randint(0,600)
        
    
    for x in range(xS,xE):
        for y in range (yS,yE):
            pixy[x,y]= (224,224,224)
            
for count in range(2):
    xS = random.randint(0,600)
    xE = random.randint(0,600)
    yS = random.randint(0,600)
    yE = random.randint(0,600)
    while(xE<=xS):
        xS = random.randint(0,600)
        
    while(yE<=yS):
        yS = random.randint(0,600)
        
    
    for x in range(xS,xE):
        for y in range (yS,yE):
            pixy[x,y]= (128,128,128)

for count in range(2):
    xS = random.randint(0,600)
    xE = random.randint(0,600)
    yS = random.randint(0,600)
    yE = random.randint(0,600)
    while(xE<=xS):
        xS = random.randint(0,600)
        
    while(yE<=yS):
        yS = random.randint(0,600)
        
    
    for x in range(xS,xE):
        for y in range (yS,yE):
            pixy[x,y]= (64,64,64)
            
for count in range(2):
    xS = random.randint(0,600)
    xE = random.randint(0,600)
    yS = random.randint(0,600)
    yE = random.randint(0,600)
    while(xE<=xS):
        xS = random.randint(0,600)
        
    while(yE<=yS):
        yS = random.randint(0,600)
        
    
    for x in range(xS,xE):
        for y in range (yS,yE):
            pixy[x,y]= (20,20,20)

img.show()