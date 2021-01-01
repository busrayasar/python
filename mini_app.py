# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 21:35:24 2020

@author: busra
"""
#if , for, fonk

#maaslara 3000 üzerine %10, altına %20
maaslar = [1000, 2000, 3000, 4000, 5000]

def zam20(maas):
    zamlı_maas = maas + maas*20/100
    print(zamlı_maas)
    
def zam10(maas):
    zamlı_maas = maas + maas*10/100
    print(zamlı_maas)
    

for i in maaslar: #listenin içinde döngüyle gezecek, i her bir elemanı temsil eden geçici değişken
    if i > 3000:
        zam10(i)
    else:
        zam20(i)

