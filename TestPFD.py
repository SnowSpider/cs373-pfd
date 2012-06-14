#!/usr/bin/env python

# -------------------------------
# Author: Wonjun Lee
# -------------------------------

"""
To test the program:
    % python TestPFD.py > TestPFD.out
    % python TestPFD.py &> TestPFD.out
    % chmod ugo+x TestPFD.py
    % TestPFD.py > TestPFD.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from PFD import pfd_read, pfd_eval, pfd_print, pfd_solve

# -------
# TestPFD
# -------

class TestPFD (unittest.TestCase) :
    # ----
    # read
    # ----
    
    def test_read_1 (self) :
        r = StringIO.StringIO("2 1\n1 1 2")
        a = pfd_read(r)
        self.assert_(a == [[1, []], [0, [1]]])
    
    def test_read_2 (self) :
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1")
        a = pfd_read(r)
        self.assert_(a == [[0, [3, 5]], [2, []], [2, [2, 4]], [1, []], [1, [3, 2]]])
    
    def test_read_3 (self) :
        r = StringIO.StringIO("5 1\n5 1 1")
        a = pfd_read(r)
        self.assert_(a == [[0, [5]], [0, []], [0, []], [0, []], [1, []]])
    # ----
    # eval
    # ----
    def test_eval_1 (self) :
        v = pfd_eval([[1, []], [0, [1]]])
        self.assert_(v == [2, 1] )

    def test_eval_2 (self) :
        v = pfd_eval([[0, [3, 5]], [2, []], [2, [2, 4]], [1, []], [1, [3, 2]]])
        self.assert_(v == [1, 5, 3, 2, 4])

    def test_eval_3 (self) :
        v = pfd_eval([[0, [5]], [0, []], [0, []], [0, []], [1, []]])
        self.assert_(v == [1, 2, 3, 4, 5])
        
    # -----
    # print
    # -----
    
    def test_print_1 (self) :
        w = StringIO.StringIO()
        pfd_print(w, [1, 2, 3])
        self.assert_(w.getvalue() == "1 2 3")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        pfd_print(w,[4, 5, 6])
        self.assert_(w.getvalue() == "4 5 6")
    
    def test_print_3 (self) :
        w = StringIO.StringIO()
        pfd_print(w, [7, 8, 9])
        self.assert_(w.getvalue() == "7 8 9")
    
    # -----
    # solve
    # -----
    
    def test_solve_1 (self) :
        r = StringIO.StringIO("2 1\n1 1 2")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "2 1")
    
    def test_solve_2 (self) :
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "1 5 3 2 4")
    
    def test_solve_3 (self) :
        r = StringIO.StringIO("5 1\n5 1 1")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "1 2 3 4 5")
    
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
