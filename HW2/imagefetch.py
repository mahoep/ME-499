#!usr/bin/env python3
'''
    @author Matthew Hoeper
'''

import webcam, time, csv, os.path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal


def moving_average():

    avg = []
    lst_time = []
    datafile = 'E:/Users/Matt/Documents/Programming Projects/ME-499/HW2/image_data.csv'
    dir = 'E:/Users/Matt/Documents/Programming Projects/ME-499/HW2/images/'
    if os.path.isfile(dir+datafile) == True:
        raise OSError("File already exists, please rename file")
    else:
        pass
    while time.time() < 1527607800:
        with open(datafile, 'w', newline='') as f:
            now = time.time()

            filename = 'MU_{}.jpg'.format(now)
            mu_live = webcam.Webcam().grab_image()
            mu_live.save(dir+filename, 'JPEG')

            print("image grabbed at {}".format(now))
            intensity = mu_live.getdata()
            pxlavg = []
            for i in list(intensity):
                pxlavg.append(np.mean(i))

            avg.append(np.mean(pxlavg))
            lst_time.append(now)

            csvRow = [now, np.mean(pxlavg)]
            wr = csv.writer(f)
            wr.writerow(csvRow)
            time.sleep(1)

    avg = []
    lst_time = []
    with open(datafile) as file:
        for row in csv.reader(file):
            lst_time.append(float(row[0]))
            avg.append(float(row[1]))



    t0 = lst_time[0]
    lst_time[:] = [(x - t0)/60 for x in lst_time]

    b, a = signal.butter(5, 0.025)
    zi = signal.lfilter_zi(b, a)
    z, _ = signal.lfilter(b, a, avg, zi=zi * avg[0])
    z2, _ = signal.lfilter(b, a, z, zi=zi * z[0])
    y = signal.filtfilt(b, a, avg)

    plt.plot(lst_time, avg, 'k',lst_time, y, 'r--')
    plt.xlabel('Minutes (min)')
    plt.ylabel('Average Intensity')
    plt.legend(('Noisy Signal', 'Filtered Signal'), loc='best')
    plt.show()


if __name__ == '__main__':

    moving_average()




