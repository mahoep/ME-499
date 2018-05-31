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

    def __init__(self):
        self.MU = Webcam()
        self.img_intensity = []
        self.img_time = []
        self.MU.start()
        self.filtered_average = []
        self.MU.register_callback(self._average_intensity, 1)
        self.img = []
        self.euclidean_dist = None

    def _average_intensity(self, image):
        '''
        A function that does the actual calculations
        :param image: the image is retrieved from the webcam.py file using the callback function
        :return: the average intensity of the captured images in a list, the time of capture, the image objects
            in a list
        '''
        self.img_intensity.append(np.mean(np.mean(image)))
        self.img_time.append(time.time())
        self.img.append(image)
        return np.mean(np.mean(image))

    def average_intensity(self):
        '''
        The function that should actually be called if you want to know the average intensity
        :return: The average intensity of the image that was most recently retreived from the webcam
        '''
        while len(self.img_intensity) < 1:
            pass
        return self.img_intensity[-1]

    def filtered_average_intensity(self):
        '''
        Function that takes in the average intensity list from _average_intensity() and passes the data through
        a butterworth filter.
        https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.signal.butter.html
        :return: A list of the filtered average intensities
        '''
        b, a = signal.butter(5, 0.025)
        zi = signal.lfilter_zi(b, a)
        z, _ = signal.lfilter(b, a, self.img_intensity, zi=zi * self.img_intensity[0])
        z2, _ = signal.lfilter(b, a, z, zi=zi * z[0])
        self.filtered_average = signal.filtfilt(b, a, self.img_intensity)

    def intensity_plot(self):
        '''
        Creates a plot of the raw average intensites and the filtered intensites
        Raw is a solid black line, filtered is a dashed red line
        :return: A plot
        '''
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
        '''
        Determines whether it is night or day from retreived webcam image
        :param threshold: the average intesntity value that is used to determine time of day
        if calculated average intensity is less than the threshold, it is night, otherwise it is day
        :return: True if daytime, false if nighttime
        '''
        while len(self.img_intensity) < 1:
            pass
        img = self.img[-1]
        intensity = np.mean(np.mean(img))
        if intensity < threshold:
            return False
        else:
            return True

    def common_color(self):
        '''
        Calculates the most common color in the retrieved webcam image
        Uses statistics library
        :return: color that occurs the most in a tuple (R,G,B)
        '''
        img = self.img[-1].getdata()
        m = statistics.mode(img)
        return m

    def stop(self):
        '''
        Function that terminates the callback function that is started in __init__
        Will call the filtering function and plotting function
        :return:
        '''
        self.MU.stop()
        self.filtered_average_intensity()
        self.intensity_plot()

    def motion(self):
        '''
        Determines whether or not motion took place between two images
        Waits until 25 images have been retreived to make sure the two images that are being compared
        are actually different. Webcam updates about once a minute so 25 images should be long enough
        :return: True if motion occurred, false if motion did not occur
        '''
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
        '''
        Creates an image that highlights the motion between 2 webcam images in red
        aits until 25 images have been retreived to make sure the two images that are being compared
        are actually different. Webcam updates about once a minute so 25 images should be long enough
        :return: The second picture, but with the different pixels highlighted in red
        '''
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

    def event(self):
        '''
        Determines if there is an event going on in the quad. Based on the color and euclidean distance of
        two images in the quad
        :return: True if there is an event, false if otherwise
        '''
        while len(self.img_intensity) < 1:
            pass

        pxl_coor = (250, 365, 500, 470)
        img_grey_large = np.asarray(self.img[-1])
        img_event = np.asarray(self.img[-1])
        img = self.img[-1].crop(pxl_coor)
        baseline = np.asarray(img)

        baseline.setflags(write=1)
        img_grey_large.setflags(write=1)
        img_event.setflags(write=1)

        for i in range(len(baseline[1, :])):
            for j in range(len(baseline[:, i])):
                baseline[j, i] = [170, 170, 168]

        for i in range(249,500):
            for j in range(365, 470):
                img_grey_large[j, i] = [170, 170, 168]
                img_event[j, i] = [255, 255, 255]

        img_grey = Image.fromarray(baseline, 'RGB')
        img_grey_large = Image.fromarray(img_grey_large, 'RGB')
        img_event = Image.fromarray(img_event, 'RGB')

        img_compare = ImageChops.subtract(img, img_grey)
        euclidean_dist = mth.sqrt(np.sum(np.array(img_compare.getdata()) ** 2))

        img_grey_large.show()
        img_event.show()

        if euclidean_dist > 8000:
            return True
        else:
            return False


if __name__ == '__main__':
    test = MUCamera()
    # print(test.average_intensity())
    # print(test.daytime())
    # print(test.motion())
    # print(test.common_color())
    # test.highlight_motion()
    print(test.event())
    # start = time.time()
    # time.sleep(350)
    # print("stopping...")
    # test.stop()




