#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

from webcam import Webcam
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import time


class MUCamera:

    def __init__(self):
        self.MU = Webcam()
        self.img_intensity = []
        self.img_time = []
        self.MU.start()
        self.start = time.time()
        self.filtered_average = []
        self.MU.register_callback(self.average_intensity, 1)

    def average_intensity(self, image):
        self.img_intensity.append(np.mean(np.mean(image)))
        self.img_time.append(time.time())

    def filtered_average_intensity(self):
        b, a = signal.butter(5, 0.025)
        zi = signal.lfilter_zi(b, a)
        z, _ = signal.lfilter(b, a, self.img_intensity, zi=zi * self.img_intensity[0])
        z2, _ = signal.lfilter(b, a, z, zi=zi * z[0])
        self.filtered_average = signal.filtfilt(b, a, self.img_intensity)

    def intensity_plot(self):
        t = self.img_time
        y = self.img_intensity
        y_filtered = self.filtered_average

        plt.plot(t, y, 'k', t, y_filtered, 'r--')
        plt.xlabel('Minutes (min)')
        plt.ylabel('Average Intensity')
        plt.legend(('Noisy Signal', 'Filtered Signal'), loc='best')
        plt.show()

    def stop(self):
        self.MU.stop()
        self.filtered_average_intensity()
        self.intensity_plot()



if __name__ == '__main__':
    test = MUCamera()
    start = time.time()
    time.sleep(60)
    test.stop()





