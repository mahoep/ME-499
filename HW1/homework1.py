#!/usr/bin/env python
'''
   @author Matthew Hoeper
'''

import time, csv, math, numpy as np
#https://pythonspot.com/reading-csv-files-in-python/
print("")
print("....Modules Imported....")


def read_in_csv(file):


    with open(file, 'r') as fp:
        read_obj = csv.reader(fp)
        headers = []
        final_score = []
        count = 0


        for row in read_obj:
            if count == 0:
                for i in range(len(row)):
                    headers.append(row[i])

            for x in range(len(row)):
                if "Final Score" == headers[x]:
                    try:
                        final_score.append(float(row[x]))
                    except ValueError:
                        pass
            count += 1
    return final_score


def read_in_np(file):


    data = np.genfromtxt(file, delimiter=',')
    #https: // stackoverflow.com / questions / 3518778 / how - to - read - csv - into - record - array - in -numpy

    return data


def read_in_csv_alt(file):
    with open(file, 'r') as fp:
        data_raw = csv.reader(fp,
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


def final_score_stat(list):


    avg_final_score = np.mean(list)
    med_final_score = np.median(list)

    above_avg = 0
    above_med = 0
    for x in list:
        if x > avg_final_score:
            above_avg += 1
        if x > med_final_score:
            above_med += 1
    above_avg_ratio = (len(list) - above_avg)/len(list) * 100
    above_med_ratio = (len(list) - above_med)/len(list) * 100

    print("Average Score:", "%.2f" % avg_final_score)
    print("Above Average:", "%.2f" % above_avg_ratio, '%')
    print("Average Score:", "%.2f" % med_final_score)
    print("Above Average:", "%.2f" % above_med_ratio, '%')

if __name__ == '__main__':

    file = 'grades.csv'
    final_score = read_in_csv(file)
    final_score_stat(final_score)

