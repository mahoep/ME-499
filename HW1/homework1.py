#!/usr/bin/env python
'''
   @author Matthew Hoeper
'''

import time, csv, math, numpy as np
"https://pythonspot.com/reading-csv-files-in-python/"


finalScore = []
filename = 'grades.csv'
with open(filename, 'r') as fp:
    time.sleep(0.25)
    print(".....Importing data from", filename,"....")
    read_obj = csv.reader(fp)

    for row in read_obj:
        try:
            finalScore.append(float(row[-1]))
        except ValueError:
            finalScore.append('null')


print(len(finalScore)-1, "students accounted for")
for x in range(0, len(finalScore)-1):
    if finalScore[x] == 'null':
        del finalScore[x]
    #print(finalScore[x])

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


