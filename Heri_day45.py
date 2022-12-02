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
