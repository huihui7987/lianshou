#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys
cc=[]

def read_input():
    with open('/home/huihui7987/20417.txt') as file:

        for line in file:
            # split the line into words
            yield line.split()

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input()
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in words:
            #print ('%s%s%d' % (word, separator, 1))
            cc.append((word, separator, 1))
    return cc

if __name__ == "__main__":
    main()
    print(cc)

