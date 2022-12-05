#Menggolongkan tahun kabisat

print("=== MENENTUKAN TAHUN KABISAT ===")

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
            

