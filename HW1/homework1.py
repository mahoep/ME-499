#!/usr/bin/env python3
'''
   @author Matthew Hoeper
'''

import time, csv, math, numpy as np
#https://pythonspot.com/reading-csv-files-in-python/

print("....Modules Imported....")
print("")


def read_in_csv(file):
    '''
    Reads in the csv file and stores the necessary data in arrays
    :requires .csv files:
    '''
    with open(file, 'r') as fp:
        read_obj = csv.reader(fp)
        headers = []
        final_score = []
        hw1 = []
        hw2 = []
        hw3 = []
        hw4 = []
        hw5 = []
        hw6 = []
        hw7 = []
        hw8 = []
        hw9 = []
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

                if "Homework 1" in headers[x]:
                    try:
                        hw1.append(float(row[x]))
                    except ValueError:
                        pass
                if "Homework 2" in headers[x]:
                    try:
                        hw2.append(float(row[x]))
                    except ValueError:
                        pass
                if "Homework 3" in headers[x]:
                    try:
                        hw3.append(float(row[x]))
                    except ValueError:
                        pass
                if "Homework 4" in headers[x]:
                    try:
                        hw4.append(float(row[x]))
                    except ValueError:
                        pass
                if "Homework 5" in headers[x]:
                    try:
                        hw5.append(float(row[x]))
                    except ValueError:
                        pass
                if "Homework 6" in headers[x]:
                    try:
                        hw6.append(float(row[x]))
                    except ValueError:
                        pass
                if "Homework 7" in headers[x]:
                    try:
                        hw7.append(float(row[x]))
                    except ValueError:
                        pass
                if "Homework 8" in headers[x]:
                    try:
                        hw8.append(float(row[x]))
                    except ValueError:
                        pass
                if "Homework 9" in headers[x]:
                    try:
                        hw9.append(float(row[x]))
                    except ValueError:
                        pass
            count += 1
        hw_scores = [hw1,hw2,hw3,hw4,hw5,hw6,hw7,hw8,hw9]

    return final_score, hw_scores


def read_in_np(file):
    '''
    Reads in a csv file and converts the entire thing to a numpy array
    Slower than csv reader from csv library
    :param file:
    :return:
    '''

    data = np.genfromtxt(file, delimiter=',')
    #https: // stackoverflow.com / questions / 3518778 / how - to - read - csv - into - record - array - in -numpy

    return data


def read_in_csv_alt(file):
    '''
    Reads in the csv file and stores the necessary data in arrays
    :requires .csv files:
    '''
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
    '''

    :param list: a list of numbers
    :return: average of the list, median of the list, percent above average and above median
    '''

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

    return [avg_final_score, above_avg_ratio, med_final_score, above_med_ratio]



if __name__ == '__main__':

    file = 'grades.csv'
    final_score, hw_scores = read_in_csv(file)
    final_score_data = final_score_stat(final_score)

    print("Average Score:", "%.2f" % final_score_data[0])
    print("Above Average:", "%.2f" % final_score_data[1], '%')
    print("Average Score:", "%.2f" % final_score_data[2])
    print("Above Average:", "%.2f" % final_score_data[3], '%')


    print(hw_scores)