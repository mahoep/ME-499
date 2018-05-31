#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

from PIL import Image
from PIL import ImageChops
import math as mth
import numpy as np
from webcam import Webcam
import time

img1 = Image.open('E:/Users/Matt/Documents/Programming Projects/ME-499/HW2/images/MU_1527554390.4918337.jpg')
img2 = Image.open('E:/Users/Matt/Documents/Programming Projects/ME-499/HW2/images/MU_1527554448.4631853.jpg')

img3 = ImageChops.subtract(img1, img2)
img2_data = np.asarray(img2)
img3_data = np.asarray(img3)
img2_data.setflags(write=1)
for i in range(len(img3_data[1,:])):
    for j in range(len(img3_data[:,i])):
        avg = np.mean(img3_data[j,i])
        if avg > 55 and j > 250:
            img2_data[j,i] = [255, 0, 0]

img_new = Image.fromarray(img2_data, 'RGB')
img_new.show()

