#PENGENALAN TIPE DATA STRING

kata = "ini adalah string tipe data string"
print(kata)
print(type(kata))

#cara membuat string

'''

1.dengan menggunakan tanda petik satu '...'
2.dengan menggunakan tanda petik dua "..."
3.menggabungkan tanda petik satu dan dua '"..."'
4.menggabungkan tanda petik dua dan satu "'...'"

'''

contoh1 = '\nmenggunakan tanda petik satu'
print(contoh1)
print('contoh1 masuk kedalam tipe data',type(contoh1))

contoh2 = "\nmenggunakan tanda petik dua"
print(contoh2)
print("contoh2 masuk kedalam tipe data",type(contoh2))

contoh3 = '\n"menggabungkan tanda petik satu dan dua"'
print(contoh3)
print('"contoh3 masuk kedalam tipe data"',type(contoh3))

contoh4 = "\n'menggabungkan tanda petik satu dan dua'"
print(contoh4)
print('"contoh4 masuk kedalam tipe data"',type(contoh4))


#menyambung string

print("\n")
nama_pertama = "Heri"
nama_tengah = "Herviansya"
nama_akhir = "Syaputra"

nama_lengkap = nama_pertama +" "+ nama_tengah +" "+ nama_akhir
print (nama_lengkap)

#menghitung panjang string
print("\n")
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang),"karakter")

#memeriksa karakter string pada string
print("\n")
H = "H"
status = H in nama_lengkap
print("string " + H +" ada di " + nama_lengkap + " = " + str(status))

#mengulang string
print("\n")
print("ha"*15)
print(15*"ha")

#indexing
print("\n")
print("index ke-0 : " + nama_lengkap [0])
print("index ke-1 : " + nama_lengkap [1])
print("index ke-2 : " + nama_lengkap [2])
print("index ke-3 : " + nama_lengkap [3])
print(" Dan seterusnya ")


