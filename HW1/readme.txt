In order to run the included python files make sure python3 is being used.
hw1.py is the parent file and all other files are imported into hw1.py

Modules used:
numpy, csv

tested on windows 10, ubuntu 16.04 with python3.5 and 3.6

hw1.py imports the functions from all other files as well as importing the data from csv using
	a numpy function called genfromtext().

Read_in_headers.py reads the csv file and stores the headers in a list. 
	No other data is stored from this file. Corresponds to part 2

final_scores.py calculates the average, median, and percent above average and median
	Corresponds to part 3

hardest_assignment.py determines the most difficult homework assignment by normalizing
	all of the scores based on the assumption that someone always receives  maximum 
	credit. The assignment with the lowest average is returned.

hardest_lab.py does the same exact thing as hardest_assignment.py does but with the lab assignments.

grade_dist.py calculates the number of students that received an A, A-, B+, etc. 
	Input is a list with the final scores. Output is a list a numbers corresponding 
	to A, A-, B+, ect.

complain.py calculates the number of students that are within 0.5% of the next grade up. 
	Input is a list of the final scores. Output is a number.

grade_cutoff.py  calculates the cutoff for the grades of A,B,C,D. 10% get an A, 
	20% get a B, 30% get a C, 30% get a D, and the rest get an F. Input is a list
	of the final scores. Ouput is a list with each cutoff in order of A,B,C,D.