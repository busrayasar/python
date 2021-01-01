# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 21:04:50 2020

@author: busra
"""
ogrenci = ["ali","veli", "berk","nur"]

for i in ogrenci:
    print(i)
    
    
    
maaslar = [1000, 2000, 3000, 4000, 5000]

for j in maaslar:
    print(j)
    
    
#maaslara yüzde yirmi zam yapılacak
maaslar = [1000, 2000, 3000, 4000, 5000]

def zam(maas):
    zamlı_maas = maas + maas*20/100
    print(zamlı_maas)
    
for i in maaslar: #listenin içinde döngüyle gezecek
    zam(i)