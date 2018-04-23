#!/usr/bin/env python
'''
   @author Matthew Hoeper
'''

import time, csv, math, numpy as np
#https://pythonspot.com/reading-csv-files-in-python/
print("")
print("....Modules Imported....")

finalScore = []
header = []
header_num = []
# convert to numpy array later
hw_score = np.array([])

filename = 'grades.csv'
with open(filename, 'r') as fp:
    time.sleep(0.25)
    print("....Importing data from", filename ,"....")
    read_obj = csv.reader(fp)
    i = 0
    for row in read_obj:
        try:
            finalScore.append(float(row[-1]))
        except ValueError:
            finalScore.append('null')

        for x in range(0, len(row)-1):
            if "Homework" in row[x] and "Score" not in row[x]:
                header.append(row[x][0:len("Homework #")])
                header_num.append(x)

        for j in range(0, len(header_num)):
            hw_score = np.append(hw_score, row[header_num[j]])
            # http://akuederle.com/create-numpy-array-with-for-loop"
        i = i + 1


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
for x in range(0, len(hw_score)):
    try:
        float(hw_score[x])
    except ValueError:
        continue
print(len(hw_score))
hw_score = np.reshape(hw_score, (165, 10))
print(np.size(hw_score, 0))

#https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html

avgHWscore = []
#for y in range(1, np.size(hw_score,1)-1):
    #avgHWscore.append(np.average(hw_score[1:-1,y], 0))
    #print(sum(hw_score[1:-1,y]))