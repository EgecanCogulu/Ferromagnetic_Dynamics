# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 00:24:04 2020

@author: Egecan
"""


from PIL import Image, ImageDraw
import os

foldername=r"C:\Users\Egecan\Desktop\GIF\\"
filenames=os.listdir(foldername)
images=[]

for (i,filename) in enumerate(filenames):
    img = Image.open(foldername+filename)
    images.append(img)




# images = []

# width = 200
# center = width // 2
# color_1 = (0, 0, 0)
# color_2 = (255, 255, 255)
# max_radius = int(center * 1.5)
# step = 8

# for i in range(0, max_radius, step):
#     im = Image.new('RGB', (width, width), color_1)
#     draw = ImageDraw.Draw(im)
#     draw.ellipse((center - i, center - i, center + i, center + i), fill=color_2)
#     images.append(im)

# for i in range(0, max_radius, step):
#     im = Image.new('RGB', (width, width), color_2)
#     draw = ImageDraw.Draw(im)
#     draw.ellipse((center - i, center - i, center + i, center + i), fill=color_1)
#     images.append(im)

images[0].save(foldername+str(i)+" IMAGES GIF.gif",
                save_all=True, append_images=images[1:], optimize=True, duration=0, loop=0)