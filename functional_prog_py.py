# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 11:14:55 2021

@author: busra
"""
#(Birinci sınıf nesnelerdir)
#Yan etkisiz fonksiyonlar (statelesss, girdi-cıktı)
#Yuksek Seviye Fonksiyonlar
#Vektorel Operasyonlar


#Yan Etkisiz Fonksiyonlar (Pure Function)
 #Ornek 1- Bağımsızlık,   Yan etki
A = 6

def impure_sum(b): # saf olmayan , dışarıya  bağımlılıkları olan fonksiyon
    return b + A

def pure_sum(a, b):
    return a + b

impure_sum(4)

pure_sum(5, 6)


#Olumcul yan etkiler 
#OOP
class LineCounter:
    def __init__(self, filename):
        self.filename = open(filename, "r")
        self.lines = []
        
        def read(self):
            self.lines = [line for line in self.file]
            
        def count(self):
            return len(self.lines)
        
lc = LineCounter("deneme.txt")

lc.read()
print(lc.lines)
print(lc.count)

#Functional Programming

def read(filename):
    with open(filename, "r") as f:
        return [line for line in f]
def count(lines):
    return len(lines)

example_lines = read("deneme.txt")
lines_count = count(example_lines)
lines_count










