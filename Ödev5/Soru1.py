import pandas as pd
import numpy as np
import simpsom as sps#Kendi kendini organize eden harikatalar(SimpSom basit som kütüphanesi)
from sklearn.cluster import KMeans
#verisetinin yüklenesi ve ayarlanması
veri=pd.read_csv("mall_customers.csv")

X=veri.drop(["CustomerID","Genre"],axis=1)
#Ağ oluşturulması
net = sps.SOMNet(20,20,X.values,PBC=True)#(yükseklik,genişlik,veri,PBC=veriler arasındaki sınırlar)
#Ağın Eğitilmesi
net.train(train_algo='online',start_learning_rate=0.01, epochs=10000)#(0.01=öğrenme katsayısı,10000=epok sayısı)

#veri noktalarının 2 boyutlu bir haritaya gömülmesi ve kümeleme yapılması
hrt=np.array(net.project(X.values))#2 boyutlu haritaya gömme 
kOrt=KMeans(n_clusters=3,max_iter=300,random_state=0)#kümeleme(3 denmesinin sebebi 3 çıkış istediğimiz için)

#Örneklerin hangi kümelere ait olduğunu belirleyeceğiz
yOrt=kOrt.fit_predict(hrt)

#kümelerin etiketlenmesi
veri["kümeler"]=kOrt.labels_
#1 numaları kümenin değerlerine bakılması(yani 0. index)
print(veri[veri["kümeler"]==0].head(5))
#2 numaları kümenin değerlerine bakılması(yani 1. index)
print(veri[veri["kümeler"]==1].head(5))
#3 numaları kümenin değerlerine bakılması(yani 2. index)
print(veri[veri["kümeler"]==2].head(5))


