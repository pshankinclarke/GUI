#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 12:42:28 2018

@author: Max
"""
from PIL import Image, ImageDraw
import random
import numpy as np




img = Image.new('RGB', (1000, 1000), color = (random.randint(0,256), random.randint(0,256), random.randint(0,256)))
count =0 
d = ImageDraw.Draw(img)
d.text((10,10),"", fill=(255,255,0))
countx=0
county=0
pixy = img.load()
d = np.array([])
lab = np.array([])
test = np.array([1,2,3,4,5,6])

def get_area(height,width) :
    area = height* width 
    return area


for count in range(10):
    xS = random.randint(0,50)
    xE = random.randint(0,50)
    yS = random.randint(0,50)
    yE = random.randint(0,50)
    gray = random.randint(100,255)
    while(xE<=xS):
        if (countx>50):
            xE = random.randint(0,50)
            countx=0
        xS = random.randint(0,50)
        countx+=1
    while(yE<=yS):
        if (county>50):
            yE = random.randint(0,50)
            county=0
        county+=1    
        yS = random.randint(0,50)
        
    
    for x in range(xS,xE):
        for y in range (yS,yE):
            pixy[x,y]= (gray,gray,gray)
            a = np.array(pixy[x,y])
            b = np.asarray(pixy[x,y])
            d = np.append(d, a)
e = np.delete(d, slice(None,None,3))
#e = np.delete(d,np.arange(0,d.size,3))
#img.show()          

np.set_printoptions(threshold=np.nan)    
#print(e)
k = len(e)/2
e = np.arange(len(e)).reshape(int(k),2)
f= []
for i in range (len(e)):
    f.append(1)

print(e)     
#print(count) 

for i in range(1000):
    for j in range (1000):
        print(pixy[i,j])





