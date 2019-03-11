#!/usr/bin/env python

import sys

infile = sys.argv[1]
outfile = sys.argv[2]

a = open(infile, 'r')
b = open(outfile, 'w')

c = 0
l = a.readline()
while c < 10:
    b.write(l)
    l = a.readline()
    c += 1

b.close()