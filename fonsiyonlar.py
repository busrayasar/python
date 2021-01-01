# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 12:15:23 2020

@author: busra
"""

# ?fonksiyon_adı yazarsan o fonkun dökümantasyonunu gösterir
print("a", "b", sep="_") # a ve b elemanlarını "_" ile birleştirir ->a_b


def square(x):
   print( x**2)

square(9) 

#bilgi notu üreten fonksiyon
def square(x):
   print( "The square of entered number " + str(x**2))
   
square(6)
   


#bilgi notu üreten fonksiyon
def square(x):
   print( "Entered number: " + str(x) +", The square of entered number " + str(x**2) )
   
square(6)


def mult(x,y):
    print("Multiplication: " + str(x*y))
    
mult(3 ,4)

#ön tanımlı argümanlar 


def mult(x,y = 1):
    print("Multiplication: " + str(x*y))
    
mult(3)

#Argümanların Sıralaması
def mult(x,y = 1):
    print("Multiplication: " + str(x*y))
    
mult(y=3, x= 7)

#return : fonk return'e gelince durur altında kod varsa görmez
def hesap(isi, nem, sarj):
    return (isi + nem)/ sarj

hesap(30, 40, 60)
      
#local-global vars
x= 10 
y= 20  #bu x ve y global değişkenlerdir

def carp(x,y):
    return x*y   #buradaki x ve y localdir bu fonkun etki alanındadır

carp(2,3)

#local etki alanından global etki alanını değiştirme
x= []  #global etki alanında

def add_elm(y):
    x.append(y)
    print(str(y) + " elemanı eklendi")
    
    #python önce lokal etki alanında elemanı arar ve bulmaya çalışır. örn burdaki x
    #
add_elm()






#TRUE FALSE 
limit=50000

limit == 4000
limit == 50000

#if
gelir = 4000000

if gelir < limit:        #burası true iken if çalışır
    print("Gelir limitten kucuk")
    print("Gelir: " + str(limit))
    
#else
else:
    print("Gelir limitten büyük")

#elif

if gelir > limit:        #burası true iken if çalışır
    print("Tebrikler, odul kazandınız. ")
    print("Gelir: " + str(limit))
    
elif gelir < limit:
    print("Maalesef ödül kazanamadınız. ")
else:
    print("Eşit miktar")



















