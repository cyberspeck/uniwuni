# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:04:58 2017

@author: chrisjoschidavid
"""

import numpy as np
from numpy.linalg import multi_dot
import time

import sys,time,os
import multiprocessing

def m_list(number, seitenlange):
    list = []
    for a in range(number):
        list.append( np.random.random((seitenlange,seitenlange)) )
    return list

def m_multi(list):
    for a in range( len(list)-1 ):
        list[a+1] = np.dot(list[a],list[a+1])
    return list[len(list)-1]


supaliste = m_list(10,200)
supaliste


t0 = time.time()
mulitliste = m_multi(supaliste)
mulitliste
t1 = time.time()

delta_t = t1-t0
delta_t

######################################
# Sandkiste
######################################

t0 = time.time()
# findet optimale Weise um gelistete Matrizen zu multiplizieren
product = multi_dot( list )
t1 = time.time()

delta_t = t1-t0
delta_t


a = np.array( [[1,2,3],
               [4,5,6],
               [7,8,9]] )
# multipliziert einfach 2 Matrizen
np.dot( a,a )
