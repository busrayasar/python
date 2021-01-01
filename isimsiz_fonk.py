# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:58:15 2021

@author: busra
"""
#Isimsiz fonksiyonlar - anonymus func
def old_sum(a, b):
    return a+b

old_sum(3,4)


new_sum = lambda a,b : a+b
new_sum(6,8)    

sirasiz_liste = [('b', 3), ('a',8), ('d',12), ('c',1)]
sirasiz_liste

sorted(sirasiz_liste, key = lambda  x : x[1])
#isimsiz olarak fonksiyon yazıp tupleların 2.değerine bakarak sıraladık
