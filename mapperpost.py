#!/usr/bin/python
"""
We are interested to see if there is a correlation between the length of a post 
and the length of answers.This is a mapreduce program that would process the forum_node
data and output the length of the post and the average answer (just answer, not comment)
length for each post. We will have to decide how to write both the mapper
and the reducer to get the required result.
"""

import sys
import csv

def mapper(stdin):
    """ MapReduce Mapper. """
    reader = csv.reader(stdin, delimiter='\t')
    reader.next()
    for line in reader:
        if len(line) == 19:
            nodetype = line[5]
	    if nodetype == "question":
		ntype = "question"
		nodeid = line[0]
		length = len(line[4])
	    if nodetype == "answer":
	        ntype = "answer"
		nodeid = line[6]
		length = len(line[4])
	    yield '%s\t%s\t%s' % (nodeid, ntype, length)
if __name__ == "__main__":
    for output in mapper(sys.stdin):
        print output
