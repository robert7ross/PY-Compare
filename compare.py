#
# compare.py
# Author: Robert Ross
# Date: 3/14/18
# Description: #Compares 2 seperate lists of items and outputs
#   a list of items that appear on both lists.
#

import sys
file_1_path = ""
file_2_path = ""
output_path = ""


#Load data from the first file
file_1 = open(file_1_path, 'r')
file_1_list = list()

for line in file_1:
    s = line.strip().split(",")[0]
    if s not in file_1_list:
        file_1_list.append(s)

file_1.close()

#Load data from file 2 and compare
file_2 = open(file_2_path, 'r')
match_list = list()

for line in file_2:
    s = line.strip().split(",")[0]
    if s in file_1_list:
        match_list.append(line)

file_2.close()

#Output the data
o = open(output_path, 'w')

for item in match_list:
    o.write(item)

o.close()
            

