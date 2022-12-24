total = 0
barang = []
harga = []

while True:
    print(""" \n\t===Daftar Barang ===\n
        1. Roti \t 5000
        2. Es Krim \t 7000
        3. Keripik \t 8000
        4. cokelat \t 12000
        5. wafer \t 4000
        6. mie goreng \t 3000
        7. biskuat \t 9000
        """)
    
    pilihan = input("Masukkan nomor barang :")
    if pilihan == "1":
        barang.append(" roti")
        harga.append("5000")
        total += 5000
    elif pilihan == "2":
        barang.append("Es Krim")
        harga.append("7000")
        total += 7000
    elif pilihan == "3":
        barang.append("Keripik")
        harga.append("8000")
        total += 8000
    elif pilihan == "4":
        barang.append("Cokelat")
        harga.append("12000")
        total += 12000
    elif pilihan == "5":
        barang.append("Wafer")
        harga.append("4000")
        total += 4000
    elif pilihan == "6":
        barang.append("mie goreng")
        harga.append("3000")
        total += 3000
    elif pilihan == "7":
        barang.append("Biskuat")
        harga.append("9000")
        total += 9000
    else:
        print("pilihan anda salah")
    
    lanjut = input("lanjut belanja y/t : ")
    if lanjut == "t" or lanjut == "T":
        print()
        break
    
print("Barang yang dibeli :",barang)
print("Dengan harga setiap barang :",harga)
print("Total yang harus dibayarkan :",total, "\n")

uang = int(input("Masukkan uang pembayaran :"))
if uang > total:
    print("Kembaliannya :",uang - total)
elif uang == total:
    print("Uang pas")
else:
    print("Uangnya kurang :",uang - total)
    
    