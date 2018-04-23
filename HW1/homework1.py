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
    print("....Importing data from", filename ,"....")
    read_obj = csv.reader(fp)

    for row in read_obj:
        try:
            finalScore.append(float(row[-1]))
        except ValueError:
            finalScore.append('null')

        for x in range(0, len(row)-1):
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



#####  PART 1: SCORES
print("....",len(finalScore)-1, "students accounted for....")
for x in range(0, len(finalScore)-1):
    if finalScore[x] == 'null':
        del finalScore[x]

avgScore = np.mean(finalScore)
medianScore = np.median(finalScore)

abvAvg = 0
abvMed = 0
for x in range(0, len(finalScore)-1):
    if finalScore[x] > avgScore:
        abvAvg += 1
    if finalScore[x] > medianScore:
        abvMed += 1
abvAvgPer = (len(finalScore) - abvAvg)/len(finalScore) * 100
abvMedPer = (len(finalScore) - abvMed)/len(finalScore) * 100

print("Average Score:",round(avgScore, 2))
print("Above Average:", str(round(abvAvgPer, 2))+"%")
print("Median Score:",round(medianScore, 2))
print("Above Median:", str(round(abvMedPer, 2))+"%")



#####  PART 2: HARDEST ASSIGNMENT
hw_score_raw = np.reshape(hw_score_raw, (len(finalScore)+1, 10))
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html

hw_score_raw = np.delete(hw_score_raw, (0), axis=0)
# some dumb bug is not letting me convert the np array to floats from str

hw_avg_scores = []
hw_score = []

for y in range(1, np.size(hw_score_raw, 1)):
    for x in range(0, np.size(hw_score_raw, 0)):
        #print(x)
        try:
            hw_score.append(float(hw_score_raw[x, y]))
        except ValueError:
            hw_score.append(0)
                #converting non numbers to 0
    hw_avg_scores.append(np.mean(hw_score))

print("Hardest Assignment: Homework", hw_avg_scores.index(min(hw_avg_scores)))



#####  PART 3: HARDEST Lab
lab_score_raw = np.reshape(lab_score_raw, (len(finalScore)+1, 11))
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html

lab_score_raw = np.delete(lab_score_raw, (0), axis=0)
lab_score = []
lab_avg_scores = []
for y in range(1, np.size(lab_score_raw, 1)):
    for x in range(0, np.size(lab_score_raw, 0)):
        #print(x)
        try:
            lab_score.append(float(lab_score_raw[x, y]))
        except ValueError:
            lab_score.append(0)
                #converting non numbers to 0
    lab_avg_scores.append(np.mean(lab_score))
print("Hardest Assignment: Lab", lab_avg_scores.index(min(lab_avg_scores)))



#####  PART 3: GRADES
a = 0
a_minus = 0
b_plus = 0
b = 0
b_minus = 0
c_plus = 0
c = 0
c_minus = 0
d_plus = 0
d = 0
d_minus = 0
f = 0

for x in finalScore:
    if x > 94:
        a = a + 1
    elif x < 90 and x > 94:
        a_minus = a_minus + 1
    elif x < 90 and x > 87:
        b_plus = b_plus + 1
    elif x < 87 and x > 84:
        b = b + 1
    elif x < 84 and x > 80:
        b_minus =  b_minus + 1
    elif x < 80 and x > 77:
        c_plus = c_plus + 1
    elif x < 77 and x > 74:
        c = c + 1
    elif x < 74 and x > 70:
        c_minus = c_minus + 1
    elif x < 70 and x > 67:
        d_plus = d_plus + 1
    elif x < 67 and x > 64:
        d = d + 1
    elif x < 64 and x > 61:
        d_minus =  d_minus + 1
    else:
        f = f + 1


gradesTot = a + a_minus + b_plus + b + b_minus + c_plus + c + c_minus + d_plus + d + d_minus + f
print("A:",a)
print("A-:",a_minus)
print("B+:",b_plus)
print("B:",b)
print("B-:",b_minus)
print("C+:",c_plus)
print("C:",c)
print("C-:",c_minus)
print("D+:",d_plus)
print("D:",d)
print("D-:",d_minus)
print("F:",f)