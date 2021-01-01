# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 10:38:37 2021

@author: busra
"""
#Ornek Metodları - instance methods
class Veribilimci():
    calisanlar = [] #calisanlar nesnesi
    def __init__(self):         #nesnelerin değişebilecek ozellikleri
        self.bildigi_diller = []
        self.bolum = " "
    def dil_ekle(self, yeni_dil):       #class içi methodumuz
        self.bildigi_diller.append(yeni_dil)
        
ali = Veribilimci()
ali.bildigi_diller
ali.bolum

veli = Veribilimci()
veli.bildigi_diller
veli.bolum


dir(Veribilimci) #classımızın methodları ve attributeleri

ali.dil_ekle("Java")
ali.bildigi_diller

veli.dil_ekle("Python")
veli.bildigi_diller

#Miras Yapıları (inheritance)

class Employees():
    def __init__(self, fname, lname, address):         #nesnelerin değişebilecek ozellikleri
        self.FirstName = fname
        self.LastName = lname
        self.Address = address
        
alis = Employees("alis", "soyad", "İstanbul")
alis.Address
alis.FirstName
alis.LastName
        
class DataScience(Employees):  #THATS INHERINTANCE !!!!!!
    def __init__(self):         #nesnelerin değişebilecek ozellikleri
        self.Programming = ""
        
ds1 = DataScience();

      
class Marketing(Employees): #INHERITANCE - EMPLOYEES ÖZELLİKLERİNİ ALDIK
    def __init__(self):         #nesnelerin değişebilecek ozellikleri
        self.StoryTelling = ""
       
               
mar1 = Marketing()
mar1.StoryTelling = "YES"










































