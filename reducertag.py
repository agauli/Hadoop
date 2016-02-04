#!/usr/bin/python
'''
We are interested seeing what are the top tags used in posts. This is a mapreduce 
program that would output Top 10 tags, ordered by the number of questions they 
appear in.
 
'''

import sys
oldTag = None
count = 0
topten = []

def add_record(thisTag, count, topten):
    if len(topten)<10 or count > topten[9][1]:
        topten.append([thisTag, count])
        topten.sort(key = lambda tup:tup[1],reverse = True)
        topten = topten[:10]
    return topten

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisTag, rep = data_mapped
    postlength = int(rep)
   
    if oldTag and oldTag != thisTag:
        topten = add_record(oldTag, count, topten)
        oldTag = thisTag
        count = 0
    oldTag = thisTag
    count += int(rep)

topten = add_record(oldTag, count, topten)
for tag, count in topten:
    print tag, count


    
