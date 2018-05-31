#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

import webcam, time
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal


class MUCamera:

    def __init__(self):
        self.image = webcam.Webcam().grab_image()
        self.imdata = self.image.getdata()

    def image_intensity(self):
        pxlavg = []
        for i in list(self.imdata):
            pxlavg.append(np.mean(i))

        return np.mean(pxlavg)

    def moving_average(self):
        avg = []
        lst_time = []
        inital_time = time.time()
        while time.time() < inital_time+120: # May 29th, @ 8:30 am PST
                now = time.time()
                pxlavg = []

                for i in list(self.imdata):
                    pxlavg.append(np.mean(i))

                lst_time.append(now)
                avg.append(np.mean(pxlavg))
                time.sleep(1)

        t0 = lst_time[0]
        lst_time[:] = [x - t0 for x in lst_time]

        return lst_time, avg

    def filtered_average_intensity(self):
        # from https://docs.scipy.org/doc/scipy-1.0.0/reference/generated/scipy.signal.lfilter.html#scipy.signal.lfilter
        _, avg = self.moving_average()
        b, a = signal.butter(5, 0.025)
        zi = signal.lfilter_zi(b, a)
        z, _ = signal.lfilter(b, a, avg, zi=zi * avg[0])
        z2, _ = signal.lfilter(b, a, z, zi=zi * z[0])
        y = signal.filtfilt(b, a, avg)
        return y

    def intensity_plot(self):
        lst_time, avg = self.moving_average()
        y = self.filtered_average_intensity()

        plt.plot(lst_time, avg, 'k', lst_time, y, 'r--')
        plt.xlabel('Minutes (min)')
        plt.ylabel('Average Intensity')
        plt.legend(('Noisy Signal', 'Filtered Signal'), loc='best')
        plt.show()

    def daytime(self, threshold=80):
        intensity = self.image_intensity()

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
    test = MUCamera()
    print(test.image_intensity())
