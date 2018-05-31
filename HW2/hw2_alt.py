#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

from webcam import Webcam
from PIL import ImageChops
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import time, statistics
import math as mth


class MUCamera:

    def __init__(self, print_avg=0):
        self.MU = Webcam()
        self.img_intensity = []
        self.img_time = []
        self.MU.start()
        self.filtered_average = []
        self.MU.register_callback(self.average_intensity, 1)
        self.img = []
        self.euclidean_dist = None
        self.print_avg = print_avg

    def average_intensity(self, image):
        self.img_intensity.append(np.mean(np.mean(image)))
        self.img_time.append(time.time())
        self.img.append(image)
        if self.print_avg == 1:
            print(np.mean(np.mean(image)))
        return np.mean(np.mean(image))

    def filtered_average_intensity(self):
        b, a = signal.butter(5, 0.025)
        zi = signal.lfilter_zi(b, a)
        z, _ = signal.lfilter(b, a, self.img_intensity, zi=zi * self.img_intensity[0])
        z2, _ = signal.lfilter(b, a, z, zi=zi * z[0])
        self.filtered_average = signal.filtfilt(b, a, self.img_intensity)

    def intensity_plot(self):
        t0 = self.img_time[0]
        t = [(x - t0)/60 for x in self.img_time]
        y = self.img_intensity
        y_filtered = self.filtered_average

        plt.plot(t, y, 'k', t, y_filtered, 'r--')
        plt.xlabel('Minutes')
        plt.ylabel('Average Intensity')
        plt.legend(('Average Image Intensity', 'Smoothed Average Image Intensity'), loc='best')
        plt.title('Average Image Intensity from 5:45 PM to 8:30 AM PST, May 29th')
        plt.grid()
        plt.show()

    def daytime(self, threshold=75):
        time.sleep(2)
        img = self.img[-1]
        intensity = np.mean(np.mean(img))
        if intensity < threshold:
            return False
        else:
            return True

    def common_color(self):
        img = self.img[-1].getdata()
        m = statistics.mode(img)
        return m

    def stop(self):
        self.MU.stop()
        self.filtered_average_intensity()
        self.intensity_plot()

    def motion(self):
        while len(self.img) < 25:
            pass

        img1 = self.img[-25]
        img2 = self.img[-1]
        img3 = ImageChops.subtract(img1, img2)
        self.euclidean_dist = mth.sqrt(np.sum(np.array(img3.getdata()) ** 2))

        if self.euclidean_dist > 8000:
            return True
        else:
            return False

    def highlight_motion(self):
        while len(self.img) < 25:
            pass
        img1 = self.img[-25]
        img2 = self.img[-1]

        img3 = ImageChops.subtract(img1, img2)
        img2_data = np.asarray(img2)
        img3_data = np.asarray(img3)
        img2_data.setflags(write=1)
        for i in range(len(img3_data[1, :])):
            for j in range(len(img3_data[:, i])):
                avg = np.mean(img3_data[j, i])
                if avg > 35 and j > 250:
                    img2_data[j, i] = [255, 0, 0]

        img_new = Image.fromarray(img2_data, 'RGB')
        img_new.show()



if __name__ == '__main__':
    test = MUCamera(print_avg=0)
    # print(test.average_intensity())
    # print(test.daytime())
    # print(test.motion())
    # print(test.common_color())
    test.highlight_motion()
    # start = time.time()
    # time.sleep(60)
    # test.stop()
