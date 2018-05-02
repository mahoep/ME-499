#!/usr/bin/env python3
'''
   @author Matthew Hoeper
'''

import time, csv, math, numpy as np
#https://pythonspot.com/reading-csv-files-in-python/

print("....Modules Imported....")
print("")

from read_in_headers import *
from final_scores import *
from hardest_assignment import *
from hardest_lab import *

file = 'grades.csv'
headers = read_in_headers(file)
data = np.genfromtxt(file, delimiter=',')
    #https: // stackoverflow.com / questions / 3518778 / how - to - read - csv - into - record - array - in -numpy

final_scores = final_scores(headers, data)

print("Average Score:", "%.2f" % final_scores[0])
print("Above Average:", "%.2f" % final_scores[1], '%')
print("Average Score:", "%.2f" % final_scores[2])
print("Above Average:", "%.2f" % final_scores[3], '%')

print("Hardest Assignment:", hardest_assignment(headers, data))
print("Hardest Lab:", hardest_lab(headers, data))