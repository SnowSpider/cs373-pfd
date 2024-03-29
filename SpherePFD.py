#!/usr/bin/env python

# --------------------------
# Wonjun Lee & Daniel Moreno
# --------------------------

import sys
import heapq

#verts = None #array of Vertex
numVert = 0; #number of vertices
numRule = 0; #number of rules

# ------
# Vertex
# ------

class Vertex:
    def __init__(self, numPred = 0, succs = None):
        self.numPred = numPred #number of predecessors
        self.succs = succs #list of successors
        VertexList = [0,[]] * numVert
        
        """
        a = Vertex()
        b = Vertex(2, [1, 2, 3])
        """
# --------
# pfd_read
# --------

def pfd_read (r) :
    """
    reads up to 100 vertices into verts
    r is a  reader
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    numVert = int(l[0])
    numRule = int(l[1])
    assert numVert > 0 and numVert <= 100
    assert numRule > 0 and numRule <= 100
    v = [[0,[]]] #build the Vertex array
    for i in range(1, numVert):
        temp = [0,[]]
        v.append(temp)
    s = r.readline()
    for i in range(0, numRule):
        if s == "":
            return False
        l = s.split()
        v[int(l[0])-1][0] = int(l[1]) #verts[l[0]].numPred = l[1]
        #verts[l[0]].preds = [0] * (len(l)-2) #I don't know whether this line is necessary
        lenl = len(l)
        for j in range(2,lenl):
            v[int(l[j])-1][1].append(int(l[0]))
            #verts[l[j]-1].succ.append(l[0])         
        s = r.readline()
    return v

# --------
# pfd_eval
# --------

def pfd_eval (v) : 
    """
    evaluates the given array of vertices
    return int array of vertex id in order of dependency
    """
    a = []
    
    hq = []
    heapq.heapify(hq)
    lenv = len(v)
    while len(a) != lenv:
        for i in range (lenv):
            if v[i][0] == 0:
                if v[i][1] != []: 
                    lenvi1 = len(v[i][1])
                    for j in range (lenvi1):
                        v[v[i][1][j] - 1][0] -= 1
                    a.append(i+1)
                    v[i][0] = -1
                    break
                else:
                    a.append(i+1)
                    v[i][0] = -1
    return a

# ---------
# pfd_print
# ---------

def pfd_print (w, v) :
    """
    prints the values v
    w is a writer
    v is the ordered list of vertices
    """
    """
    s = ""
    for k in range(len(v)-1):
        s += str(v[k])
        s += " "
    s += str(v[numVert-1])
    w.write(s)
    """
    
    """
    s = []
    for k in xrange(len(v)):
        s.append(str(v[k]))
    w.write(' '.join(s))
    """
    lenv = len(v)
    w.write(' '.join([str(v[k]) for k in xrange(lenv)]))
    
# ---------
# pfd_solve
# ---------

def pfd_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    f = pfd_read(r)
    v = pfd_eval(f)
    pfd_print(w, v)
    
pfd_solve(sys.stdin, sys.stdout)
