#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

import webcam, time
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# class MUCamera:


def image_intensity():
    mu_live = webcam.Webcam().grab_image()
    intensity = mu_live.getdata()
    pxlavg = []
    for i in list(intensity):
        pxlavg.append(np.mean(i))

    return np.mean(pxlavg)

def moving_average():

    avg = []
    lst_time = []
    while time.time() < 1527612840:
            now = time.time()
            mu_live = webcam.Webcam().grab_image()
            intensity = mu_live.getdata()
            pxlavg = []

            for i in list(intensity):
                pxlavg.append(np.mean(i))

            lst_time.append(now)
            avg.append(np.mean(pxlavg))
            time.sleep(1)

    t0 = lst_time[0]
    lst_time[:] = [x - t0 for x in lst_time]

    plt.plot(lst_time, avg)
    plt.xlabel('Time (s)')
    plt.ylabel('Average Intensity')
    plt.show()





def daytime(threshold=80):
    intensity = image_intensity()

    if intensity < threshold:
        return False
    else:
        return True

def common_color():
    image = webcam.Webcam().grab_image()
    pixels = mu_live.getcolors()

    most_frequent_pixel = pixels[0]

    # for count, colour in pixels:
    #     if count > most_frequent_pixel[0]:
    #         most_frequent_pixel = (count, colour)

    return most_frequent_pixel



if __name__ == '__main__':
    # print(image_intensity())
    moving_average()
    # print(daytime())
    # print(common_color())




