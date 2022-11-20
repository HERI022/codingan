#Program mengkonversi mata uang 19,Desember,2022.
#Dolar ke Rupiah
#Rupiah ke Dolar



ulang = "Y"
while ulang == "y" or ulang == "Y" :
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
        ulang = input("\nMasih mau mengkonversi (y/t) :")
        
    elif pilihan == "2":
        rupiah = int(input("Masukkan jumlah uang Rupiah = Rp"))
        hasil = float(rupiah / 15692)
        print("Nilai uang Rp",rupiah, "==> $",hasil)
        ulang = input("\nMasih mau mengkonversi (y/t) :")
        print()

    elif pilihan == "3":
        print("Program selesai")
        print("=== TERIMAKASIH ===")
        print()
        break

    else :
        print("anda salah memasukkan program atau pilihan")
        print("Masukkan pilihan dengan benar")
        print(pilihan)
        ulang = input("\nMasih mau mengkonversi (y/t) :")
        print()



