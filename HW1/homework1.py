#!/usr/bin/env python
'''
   @author Matthew Hoeper
'''

import time, csv, math, numpy as np
#https://pythonspot.com/reading-csv-files-in-python/
print("")
print("....Modules Imported....")


def read_in_csv(filename):


    with open(filename, 'r') as fp:
        time.sleep(0.25)
        print("....Importing data from", filename, "....")
        read_obj = csv.reader(fp)

        headers = []
        count = 0
        for row in read_obj:
            if count == 0:
                headers.append(row)


def read_in_np(filename):


    data = np.genfromtxt(filename, delimiter=',')
    #https: // stackoverflow.com / questions / 3518778 / how - to - read - csv - into - record - array - in -numpy
    return data

def read_in_csv_alt(file):
    with open(file, 'r') as f:
        data_raw = csv.reader(f,
                               delimiter=',',
                               quotechar='"')
        data = [data for data in data_raw]
    return data

def timing():


    filename = 'grades.csv'
    start = time.time()
    data = read_in_csv(filename)
    end = time.time() - start
    print(end)

    start = time.time()
    data = read_in_np(filename)
    end = time.time() - start
    print(end)

    start = time.time()
    data = read_in_csv_alt(filename)
    end = time.time() - start
    print(end)


if __name__ == '__main__':

    timing()