#!/usr/bin/env python
'''
   @author Matthew Hoeper
'''

import time, csv, math, numpy as np
"https://pythonspot.com/reading-csv-files-in-python/"


finalScore = []
header = []
header_num = []
# convert to numpy array later
hw0_score = []
hw1_score = []
hw2_score = []
hw3_score = []
hw4_score = []
hw5_score = []
hw6_score = []
hw7_score = []
hw8_score = []
hw9_score = []
filename = 'grades.csv'
with open(filename, 'r') as fp:
    time.sleep(0.25)
    print("....Importing data from", filename,"....")
    read_obj = csv.reader(fp)

    for row in read_obj:
        try:
            finalScore.append(float(row[-1]))
        except ValueError:
            finalScore.append('null')

        for x in range(0, len(row)-1):
            if "Homework" in row[x] and "Score" not in row[x]:
                header.append(row[x][0:len("Homework #")])
                header_num.append(x)
        try:
            hw0_score.append(float(row[header_num[0]]))
        except ValueError:
            hw0_score.append('null')


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

print(header_num)