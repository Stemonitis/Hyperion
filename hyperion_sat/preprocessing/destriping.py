#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 23:51:04 2020

@author: stemonitis
"""

"""Discrete wavelet transform"""
import numpy as np
N = 8
res = [np.sin(k) for k in range(N)]

for k in range(N):
    print(res[k])



def discreteHaarWaveletTransform(x):
    N = len(x)
    output = [0.0]*N

    length = N >> 1
    while True:
        for i in range(0,length):
            summ = x[i * 2] + x[i * 2 + 1]
            difference = x[i * 2] - x[i * 2 + 1]
            output[i] = summ
            output[length + i] = difference

        if length == 1:
            return output

        #Swap arrays to do next iteration
        #System.arraycopy(output, 0, x, 0, length << 1)
        x = output[:length << 1]

        length >>= 1


res = discreteHaarWaveletTransform(res)

for k in range(N):
    print(res[k])
    
    
    
"""MNF transform"""












































