#program menghitung luas bangun datar

print("\n HERI SI TAMPAN DAN PEMBERANI")
print("-----------------------------\n")
print("Dibawah ini program menghitung luas bangun datar\n")

print(" 1.persegi panjang\n 2.persegi\n 3.segitiga\n 4.trapesium\n 5.jajargenjang\n 6.belahketupat\n 7.lingkarang")
print(20*"=")

user = input("masukkan bangun datar yang anda hitung luasnya :")
print()

if user == "1" or user == "persegi panjang" :
    print("anda mau menghitung luas persegi panjang")
    print("rumus luas persegi panjang = panjang * Lebar \n")
    p = float(input("masukkan panjang sisi dalam cm :"))
    l = float(input("masukkan lebar sisi dalam cm :"))
    if l > p :
        print("anda salah memasukkan panjang dan lebar pada persegi panjang")
        
    else :
        luas = p * l
        print("Luas persegi panjang =",luas, "cm")

elif user == "2" or user == "persegi" :
    print("anda mau menghitung luas persegi")
    print("rumus luas persegi = sisi * sisi \n")
    s = float(input("masukkan panjang sisi cm :"))
    luas = s * s
    print("Luas persegi =",luas, "cm")

elif user == "3" or user == "segitiga" :
    print("anda mau menghitung luas segitiga")
    print("rumus segitiga = (alas * tinggi) / 2 \n")
    a = float(input("masukkan panjang alas dalam cm :"))
    t = float(input("masukkan tinggi sisi dalam cm :"))
    luas = (a * t)/2
    print("Luas segitiga =", luas, "cm")

elif user == "4" or user == "trapesium" :
    print("anda mau menghitung luas trapesium")
    print("rumus luas trapesium = (sisi atas + sisi bawah)* tinggi / 2 \n")
    a1 = float(input("masukkan panjang alas atas dalam cm :"))
    a2 = float(input("masukkan panjang alas bawah dalam cm :"))
    t = float(input("masukkan tinggi dalam cm :"))
    luas = ((a1 + a2) * t) / 2
    print("Luas trapesium =",luas, "cm")

elif user == "5" or user == "jajargenjang" :
    print("anda mau menghitung luas jajargenjang")
    print("rumus luas jajargenjang = alas * tinggi \n")
    a = float(input("masukkan panjang alas dalam cm :"))
    t = float(input("masukkan tinggi dalam cm :"))
    luas = a * t
    print("Luas jajargenjang =",luas, "cm")

elif user == "6" or user == "belahketupat" :
    print("anda mau menghitung luas belahketupat")
    print("rumus luas belahketupat = (diagonal 1 * diagonal 2) / 2 \n")
    d1 = float(input("masukkan panjang diagonal 1 dalam cm :"))
    d2 = float(input("masukkan panjang diagonal 2 dalam cm :"))
    luas = (d1 * d2) / 2
    print("Luas belahketupat =",luas, "cm")

elif user == "7" or user == "lingkarang" :
    print("anda mau menghitung luas lingkarang")
    print("rumus luas lingkarang = 3.14 *(jari-jari * jari-jari \n")
    r = float(input("masukkan panjang jari-jari dalam cm :"))
    luas = 3.14 *( r * r)
    print("Luas lingkarang =",luas, "cm")

else :
    print("maaf, pilihan anda tidak tersedia.")
