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
# img3.show()

pxldata = np.asarray(img3)
copy = np.asarray(img3)
copy.setflags(write=1)
for i in range(len(pxldata[1,:])):
    for j in range(len(pxldata[:,i])):
        avg = np.mean(pxldata[j,i])
        if avg > 55:
            copy[j,i] = [255, 0, 0]


img_new = Image.fromarray(copy, 'RGB')
img_new.show()

