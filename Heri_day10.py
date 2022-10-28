# Penggabungan Operasi Komparasi dengan operator Boolean/logika (or) dan (and)

#komparasi boolean (or)

User = int(input("masukkan angka \nLebih kecil dari 3 \natau \nLebih besar dari 10 \n: "))

#memeriksa angka lebih kecil dari 3
KurangDari = (User < 3)
print("angka",User,"kurang dari 3 =",KurangDari)

#memeriksa angka lebih besar dari 10
LebihDari = (User > 10)
print("angka",User,"lebih dari 10 =",LebihDari)

#lebih kecil dari 3 atau lebih besar dari 10
hasil = (KurangDari or LebihDari)
print("angka yang anda masukkan:",hasil)

#jadi jika salah satu angka bernilai True maka hasilnya adalah True.


print("\n",30*"=","\n")


#Komparasi Boolean (and)

User = int(input("masukkan angka \nLebih dari 3 \ndan \nkurang dari 10 \n: "))

#memeriksa angka lebih dari 3
LebihDari = (User > 3)
print("angka",User,"Lebih dari 3 =",LebihDari)

#memeriksa angka lebih besar dari 10
KurangDari = (User < 10)
print("angka",User,"Kurang dari 10 =",KurangDari)

#Lebih dari 3 and kurang dari 10
hasil = (LebihDari and KurangDari)
print("angka yang anda masukkan:",hasil)

#jadi jika salah satu angka bernilai False maka hasilnya adalah False.



