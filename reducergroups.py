"""We might want to help students form study groups. But first we want 
to see if there are already students on forums that communicate a lot 
between themselves.
As the first step for this analysis we have been tasked with writing a 
mapreduce program that for each forum thread (that is a question node with 
all it's answers and comments) would give us a list of students that 
have posted there - either asked the question, answered a question or added a 
comment. If a student posted to that thread several times, they should be added to that
list several times as well, to indicate intensity of communication."""


import sys
oldNode = None
invd_inforum = []
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    thisNode, authors = data_mapped
    if oldNode and oldNode != thisNode:
        print oldNode, invd_inforum
        oldNode = thisNode
        invd_inforum = []
    oldNode = thisNode
    invd_inforum.append(authors)

if oldNode != None:
    print oldNode, invd_inforum