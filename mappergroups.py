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
import csv

def mapper(stdin):
    """ MapReduce Mapper. """
    reader = csv.reader(stdin, delimiter='\t')
    # Skip header.
    reader.next()
    for line in reader:
        if len(line) == 19:
            if line[5] == "question":
                node = line[0]
            else:
                node = line[6]
            author = line[3]  
        yield '%s\t%s' % (node, author)

if __name__ == "__main__":
    for output in mapper(sys.stdin):
        print output
