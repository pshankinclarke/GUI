#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 17:39:01 2018

@author: parkershankin-clarke
"""
from PIL import Image, ImageDraw
import random

img = Image.new('RGB', (600, 600), color = (random.randint(0,256), random.randint(0,256), random.randint(0,256)))
count =0 
d = ImageDraw.Draw(img)
d.text((10,10),"", fill=(255,255,0))

pixy = img.load()

def get_area(height,width) :
    area = height* width 
    return area



for count in range(10):
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
            pixy[x,y]= (160,160,160)


#
#for imgnum in range (1,1) : 
#    d = imgnum + 1 
#    img = Image.new('RGB', (600, 600), color = (73, 109, 137))
#    print(imgnum)
#    draw = ImageDraw.Draw(img)   
#
#    
#    width,height= img.size
#    pix = img.load()
#    pix [0,0]= (255,255,255)
# =============================================================================
#     for count in range(10):
#         i = random.randomint(0,400)
#         j =random.randomint(0,400)
#         for x in range(i):
#             for y in range (j):
#                 pix[x,y]= (160,160,160)
#                 
# =============================================================================
#img.show()
#img.save('pil_text' + str(imgnum) + '.png')
        
# =============================================================================
#     del draw
#     del img
#     
# =============================================================================
#img.show()