# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:51:06 2020

@author: busra
#TUPLE 
1.Kapsayıcıdırlar str+int vb aynı anda olabilir 2. Sıralıdır 3. Değiştirilemez
"""
t=("ali", "veli", 1,2, [1,2,3])
t
t[1]
t[0:3]
#t[2] = 99 #hata alırsın çünkü tuple değiştirilemez

"""
Dictionary -Sözlük
1. Kapsayıcıdır
2. Sırasızdır
3. Değiştirilebilir
Key,value
"""
sozluk = {"reg":{"reg":"regresyon_modeli", "loj":["MSE",20], "cart":"classification and reg"}, 
          
          "loj":["MSE",20], 
          "cart":"classification and reg"}
#sözlükte value yu list olarak verebiliriz
print (sozluk, len(sozluk))

print(sozluk["loj"]) # sözlükte elemanlara erişim
print(sozluk["reg"]["loj"])

#sözlüğe eleman ekleme
sozluk["GBM"] = "Gradient Boosting Mac"

#sözlükte eleman değiştirme 
sozluk["REG"] = "Çoklu Doğrusal Regresyon"

# sozluk["key"] = "value"

l =[1]
#sozluk[l] ="yeni bir liste"
# sözlüklerde key değerleri ancak sabit veri yapıları ile oluşturulabilir. string integer gibi.
#eğer yukardaki gibi liste koyarsan key değerine unhashable type =list hatası alırsın
"""
sözlüklerde key değerleri sabit veri yapıları olan değiştirilemeyen TUPLE olabilir 
"""
t = ('tuple')
sozluk[t] = "yeni bir tuple"
print(sozluk)
































