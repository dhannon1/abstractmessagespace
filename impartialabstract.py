# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:02:27 2022

@author: ahw769
"""

import numpy as np


def abstract_message_states(n, M):
    size = (len(M))**n
    G = np.zeros((size, n))
    l = range(size-1)
    """iterative over all rows"""
    
    j0 = 0    
    j1 = 0
    j2 = 0
    j3 = 0
    
    j = np.zeros(n)

    
    for i in l:
        """     
        print(str(j0) + str(j1) + str(j2) + str(j3))     
"""

        j[0] = j[0] + 1
        if j[0] >= len(M):
            j[0] = j[0] - len(M)    
        if j[0] == [0]:
            j[1] = j[1] + 1
        if j[1] >= len(M):
            j[1] = j[1] - len(M)
        if j[0] == 0 and j[1] == 0:
            j[2] = j[2] + 1
        if j[2] >= len(M):
            j[2] = j[2] - len(M)
        if j[0]==0 and j[1]== 0 and j[2] == 0:
            j[3] = j[3] + 1
        if j[3] >= len(M):
            j[3] = j[3] - len(M)
        print(str(j[0]) + str(j[1]) + str(j[2]) + str(j[3]))
        
        G[i,0] = M[j[0]]
        G[i,1] = M[j[1]]
        G[i,2] = M[j[2]]
        G[i,3] = M[j[3]]
        
        """
        j0 = j0 + 1
        if j0 >= len(M):
            j0 = j0 - len(M)    
        if j0 == 0:
            j1 = j1 + 1
        if j1 >= len(M):
            j1 = j1 - len(M)
        if j0 == 0 and j1 == 0:
            j2 = j2 + 1
        if j2 >= len(M):
            j2 = j2 - len(M)
        if j0==0 and j1== 0 and j2 == 0:
            j3 = j3 + 1
        if j3 >= len(M):
            j3 = j3 - len(M)
        print(str(j0) + str(j1) + str(j2) + str(j3))
        
        G[i,0] = M[j0]
        G[i,1] = M[j1]
        G[i,2] = M[j2]
        G[i,3] = M[j3]
        
        """
        
    print("Number of states in this space is " + str(size))
    print(G)

     
"""   

def impartiality_constraints(n, M, G):
    for g in G:


def makelp(G,H):
    
    make a new array with imparitality constraints
    
    f= open("abstract.lp", "x")
    f.write("minimize")
    f.write("  alpha")
    f.write("subject to")
    

""" 

M = np.array([0,1])
n = 4

abstract_message_states(n, M)
