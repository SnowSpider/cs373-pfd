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

pfd_solve(sys.stdin, sys.stdout)
