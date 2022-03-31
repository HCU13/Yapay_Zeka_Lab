# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 02:11:14 2022

@author: Gürkan
"""
def Soru1(BirinciAci,IkinciAci,UcuncuAci):
    #BirinciAci:int(input("Açıyı Giriniz:"))
    #IkinciAci:int(input("Açıyı Giriniz:"))
    #UcuncuAci:int(input("Açıyı Giriniz:"))
    
    if(BirinciAci + IkinciAci + UcuncuAci > 180):
        print("Hatalı Giriş Yaptınız!")
        
    elif(BirinciAci > 90 or IkinciAci > 90 or UcuncuAci > 90):
        print("Bu bir geniş açılı üçgendir")
    elif(BirinciAci == 90 or IkinciAci == 90 or UcuncuAci == 90):
        print("Bu bir dik açılı üçgendir")
    else:
        print("Bu bir dar açılı üçgendir")
    
    
def Soru2():
    uzayli_rengi=str(input("Uzaylı rengi girin:"))
    if(uzayli_rengi=="Yeşil"):
        print("Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız")
    else:
        print("Tebrikler, yeşil olmayan uzaylıya ateş ettiğiniz için 10 puan kazandınız")
        
        
def Soru3():
    uzayli_rengi=str(input("Uzaylı rengi girin:"))
    if(uzayli_rengi=="Yeşil"):
        print("Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız")
    elif(uzayli_rengi=="Sarı"):
        print("Tebrikler, sarı uzaylıya ateş ettiğiniz için 10 puan kazandınız")
    elif(uzayli_rengi=="Kırmızı"):
        print("Tebrikler, kırmızı uzaylıya ateş ettiğiniz için 15 puan kazandınız")
    else:
        print("Puan Alamadınız.")
        
        
def Soru4():
    Yas=int(input("Yaşınızı Giriniz: "))
    if(Yas < 2):
        print("Bu kişi bebektir")
    elif(2<=Yas<4):
        print("Bu kişi yeni yürümeye başlayan çocuktur")
    elif(4<=Yas<13):
        print("Bu kişi çocuktur")
    elif(13<=Yas<20):
        print("Bu kişi ergendir")
    elif(20<=Yas<65):
        print("Bu kişi yetişkindir")
    else:
        print("Bu kişi yaşlıdır")
        
def Soru5():
    favori_meyveler=["muz","çilek","ananas","kavun","kivi"]
    ornek_meyveler=["elma","armut","karpuz","kavun","muz","portakal","çilek","vişne","kiraz","mandalina"]
    
    for eleman in ornek_meyveler:
        if eleman in favori_meyveler:
            print(eleman)
            
            
def Soru5v1():
    favori_meyveler=["muz","çilek","ananas","kavun","kivi","karpuz"]
    ornek_meyveler="elma","armut","karpuz","kavun","muz","portakal","çilek","vişne","kiraz","mandalina"
    
    for eleman in ornek_meyveler:
        if eleman in favori_meyveler:
            print(eleman)
    
