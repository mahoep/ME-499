#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

import webcam
from PIL import Image
import numpy as np
import time


class MUCamera:

    def image_intensity():
        mu_live = webcam.Webcam().grab_image()
        intensity = mu_live.getdata()
        pxlavg = []
        for i in list(intensity):
            pxlavg.append(np.mean(i))

        return np.mean(pxlavg)

    def moving_average():
        while time.time() < 1527607800:
            now = time.time()
            dir = 'E:/Users/Matt/Documents/Programming Projects/ME-499/HW2/images/'
            filename = 'MU_{}.jpg'.format(now)

            mu_live = webcam.Webcam().grab_image()
            mu_live.save(dir+filename, 'JPEG')

            print("image grabbed at {}".format(now))
            intensity = mu_live.getdata()
            pxlavg = []
            running_avg = []
            lst_time = []

            for i in list(intensity):
                pxlavg.append(np.mean(i))
            time.sleep(1)
            running_avg.append(np.mean(pxlavg))
            lst_time.append(now)
        return running_avg, lst_time

if __name__ == '__main__':
    # print(image_intensity())
    moving_average()





