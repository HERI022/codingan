#Menggolongkan tahun kabisat
kabisat = False
def menu():
    while (kabisat == False):
        print("=== MENENTUKAN TAHUN KABISAT ===")
        print("================================")
        tahun = int(input("Masukkan sebuah tahun :"))

        #ketentuan pertama
        if (tahun % 4) == 0 :

            #ketentuan kedua
            if (tahun % 100) == 0:

                #ketentuan ketiga
                if (tahun % 400) == 0:
                    print(tahun,"adalah tahun kabisat")

                else:
                    print(tahun,"bukan tahun kabisat")
                
                    
            else:
                print(tahun,"adalah tahun kabisat")
            
                
        else:
            print(tahun,"bukan tahun kabisat")
        ulang()
            
def ulang():
    while True:
        kembali = input("Masih ingin memeriksa tahun kabisat? y/t:")
        if kembali == "y" or kembali == "Y":
            menu()
        elif kembali == "t" or kembali == "T":
            global kabisat
            kabisat = True
            print("Program Selesai")
            break
        else:
            print("Masukkan pilihan y/t dengan benar!")

menu()
