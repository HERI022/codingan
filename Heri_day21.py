#program menghitung luas bangun datar
#saya lanjutkan materi kemarin dengan menggunakan fungsi (function)

print("\n HERI SI TAMPAN DAN PEMBERANI")
print("-----------------------------\n")
print("Dibawah ini program menghitung luas bangun datar\n")

print(" 1.persegi panjang\n 2.persegi\n 3.segitiga\n")
print(20*"=")

user = input("masukkan bangun datar yang anda hitung luasnya :")
print()

def persegi_panjang () :
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
        
def persegi () :    
    luas = s * s
    print("sisi =",s)
    print("rumus luas persegi = sisi * sisi \n")
    print("Luas persegi =",luas, "cm")

def segitiga () :
    luas = (a * t)/2
    print("alas =",a)
    print("tinggi =",t)
    print("rumus segitiga = (alas * tinggi) / 2 \n")
    print("Luas segitiga =", luas, "cm")


if user == "1" or user == "persegi panjang" :
    print("anda mau menghitung luas persegi panjang")
    p = float(input("masukkan panjang sisi dalam cm :"))
    l = float(input("masukkan lebar sisi dalam cm :"))
    persegi_panjang ()

elif user == "2" or user == "persegi" :
    print("anda mau menghitung luas persegi")   
    s = float(input("masukkan panjang sisi cm :"))
    persegi ()

elif user == "3" or user == "segitiga" :
    print("anda mau menghitung luas segitiga")
    a = float(input("masukkan panjang alas dalam cm :"))
    t = float(input("masukkan tinggi sisi dalam cm :"))
    segitiga ()


else :
    print("maaf, pilihan anda tidak tersedia.")
