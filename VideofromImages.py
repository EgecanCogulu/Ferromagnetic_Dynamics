# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:45:25 2020

@author: Egecan
"""


import cv2
import os
import numpy as np

folder=r"gif2\\"
image_folder = r'C:\Users\Egecan\Desktop\PEEM IMAGE ANALYSIS\Second Day\Final Versions\Separate Polarizations\Python\\'+folder
video_name = image_folder+'video.mp4'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images = list(np.sort(images*10))*5

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 30, (int(width),int(height)))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()