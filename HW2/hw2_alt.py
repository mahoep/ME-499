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

    def __init__(self, motion=0):
        if motion == 0:
            self.MU = Webcam()
            self.img_intensity = []
            self.img_time = []
            self.MU.start()
            self.filtered_average = []
            self.MU.register_callback(self.average_intensity, 1)
            self.img = []
            self.euclidean_dist = None

    def average_intensity(self, image):
        self.img_intensity.append(np.mean(np.mean(image)))
        self.img_time.append(time.time())
        self.img.append(image)

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
        plt.xlabel('Minutes (min)')
        plt.ylabel('Average Intensity')
        plt.legend(('Noisy Signal', 'Filtered Signal'), loc='best')
        plt.show()

    def daytime(self, threshold=75):
        img = self.MU.grab_image()
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
        # self.filtered_average_intensity()
        # self.intensity_plot()
        # self.daytime()

    def motion(self):
        while len(self.img) < 2:
            pass

        img3 = ImageChops.subtract(self.img[-2], self.img[-1])
        self.euclidean_dist = mth.sqrt(np.sum(np.array(img3.getdata()) ** 2))

        if self.euclidean_dist > 8000:
            return True
        else:
            return False

    def highlight_motion(self):
        while len(self.img) < 2:
            pass

        img3 = ImageChops.subtract(self.img[0], self.img[1])
        pxldata = np.asarray(img3)
        copy = np.asarray(img3)
        copy.setflags(write=1)
        for i in range(len(pxldata[1, :])):
            for j in range(len(pxldata[:, i])):
                avg = np.mean(pxldata[j, i])
                if avg > 55:
                    copy[j, i] = [255, 0, 0]

        img_new = Image.fromarray(copy, 'RGB')
        img_new.show()




if __name__ == '__main__':
    test = MUCamera()
    print(test.motion())
    print(test.common_color())
    test.highlight_motion()
    # start = time.time()
    # time.sleep(60)
    # test.stop()





