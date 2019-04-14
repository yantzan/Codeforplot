# -*- coding: utf-8 -*-
"""
Created on Fri May 11 13:53:58 2018

@author: 12
"""

from PIL import Image
import matplotlib.pyplot as plt
img = Image.open("9-1.tif") 
height = img.size[0]
width = img.size[1]
for i in range(0, 700):
      for j in range(0, 525):
                
        r,g,b = img.getpixel((i,j))
        if(0<=b<=210 and 0<=g<=210 and 0<=r<=210): #对黑色进灰色行判断
            b=255
            g=255
            r=255
         
        img.putpixel((i,j), (r,g,b)) 
img.save('9-1-1.tif')        
plt.show()