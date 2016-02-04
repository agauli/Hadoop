#!/usr/bin/python
"""
We are interested to see if there is a correlation between the length of a post 
and the length of answers.This is a mapreduce program that would process the forum_node
data and output the length of the post and the average answer (just answer, not comment)
length for each post. We will have to decide how to write both the mapper
and the reducer to get the required result.
"""

import sys
oldNode = None
question_len = 0
answer_len = 0
count = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisNode, nodetype, postlength = data_mapped
    postlength = float(postlength)
    if oldNode and oldNode != thisNode:
	if count == 0:
            print oldNode, question_len, 0
        else:
            print oldNode, question_len, answer_len / count
        oldNode = thisNode
        count = 0
	answer_len = 0
	question_len = 0

    oldNode = thisNode
    if nodetype == "question":
        question_len += postlength
    if nodetype == "answer":
        answer_len += postlength
        count += 1

if oldNode != None:
	if count == 0:
            print oldNode, question_len, 0
        else:
            print oldNode, question_len, answer_len / count

   
