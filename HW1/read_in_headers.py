#!/usr/bin/env python3
'''
   @author Matthew Hoeper
'''

def read_in_headers(file):
    import csv
    '''
    Reads in the csv file and stores the necessary data in arrays
    :requires .csv files:
    '''
    with open(file, 'r') as fp:
        read_obj = csv.reader(fp)
        headers = []
        count = 0


        for row in read_obj:
            if count == 0:
                for i in range(len(row)):
                    headers.append(row[i])
            else:
                break
            count += 1

    return headers