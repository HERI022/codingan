#program menghitung luas bangun datar
#saya lanjutkan materi kemarin dengan menggunakan fungsi (function)
#Melengkapi program saya dengan perulangan.

selesai = False
def menu () :
    print("\n HERI SI TAMPAN DAN PEMBERANI")
    print("-----------------------------\n")
    print("Dibawah ini program menghitung luas bangun datar\n")

    print(" 1.persegi panjang\n 2.persegi\n 3.segitiga\n")
    print(20*"=")
    
    while selesai == False :    
        user = input("masukkan bangun datar yang ingin anda hitung luasnya :")
        print()

        if user == "1" or user == "persegi panjang" :
            persegi_panjang ()

        elif user == "2" or user == "persegi" :
            persegi ()

        elif user == "3" or user == "segitiga" :
            segitiga ()

        else :
            print("maaf, pilihan anda tidak tersedia.")
            print()

def ulang():
    while True:
        print()
        user2 = input("apakah anda masih mau menghitung luas bangun datar y/t :")
            
        if user2 == "y" or user2 == "Y" :
            menu()

        elif user2 == "t" or user2 == "T" :
            global selesai
            selesai = True 
            break

        else :
            print("anda salah memasukkan program")
        
    print("program berakhir")
    

def persegi_panjang () :
    print("anda mau menghitung luas persegi panjang")
    p = float(input("masukkan panjang sisi dalam cm :"))
    l = float(input("masukkan lebar sisi dalam cm :"))
    if l > p :
        print("panjang =",p)
        print("lebar\t=",l)
        print("rumus luas persegi panjang = panjang * Lebar \n")
        print("anda salah memasukkan panjang dan lebar pada persegi panjang")
        
    else :
        luas = p * l
        print("panjang =",p)
        print("lebar\t=",l)
        print("rumus luas persegi panjang = panjang * Lebar \n")
        print("Luas persegi panjang =",luas, "cm")
        ulang()
        
def persegi () :  
    print("anda mau menghitung luas persegi")   
    s = float(input("masukkan panjang sisi cm :"))  
    luas = s * s
    print("sisi =",s)
    print("rumus luas persegi = sisi * sisi \n")
    print("Luas persegi =",luas, "cm")
    ulang()

def segitiga () :
    print("anda mau menghitung luas segitiga")
    a = float(input("masukkan panjang alas dalam cm :"))
    t = float(input("masukkan tinggi sisi dalam cm :"))
    luas = (a * t)/2
    print("alas =",a)
    print("tinggi =",t)
    print("rumus segitiga = (alas * tinggi) / 2 \n")
    print("Luas segitiga =", luas, "cm")
    ulang()

    
menu()

    



