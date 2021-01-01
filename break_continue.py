# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 21:42:34 2020

@author: busra
"""

#maaslara 3000' e gelince durmak istiyoruz
maaslar = [8000, 5000, 2000, 1000, 2000, 3000,7000,  4000, 5000]

#dir(maaslar)
maaslar.sort()
maaslar

for i in maaslar:
    if i == 3000:
        
        print("3000'e ulaşıldı")
        break
    print(i)
    
    
for i in maaslar:
    if i == 3000:
        
        print("3000'i es geç")
        continue
    print(i)
    
    