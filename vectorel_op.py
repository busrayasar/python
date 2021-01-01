# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:59:49 2021

@author: busra
"""
#Vektörel Operasyonlar

#OOP
a = [1,2,3,4]
b = [2,3,4,5]

#global alanda boş liste tanımla vektör çarpımı için
ab = []

for i in  range(0, len(a)):
    ab.append(a[i]*b[i])
    
ab

#FP
import numpy as np

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
a*b
