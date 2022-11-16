print()
print(5*"=","Menampilkan list bilangan ganjil atau genap","="*5,"\n")

while True :
    nilai_awal = int(input("masukkan nilai awal :"))
    nilai_akhir = int(input("masukkan nilai akhir :"))

    print()
    print('''Bilangan yang mau ditampilkan
    1.Ganjil
    2.Genap''')

    print()
    user = int(input("masukkan pilihan anda :"))
    print()

    if user not in [1, 2] :
        print("pilihan salah")
        
    else :
        for x in range(nilai_awal, nilai_akhir + 1) :
            
            if user == 1 and x % 2 == 1 :
                print("bilangan ganjil =",x)

            elif user == 2 and x % 2 == 0 :
                print("bilangan genap =",x)
            
            else :
                print()

    lanjut = input("apakah anda masih ingin lanjut y/t :")
    print()

    if lanjut == "y" :
        print("Silahkan lanjutkan")
        print()

    elif lanjut == "t" :
        break
            
print("program selesai")