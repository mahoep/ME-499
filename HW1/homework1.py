#!/usr/bin/env python
'''
   @author Matthew Hoeper
'''

import time, csv, math, numpy as np
#https://pythonspot.com/reading-csv-files-in-python/
print("")
print("....Modules Imported....")

finalScore = []
hwheader = []
hwheader_num = []
labheader = []
labheader_num = []
lab_score_raw = []
# convert to numpy array later
hw_score_raw = np.array([], dtype='f')

filename = 'grades.csv'
with open(filename, 'r') as fp:
    time.sleep(0.25)
    print("....Importing data from", filename, "....")
    read_obj = csv.reader(fp)
    count = 0

    for row in read_obj:
        for x in range(len(row)):
            if "Final Score" in row[x]:
                try:
                    finalScore.append(float(row[x]))
                except ValueError:
                    finalScore.append('null')
            if "Homework" in row[x] and "Score" not in row[x]:
                hwheader.append(row[x][0:len("Homework #")])
                hwheader_num.append(x)
            if "Lab" in row[x] and "Quiz" not in row[x] and "Score" not in row[x]:
                labheader.append(row[x][0:len("Lab #")])
                labheader_num.append(x)

        for j in range(0, len(hwheader_num)):
            hw_score_raw = np.append(hw_score_raw, row[hwheader_num[j]])
            # http://akuederle.com/create-numpy-array-with-for-loop"

        for j in range(0, len(labheader_num)):
            lab_score_raw = np.append(lab_score_raw, row[labheader_num[j]])






