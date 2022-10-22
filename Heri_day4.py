print("Operator Perbandingan Menggunakan Input User")

#nanti setiap jawabannya itu bolean.
#Ketika nanti hasilnya benar, maka yang muncul = True
#Ketika nanti hasilnya salah, maka yang muncul = False

a = int(input("masukkan nilai a :"))
b = int(input("masukkan nilai b :"))

hasil = a == b
print("Apakah a sama dengan b ?")
print(hasil)

hasil = a != b
print("Apakah a tidak sama dengan b ?")
print(hasil)

hasil = a > b
print("Apakah a lebih besar dari b ?")
print(hasil)

hasil = a < b
print("Apakah a lebih kecil dari b ?")
print(hasil)
