# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 09:29:41 2021

@author: busra
"""
class dataScientist():
    print("This is a class")


#Class attributes
class dataSci():
    department = ''
    sql = 'Evet'
    experience_year = 0
    known_langs = []
    
#class attributes erişimi
dataSci.department
dataSci.sql

#class attributes değiştirmek
dataSci.sql = 'Hayir'

#instantiation - sınıf örnekleme
busra = dataSci()

busra.sql
busra.experience_year
busra.known_langs.append("Python") #burada eklediğin bütün class instancelarına eklenmiş gibi davranır
busra.known_langs

veli = dataSci()
veli.known_langs

#Ornek ozellikleri - sınıfın genel özelliklerini değiştirmeden örnek üzerinden o örneğin değerlerini değiştirme
class DataScientist():
    bildigi_diller = ["R", "Python"]
    department = ''
    sql = 'Evet'
    experience_year = 0
    known_langs = []
    def __init__(self): #self örneklemleri- instanceleri temsil eder
        self.bildigi_diller = []
        self.department = ''
        
ali = DataScientist()
ali.bildigi_diller

ayse = DataScientist()
ayse.bildigi_diller

ali.bildigi_diller.append("Python")
ali.bildigi_diller

ayse.bildigi_diller.append("R")
ayse.bildigi_diller

DataScientist.bildigi_diller

print(DataScientist.department ) 
ali.department = "statistics"
print(DataScientist.department)
print(ayse.department)
ayse.department = "cse"
print(ayse.department)
print(DataScientist.department)

























