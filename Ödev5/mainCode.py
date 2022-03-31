import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import simpsom as sps
data = pd.read_csv("airline-safety.csv")
x = data.drop(["airline","avail_seat_km_per_week"], axis=1)

#Ağın oluşturulması
net = sps.SOMNet(20,20,x.values, PBC=True)

#Ağın Eğitilmesi
#Öğrenme katsayısı 0.01, epok sayısı 10000
#Burak hocanın dökümanında güncel olmayan şekli yazılmış, Ferruh diyor ki güncel hali bu
#train algoritması online olmazsa sonuç yanlış çıkıyor
net.train(train_algo='online',start_learning_rate=0.01, epochs=10000)

#Veri noktalarının 2 boyutlu haritaya gömülmesi ve kümeleme
map1 = np.array((net.project(x.values)))
kmeans = KMeans(n_clusters=3, max_iter=300, random_state=0)

y_kmeans = kmeans.fit_predict(map1)

data["kümeler"] = kmeans.labels_
print(data[data["kümeler"]==0].head(5))
print(data[data["kümeler"]==1].head(5))
print(data[data["kümeler"]==2].head(5))

pd.set_option('display.max_columns', None)