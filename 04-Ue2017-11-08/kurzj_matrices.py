#-*- coding: utf-8 -*-
import random
import sys
import os
import numpy as np
from numpy.linalg import multi_dot
import time
from multiprocessing.dummy import Pool as ThreadPool

def slowmatrixmultiplication(A, B, C):
    for i in range(0, size):
        for j in range(0, size):
            for k in range(0, size):
                '''
                print(i, "  ", j, "  ", k)
                print(A[i][k])
                print(B[k][j])
                '''
                C[i][j] = C[i][j] + (A[i][k] * B[k][j])

print("Hello World!")

lol = np.array([[1,0], [1,1]])
size = 200
A = np.random.randint(100, size=(size, size))
B = np.random.randint(100, size=(size, size))
'''
A = [[1, 2], [3, 4]]
B = [[4, 3], [1, 2]]
'''
'''
C = []
for i in range(0, size):
    C.append([])
    for j in range(0, size):
        C[i].append(0)
print("Groundwork has been layed. #lol")
t0 = time.time()
'pool = ThreadPool(4)
'results = pool.map(slowmatrixmultiplication(A, B, C))
t1 = time.time()
delta_t = t1 - t0
print("Die Scheikisten hat genau ", delta_t, "s gebraucht. Du brauchst 1 fastere Kisten - lol")
print(C)

for i in range(0, size):
    for j in range(0, size):
        C[i][j] = 0
t0 = time.time()

pool = ThreadPool()
results = pool.map(multi_dot(A, B))
t1 = time.time()
delta_t = t1 - t0
print("Klügere Algorithmen brauchen nur ", delta_t, "s.")
print(C)
'''


'''
print(A)
print("lolololololololol")
print(B)
print("lolololololololol")
print(C)
'''
yoloswag = []
for a in range(0,10):
    yoloswag.append(np.random.random((1000,1000)))
print("Arrays wurden in diese 1 Existenz gebimst.")

t0 = time.time()
pool = ThreadPool(4)
results = pool.map(multi_dot(yoloswag))
t1 = time.time()

delta_t = (t1- t0)

print("Es hat ", delta_t, "s gebraucht.")
