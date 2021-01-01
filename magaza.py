# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:55:39 2020

@author: busra
"""
store_name = input("Magaza adı nedir?")
sinir=50000
gelir = int(input("Geliriniz nedir?"))

if gelir > sinir:
    print("Tebrikler " + store_name + " mağazası")
elif gelir < sinir:
    print("Hedefe ulaşamadınız "+ str(gelir))
else:
    print("Daha iyi olmalı")