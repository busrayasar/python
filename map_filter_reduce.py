# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 15:07:43 2021

@author: busra
"""
#map_filter_reduce

liste = [1,2,3,4,5]
for i in liste:
    print(i+10)
    
    
list(map(lambda x: x*10, liste))  #her elemanın üzerine 10 ekleme işlemi FP

#list işlemin sonucunu saklayıp görmek için kullandık
#map fonk verilen bir vektörün içerisinde belirli bir fonksiyonu çalıştırma imkanı verir- isimsiz fonk

#filter
#iterative bir nesne alır , iterative nesne oluşturur ve şartı sağlayanları filtreler
liste = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x % 2 == 0, liste))

#reduce 
from functools import reduce #bu modül içerisinden fonk import ettik

liste = [1,2,3,4]
reduce(lambda a,b : a+b, liste)