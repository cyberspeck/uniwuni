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
    matrices = []
    for a in range(number):
        matrices.append( np.random.random((seitenlange,seitenlange)) )
    return matrices

def m_multi(matrices):
    result = list(matrices)
    for a in range( len(result)-1 ):
        result[a+1] = np.dot(result[a],result[a+1])
    return result[len(result)-1]


supaliste = m_list(10,200)
supaliste


t0 = time.time()
mulitliste = m_multi(supaliste)
mulitliste
t1 = time.time()

delta_t = t1-t0
delta_t

######################################
# Sandkiste                          #
######################################

t0 = time.time()
# findet optimale Weise um gelistete Matrizen zu multiplizieren
product = multi_dot( supaliste )
t1 = time.time()

delta_t = t1-t0
delta_t