#Cara menggunakan numpy

import numpy as np

tinggi = [1.84, 1.79, 1.82, 1.90, 1.80]
berat = [66.5, 60.3, 64.7, 89.5, 69.8]
print("--------------------------------")
print(tinggi)
print(berat)
print("--------------------------------")
np_tinggi = np.array(tinggi)
print(np_tinggi)
np_berat = np.array(berat)
print(np_berat)

hasil = np_berat / np_tinggi ** 2

print(hasil)

#melihat type
np_tinggi = np.array([1.84, 1.79, 1.82, 1.90, 1.80])
np_berat = np.array([66.5, 60.3, 64.7, 89.5, 69.8])

print(type(np_tinggi))
print(type(np_berat))
print()
    
np_2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np_2d)
print(np_2d.shape)
print()
print(np.array([1,2,3,4,5]))
print(np.array([[1, 2], [3, 4]]))



#contoh import matplotlib

import matplotlib.pyplot as plt

tahun = [1980, 1990, 2000, 2010, 2020]
harga = [2.5, 7.6, 9.7, 15.8, 22.9]

plt.plot(tahun, harga)
plt.show()
print()
plt.scatter(tahun, harga)
plt.show()
print()
plt.bar(tahun, harga)
plt.show()
