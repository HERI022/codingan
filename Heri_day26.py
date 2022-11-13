#belajar menyisipkan data pada list.
#menambah data di akhir list
#menambah data list dengan list
#index dalam list dimulai dari 0 sampai seterusnya
#index kiri ke kanan itu 0,1,2,3,4,dst
#index kanan ke kiri itu -1,-2,-3,-4,dst

print("\n",10*"=","LIST","="*10)
print()


#Mengambil data pada list

nama = ["Heri","Ikhsan","Andre","Jeprianto","Rio"]

print(nama)

data_pertama = nama[0]
data_kedua = nama[-2]
data_ketiga = nama[1]
data_keempat = nama[-3]
data_kelima = nama[-1]

print("Nama yang muncul pada index [0] adalah =",data_pertama)
print("Nama yang muncul pada index [-1] adalah =",data_kelima)
print("Nama yang muncul pada index [-3] adalah =",data_keempat)
print("Nama yang muncul pada index [-2] adalah =",data_kedua)
print("Nama yang muncul pada index [1] adalah =",data_ketiga)
print("jadi urutan nama yang muncul sesuai index yang saya ambil/panggil pertama kali")

#info jumlah data dalam list

panjang = len(nama)
print()
print("jumlah data dala list =",panjang)

#menyisipkan data pada list
print()

nama.insert(1,"dode")
print("tampilan  data list setelah di sisipkan nama dode")
print(nama)

#menambahkan data pada akhir list
print()

nama.append("aqmal")
print("tampilan data list setelah ditambahkan nama aqmal")
print(nama)

#menambah data list dengan list
print()

nama2 = ["fitri","marhana","rina"]
nama.extend(nama2)
print("tampilan setelah menambahkan data list pada list")
print(nama)









