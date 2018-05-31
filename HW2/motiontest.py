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
import statistics

# img1 = Image.open('E:/Users/Matt/Documents/Programming Projects/ME-499/HW2/images/MU_1527554390.4918337.jpg')
# img2 = Image.open('E:/Users/Matt/Documents/Programming Projects/ME-499/HW2/images/MU_1527554448.4631853.jpg')
#
# img3 = ImageChops.subtract(img1, img2)
# img2_data = np.asarray(img2)
# img3_data = np.asarray(img3)
# img2_data.setflags(write=1)
# for i in range(len(img3_data[1,:])):
#     for j in range(len(img3_data[:,i])):
#         avg = np.mean(img3_data[j,i])
#         if avg > 55 and j > 250:
#             img2_data[j, i] = [255, 0, 0]
#
# img_new = Image.fromarray(img2_data, 'RGB')
# img_new.show()
pxl_coor = (250, 365, 500, 470)
img = Image.open('E:/Users/Matt/Documents/Programming Projects/ME-499/HW2/plain_quad_ppl.jpg').crop(pxl_coor)


# img = img1.getdata()
# m = statistics.mode(img)
# print(m)
# baseline = np.asarray(img1)
# baseline.setflags(write=1)
# for i in range(len(baseline[1, :])):
#         for j in range(len(baseline[:, i])):
#             baseline[j,i] = [170, 170, 168]
# img_new = Image.fromarray(baseline, 'RGB')
#
#
pxl_coor = (250, 365, 500, 470)
baseline = np.asarray(img)
baseline.setflags(write=1)

for i in range(len(baseline[1, :])):
    for j in range(len(baseline[:, i])):
        baseline[j, i] = [170, 170, 168]
img_grey = Image.fromarray(baseline, 'RGB')
img_compare = ImageChops.subtract(img, img_grey)
img_grey.show()
img.show()

euclidean_dist = mth.sqrt(np.sum(np.array(img_compare.getdata()) ** 2))
print(euclidean_dist)
if euclidean_dist > 8000:
    print('true')
else:
    print('false')
