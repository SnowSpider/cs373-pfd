#!/usr/bin/env python

# --------------------------
# Wonjun Lee & Daniel Moreno
# --------------------------

"""
To run the program
    % python RunPFD.py < RunPFD.in > RunPFD.out
    % chmod ugo+x RunPFD.py
    % RunPFD.py < RunPFD.in > RunPFD.out

To document the program
    % pydoc -w PFD
"""

import sys
import random
from PFD import pfd_solve

# input generator
def genRandInput (size) :
    input_file = open("RunPFD.in", "w")
    s = str(size) + " " + str(size-1)
    b = []
    a = [0] * size
    for k in range(1, size + 1):
        a[k-1] = k
    random.shuffle(a)
    current = a.pop()
    b.append(current)
    while len(b) != size:
        temp = ""
        current = a.pop()
        temp = str(current) + " " + str(len(b))
        for i in b:
            temp += " " + str(i)
        s += "\n" + temp
        b.append(current)
    input_file.write(s)
    input_file.close()

genRandInput(100)
pfd_solve(sys.stdin, sys.stdout)
