#!/usr/bin/env python3
'''
   @author Matthew Hoeper
'''

import numpy as np

from read_in_headers import *
from final_scores import *
from hardest_assignment import *
from hardest_lab import *
from grade_dist import *
from complain import *
from grade_cutoff import *

file = 'grades.csv'
headers = read_in_headers(file)
data = np.genfromtxt(file, delimiter=',')
    #https: // stackoverflow.com / questions / 3518778 / how - to - read - csv - into - record - array - in -numpy

final_stats, scores = final_scores(headers, data)

print("\n", "Average Score:", "%.2f" % final_stats[0])
print("Above Average:", "%.2f" % final_stats[1], '%')
print("Median Score:", "%.2f" % final_stats[2])
print("Median Average:", "%.2f" % final_stats[3], '%',"\n")

print("Hardest Assignment:", hardest_assignment(headers, data),"\n")
print("Hardest Lab:", hardest_lab(headers, data),"\n")

grades = grade_dist(scores)
grade_list = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
for x in range(len(grades)):
    print(grade_list[x],grades[x])

print("\n",complain(scores),"students will complain about their grade.")

print("\n","Grade Cutoffs:")
grade_list = ["A","B","C","D"]
cutoffs = grade_cutoff(scores)
for x in range(len(grade_list)):
    print(grade_list[x], cutoffs[x])
