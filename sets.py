# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:18:55 2020

@author: busra

PYTHON SETS 
1.Sırasızdır.
2.Değerleri eşsizdir.
3.Değiştirilebilirdir.
4.Farklı tipleri barındırabilir.
Setler hız - performans odaklıdır,uniqe değerler varken kullanılır- matematikteki kümeler 
"""
s = set()

listem = [1, "l", "python"]
s = set(listem)
print(s)

tuplee = ("t", "tuple")

s= set(tuplee)
print(s)

jack = "look at the stars "
type(jack)
s =set(jack)
print(s) #birden fazla tekrarlanan değeri bir kez alır

lis = ["jack ", "goes", "to", "the", "space", "goes", "to", "the", "space"]
s = set(lis)
print(s , len(s))
#----------------------------------------------------------------------------
"""
Set(Küme)lere eleman ekleme ve çıkarma
"""
my_list =["computer", "science"]

s= set(my_list)
print(s)

#print(dir(s)) # içindeki parametrenin tipine göre fonksiyonları listeler
s.add("engineering")
print(s) # setler otutta alfabetik sırada görüntülenir
#aynı elemanı tekrar ekleyemezsin
s.remove("science")
s.discard("science") #sildiğin elemanı tekrar silmeye çalışırken kod akışının kesilmesini önler

#SETLER KLASIK KUME IŞLEMLERİ
# SEÇİLİ KOD BLOĞUNU CTRL VEYA  ALT+4 İLE YORUM BLOĞUNA ALIRIZ / YA DA SEÇ EDIT'E GEL ADD BLOCK COMMENT
# CTRL + 1 İLE satır başına "#" atabilirsin

# =============================================================================
# difference() ile iki kümenin farkını ya da "-" ifadesiyle 
# intersection() iki kümenin kesişimi veya "&" ifadesiyle
# union() iki kümenin birleşimi
# symmetric_difference() ikisinde de olmyanları
# =============================================================================

set1 = set([1,2,3,4,5,7,])
set2 = set([1,2,9,8,5,7,10]) 
# set1 de olup set2 de olmayan değerler
print(set1.difference(set2))
set1 - set2
# set2 de olup set1 de olmayan değerler
print(set2.difference(set1))
set2 - set1
#ikisinde de olayan elemanlar
print(set1.symmetric_difference(set2))
# SET INTERSECTION AND UNION
kesisim = set1.intersection(set2)
print("Intersection:" , kesisim )
print("Intersection:" , set2.intersection(set1))

birlesim = set1.union(set2)
print("union:", birlesim)

print("İntersection_update", set1.intersection_update(set2))

#Setlerde sorgu işlemleri

Set1= set([1,2,3,5,7,8,10])
Set2 = set([5,6,7,8,9,10])

#Bu iki kümenin birleşimi boş mu?
print(set1.isdisjoint(set2))
#bu kümenin bütün elemanları diğer kümenin içinde yer alıyormu
print(set1.issubset(set2))
#bir kümenin diğer bir kümeyi kapsayıp kapsamadığı
print(set2.issuperset(set1))





































































 