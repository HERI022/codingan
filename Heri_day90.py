#recursive, memanggil dirinya sendiri

def belajar():
    print("= contoh program Recursive =\n")
    print("1. senin")
    print("2. selasa")
    print("3. rabu")
    print("4. kamis")
    print("5. jum'at")
    print("6. sabtu")
    print("7. minggu")
    pilihan = input("Masukan hari pilihan anda : ")
    

    if pilihan == "senin" or pilihan =="1":
        print("Matkul Bahasa Indonesia\n")
        kembali = input("ketikkan y jika lanjut, n jika tidak: ")
        if kembali == "y":
            belajar() #recursive
        else :
            return
    elif pilihan == "selasa" or pilihan =="2":
        print("Matkul Matematika Dasar\n")
        kembali = input("ketikkan y jika lanjut, n jika tidak : ")
        if kembali == "y":
            belajar() #recursive
        else :
            return
    elif pilihan == "rabu" or pilihan =="3":
        print("Matkul Wawasan Sosial Budaya\n")
        kembali = input("ketikkan y jika lanjut, n jika tidak : ")
        if kembali == "y":
            belajar() #recursive
        else :
            return
    elif pilihan == "kamis" or pilihan =="4":
        print("Matkul pendidikan Kewarganegaraan\n")
        kembali = input("ketikkan y jika lanjut, n jika tidak : ")
        if kembali == "y":
            belajar() #recursive
        else :
            return
    elif pilihan == "jum\'at" or pilihan =="6":
        print("Matkul Dasar-Dasar Pemrograman\n")
        kembali = input("ketikkan y jika lanjut, n jika tidak : ")
        if kembali == "y":
            belajar() #recursive
        else :
            return
    elif pilihan == "sabtu" or pilihan =="6":
        print("Matkul Pendidikan Agama\n")
        kembali = input("ketikkan y jika lanjut, n jika tidak : ")
        if kembali == "y":
            belajar() #recursive
        else :
            return
    elif pilihan == "minggu" or pilihan =="7":
        print("Hari libur. nikmati hari-hari mu\n")
        kembali = input("ketikkan y jika lanjut, jika tidak : ")
        if kembali == "y":
            belajar() #recursive
        else :
            return
    else :
        print("Maaf pilihan anda tidak di temukan\n")
        kembali = input("ketikkan y jika lanjut, n jika tidak : ")
        if kembali == "y":
            belajar() #recursive
        else :
            return
        
belajar()