#Program mengkonversi mata uang 19,Desember,2022.
#Dolar ke Rupiah
#Rupiah ke Dolar

print()
print(10*"=","Konversi Mata Uang","="*10)
print(40*"=")

print("==> Menu Pilihan <==")
print("1.Dolar ke Rupiah")
print("2.Rupiah ke Dolar")
print("3.Keluar")
print(40*"=")

pilihan = input("Masukkan pilihan anda :")

if pilihan == "1":
    dolar = int(input("Masukkan jumlah uang USD =$"))
    hasil = float(dolar * 15692)
    print("Nilai USD $",dolar, "==> Rp",hasil)
    print()

elif pilihan == "2":
    rupiah = int(input("Masukkan jumlah uang Rupiah = Rp"))
    hasil = float(rupiah / 15692)
    print("Nilai uang Rp",rupiah, "==> $",hasil)
    print()

elif pilihan == "3":
    print("Program selesai")
    print("Program ini besok akan saya lengkapi")
    print()

else :
    print("anda salah memasukkan program atau pilihan")
    print("Program ini besok akan saya lengkapi")
    print("Terimakasih")
    print()

