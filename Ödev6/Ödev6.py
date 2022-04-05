#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 16:55:10 2022

@author: can
"""
#kütüphanelerin eklenmesi
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#girdi ve çıktıların tanımlanması
bulaşık_miktarı = ctrl.Antecedent(np.arange(0, 101,15),"bulaşık miktarı")
kirlilik_derecesi = ctrl.Antecedent(np.arange(0,101,15),"kirlilik derecesi")
bulaşık_cinsi = ctrl.Antecedent(np.arange(0,101,15),"bulaşık cinsi")
yıkama_zamanı = ctrl.Consequent(np.arange(30,161,10),"yıkama zamanı")
deterjan_miktarı = ctrl.Consequent(np.arange(0,93.5,17.5),"deterjan miktarı")
su_sıcaklığı = ctrl.Consequent(np.arange(35,68.5,15),"su sıcaklığı")
üst_sepet = ctrl.Consequent(np.arange(2100,3501,200),"üst sepet pompa devri")
alt_sepet = ctrl.Consequent(np.arange(2100,3501,200),"alt sepet pompa devri")

#üyelik fonksiyonlarının belirlenmesi
#girdi değerleri için
bulaşık_miktarı.automf(3)
kirlilik_derecesi.automf(3)
bulaşık_cinsi.automf(3)

#çıktı değerleri için
yıkama_zamanı["çok kısa"] = fuzz.trimf(yıkama_zamanı.universe,[30,30,60,])
yıkama_zamanı["kısa"] = fuzz.trimf(yıkama_zamanı.universe, [40,60,90])
yıkama_zamanı["orta"] = fuzz.trimf(yıkama_zamanı.universe,[70,100,120])
yıkama_zamanı["uzun"] = fuzz.trimf(yıkama_zamanı.universe,[100,130,150])
yıkama_zamanı["çok uzun"] = fuzz.trimf(yıkama_zamanı.universe,[130,150,160])
deterjan_miktarı["çok az"] = fuzz.trimf(deterjan_miktarı.universe,[0,0,17.5])
deterjan_miktarı["az"] = fuzz.trimf(deterjan_miktarı.universe,[17.5,32.5,42.5])
deterjan_miktarı["normal"] = fuzz.trimf(deterjan_miktarı.universe,[32.5,57.5,67.5])
deterjan_miktarı["çok"] = fuzz.trimf(deterjan_miktarı.universe,[57.5,82.5,92.5])
deterjan_miktarı["çok fazla"] = fuzz.trimf(deterjan_miktarı.universe,[82.5,82.5,92.5])
su_sıcaklığı["düşük"] = fuzz.trimf(su_sıcaklığı.universe,[35,37.5,50])
su_sıcaklığı["normal"] = fuzz.trimf(su_sıcaklığı.universe,[37.5,50,67.5])
su_sıcaklığı["yüksek"] = fuzz.trimf(su_sıcaklığı.universe,[55,55,67.5])
üst_sepet["çok düşük"] = fuzz.trimf(üst_sepet.universe,[2100,2300,2400])
üst_sepet["düşük"] = fuzz.trimf(üst_sepet.universe,[2300,2400,2700])
üst_sepet["normal"] = fuzz.trimf(üst_sepet.universe,[2600,2700,3000])
üst_sepet["yüksek"] = fuzz.trimf(üst_sepet.universe,[2900,3000,3300])
üst_sepet["çok yüksek"] = fuzz.trimf(üst_sepet.universe,[3200,3300,3500])
alt_sepet["çok düşük"] = fuzz.trimf(alt_sepet.universe,[2100,2300,2400])
alt_sepet["düşük"] = fuzz.trimf(alt_sepet.universe,[2300,2400,2700])
alt_sepet["normal"] = fuzz.trimf(alt_sepet.universe,[2600,2700,3000])
alt_sepet["yüksek"] = fuzz.trimf(alt_sepet.universe,[2900,3000,3300])
alt_sepet["çok yüksek"] = fuzz.trimf(alt_sepet.universe,[3200,3300,3500])

#üyelik fonksiyonlarının görsel olarak incelenmesi
bulaşık_miktarı.view()


kirlilik_derecesi.view()


bulaşık_cinsi.view()


yıkama_zamanı.view()


deterjan_miktarı.view()


su_sıcaklığı.view()


üst_sepet.view()


alt_sepet.view()


#kuralların belirlenmesi
kural1 = ctrl.Rule(bulaşık_miktarı["poor"]|kirlilik_derecesi["poor"]|bulaşık_cinsi["poor"],  üst_sepet["çok düşük"])

kural2 = ctrl.Rule(bulaşık_miktarı["poor"]|kirlilik_derecesi["good"]|bulaşık_cinsi["average"],üst_sepet["düşük"])

kural3 = ctrl.Rule(bulaşık_miktarı["average"]|kirlilik_derecesi["average"]|bulaşık_cinsi["good"], üst_sepet["yüksek"])

kural4 = ctrl.Rule(bulaşık_miktarı["good"]|kirlilik_derecesi["good"]|bulaşık_cinsi["average"],üst_sepet["düşük"])

kural5 = ctrl.Rule(bulaşık_miktarı["poor"]|kirlilik_derecesi["good"]|bulaşık_cinsi["average"],yıkama_zamanı["orta"])

kural6 = ctrl.Rule(bulaşık_miktarı["average"]|kirlilik_derecesi["average"]|bulaşık_cinsi["good"],yıkama_zamanı["orta"])

kural7 = ctrl.Rule(bulaşık_miktarı["poor"]|kirlilik_derecesi["poor"]|bulaşık_cinsi["poor"], yıkama_zamanı["kısa"])

kural8= ctrl.Rule(bulaşık_miktarı["good"]|kirlilik_derecesi["good"]|bulaşık_cinsi["average"],yıkama_zamanı["çok uzun"])

kural9 = ctrl.Rule(bulaşık_miktarı["poor"]|kirlilik_derecesi["poor"]|bulaşık_cinsi["poor"],deterjan_miktarı["çok az"])
                   
kural10 = ctrl.Rule(bulaşık_miktarı["poor"]|kirlilik_derecesi["good"]|bulaşık_cinsi["average"],deterjan_miktarı["normal"])

kural11 = ctrl.Rule(bulaşık_miktarı["average"]|kirlilik_derecesi["average"]|bulaşık_cinsi["good"],deterjan_miktarı["normal"])         
                  
kural12 = ctrl.Rule(bulaşık_miktarı["good"]|kirlilik_derecesi["good"]|bulaşık_cinsi["average"],deterjan_miktarı["çok fazla"])
                   
kural13 = ctrl.Rule(bulaşık_miktarı["poor"]|kirlilik_derecesi["poor"]|bulaşık_cinsi["poor"],su_sıcaklığı["düşük"])

kural14 = ctrl.Rule(bulaşık_miktarı["poor"]|kirlilik_derecesi["good"]|bulaşık_cinsi["average"],su_sıcaklığı["yüksek"])  
                   
kural15 = ctrl.Rule(bulaşık_miktarı["average"]|kirlilik_derecesi["average"]|bulaşık_cinsi["good"],su_sıcaklığı["normal"])
                   
kural16 = ctrl.Rule(bulaşık_miktarı["good"]|kirlilik_derecesi["good"]|bulaşık_cinsi["average"],su_sıcaklığı["yüksek"])         
 
kural17 = ctrl.Rule(bulaşık_miktarı["poor"]|kirlilik_derecesi["poor"]|bulaşık_cinsi["poor"],alt_sepet["çok düşük"])

kural18 = ctrl.Rule(bulaşık_miktarı["poor"]|kirlilik_derecesi["good"]|bulaşık_cinsi["average"],alt_sepet["çok yüksek"])

kural19 = ctrl.Rule(bulaşık_miktarı["poor"]|kirlilik_derecesi["good"]|bulaşık_cinsi["average"],alt_sepet["yüksek"])

kural20 = ctrl.Rule(bulaşık_miktarı["good"]|kirlilik_derecesi["good"]|bulaşık_cinsi["average"],alt_sepet["çok yüksek"])
        
#durumların belirlenmesi
yıkama_zamanıKontrol = ctrl.ControlSystem([kural5,kural6,kural7,kural8])
yıkama_zamanıBelirleme = ctrl.ControlSystemSimulation(yıkama_zamanıKontrol)
deterjan_miktarıKontrol = ctrl.ControlSystem([kural9,kural10,kural11,kural12])
deterjan_miktarıBelirleme = ctrl.ControlSystemSimulation(deterjan_miktarıKontrol)
su_sıcaklığıKontrol = ctrl.ControlSystem([kural13,kural14,kural15,kural16])
su_sıcaklığıBelirleme = ctrl.ControlSystemSimulation(su_sıcaklığıKontrol)
üst_sepetKontrol = ctrl.ControlSystem([kural1,kural2,kural3,kural4])
üst_sepetBelirleme = ctrl.ControlSystemSimulation(üst_sepetKontrol)
alt_sepetKontrol = ctrl.ControlSystem([kural17,kural18,kural19,kural20])
alt_sepetBelirleme = ctrl.ControlSystemSimulation(alt_sepetKontrol)


#durumların hesaplanması
yıkama_zamanıBelirleme.input["bulaşık miktarı"] = 50
yıkama_zamanıBelirleme.input["kirlilik derecesi"] = 10
yıkama_zamanıBelirleme.input["bulaşık cinsi"] = 10
yıkama_zamanıBelirleme.compute()
print(yıkama_zamanıBelirleme.output["yıkama zamanı"])


deterjan_miktarıBelirleme.input["bulaşık miktarı"] = 50
deterjan_miktarıBelirleme.input["kirlilik derecesi"] = 50
deterjan_miktarıBelirleme.input["bulaşık cinsi"] = 50
deterjan_miktarıBelirleme.compute()
print(deterjan_miktarıBelirleme.output["deterjan miktarı"])


su_sıcaklığıBelirleme.input["bulaşık miktarı"] = 50
su_sıcaklığıBelirleme.input["kirlilik derecesi"] = 50
su_sıcaklığıBelirleme.input["bulaşık cinsi"] = 50
su_sıcaklığıBelirleme.compute()
print(su_sıcaklığıBelirleme.output["su sıcaklığı"])


üst_sepetBelirleme.input["bulaşık miktarı"] = 50
üst_sepetBelirleme.input["kirlilik derecesi"] = 50
üst_sepetBelirleme.input["bulaşık cinsi"] = 50
üst_sepetBelirleme.compute()
print(üst_sepetBelirleme.output["üst sepet pompa devri"])


alt_sepetBelirleme.input["bulaşık miktarı"] = 50
alt_sepetBelirleme.input["kirlilik derecesi"] = 50
alt_sepetBelirleme.input["bulaşık cinsi"] = 50
alt_sepetBelirleme.compute()
print(alt_sepetBelirleme.output["alt sepet pompa devri"])

#görsel olarak inceleme
yıkama_zamanı.view(sim=yıkama_zamanıBelirleme)

deterjan_miktarı.view(sim=deterjan_miktarıBelirleme)

su_sıcaklığı.view(sim=su_sıcaklığıBelirleme)

üst_sepet.view(sim=üst_sepetBelirleme)

alt_sepet.view(sim=alt_sepetBelirleme)

