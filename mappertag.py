#!/usr/bin/python
'''
We are interested seeing what are the top tags used in posts. This is a mapreduce 
program that would output Top 10 tags, ordered by the number of questions they 
appear in.
 
'''

import sys
import csv

def mapper(stdin):
    """ MapReduce Mapper. """
    reader = csv.reader(stdin, delimiter='\t')
    # Skip header.
    reader.next()
    for line in reader:
        if len(line) == 19:
            tag = line[2].split()
            for word in tag: 
	    	yield '%s\t%s' % (word, 1)

if __name__ == "__main__":
    for output in mapper(sys.stdin):
        print output
