# Perulangan (loop)
# ada dua perulangan yaitu for dan while. tapi saya akan fokus ke for dulu.
# Penggunakan perulangan for

print("\n",10*"=","PERULANGAN FOR (FOR LOOP)","="*10)

#penggunaan for dengan list

angka_list = [0,1,2,3,4,5,6,7,8,9,10] #ini adalah list
print(angka_list)

for Heri in angka_list :
    print("Heri si tampan dan pemberani :",Heri)

print("contoh penggunaan for dengan list\n")

#penggunaan for dengan range

angka_range = range(10)
print(angka_range)

for Heri in angka_range :
    print("Heri si tampan dan pemberani",Heri)

print("contoh penggunaan for dengan range 10\n")

angka_range2 = range(1,11) # ada batas start dan batas akhir.
print(angka_range2)

for Heri in angka_range2 :
    print("Heri si tampan dan pemberani",Heri)

print("contoh penggunaan for dengan range 1 sampai 10\n")

#penggunaan for dengan string

jumlah_str = "Heri si tampan dan pemberani"
print(jumlah_str)

for Heri in jumlah_str :
    print("Heri si tampan dan pemberani",Heri)

print("contoh penggunaan for dengan string")





