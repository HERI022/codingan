#mengkonversi satuan panjang ke satuan panjang lainnya.


print("\n",5*"=","PROGRAM MENGKONVERSI SATUAN PANJANG","="*5)       
print(48*"=","\n")
print('''1.kilometer/km
2.hektometer/hm
3.dekameter/dam
4.meter/m
5.desimeter/dm
6.centimeter/cm
7.milimeter/mm''')
print(30*"=","\n")


def kilometer () :
    print("\n","1.hektometer/hm\n 2.dekameter/dam\n 3.meter/m\n 4.desimeter/dm\n 5.centimeter/cm\n 6.milimeter/mm\n")
    print(60*"=","\n")
    satuan2 = input("Satuan kilometer ingin dikonversi ke satuan :")

    if satuan2 == "1" or satuan2 == "hektometer" :
          hasil = angka * 10
          print(angka,"kilometer dikonversi ke hektometer =",hasil, "hm")

    elif satuan2 == "2" or satuan2 == "dekameter" :
          hasil = angka * (10 ** 2)
          print(angka,"kilometer dikonversi ke dekameter =",hasil, "dam")

    elif satuan2 == "3" or satuan2 == "meter" :
          hasil = angka * (10 ** 3)
          print(angka,"kilometer dikonversi ke meter =",hasil, "m")

    elif satuan2 == "4" or satuan2 == "desimeter" :
          hasil = angka * (10 ** 4)
          print(angka,"kilometer dikonversi ke desimeter =",hasil, "dm")

    elif satuan2 == "5" or satuan2 == "centimeter" :
          hasil = angka * (10 ** 5)
          print(angka,"kilometer dikonversi ke centimeter =",hasil, "cm")

    elif satuan2 == "6" or satuan2 == "milimeter" :
          hasil = angka * (10 ** 6)
          print(angka,"kilometer dikonversi ke milimeter =",hasil, "mm")

    else :
        print("masukkan pilihan dengan benar")
        print("dengan format angka atau nama satuan")

def hektometer () :
    print("\n","1.kilometer/km\n 2.dekameter/dam\n 3.meter/m\n 4.desimeter/dm\n 5.centimeter/cm\n 6.milimeter/mm\n")
    satuan2 = input("Satuan hektometer ingin dikonversi ke satuan :")

    if satuan2 == "1" or satuan2 == "kilometer" :
          hasil = angka / 10
          print(angka,"hektometer dikonversi ke kilometer =",hasil, "km")

    elif satuan2 == "2" or satuan2 == "dekameter" :
          hasil = angka * 10 
          print(angka,"hektometer dikonversi ke dekameter =",hasil, "dam")

    elif satuan2 == "3" or satuan2 == "meter" :
          hasil = angka * (10 ** 2)
          print(angka,"hektometer dikonversi ke meter =",hasil, "m")

    elif satuan2 == "4" or satuan2 == "desimeter" :
          hasil = angka * (10 ** 3)
          print(angka,"hektometer dikonversi ke desimeter =",hasil, "dm")

    elif satuan2 == "5" or satuan2 == "centimeter" :
          hasil = angka * (10 ** 4)
          print(angka,"hektometer dikonversi ke centimeter =",hasil, "cm")

    elif satuan2 == "6" or satuan2 == "milimeter" :
          hasil = angka * (10 ** 5)
          print(angka,"hektometer dikonversi ke milimeter =",hasil, "mm")

    else :
        print("masukkan pilihan dengan benar")
        print("dengan format angka atau nama satuan")

def dekameter () :
    print("\n","1.kilometer/km\n 2.hektometer/hm\n 3.meter/m\n 4.desimeter/dm\n 5.centimeter/cm\n 6.milimeter/mm\n")
    satuan2 = input("Satuan dekameter ingin dikonversi ke satuan :")

    if satuan2 == "1" or satuan2 == "kilometer" :
          hasil = angka / (10 ** 2)
          print(angka,"dekameter dikonversi ke kilometer =",hasil, "km")

    elif satuan2 == "2" or satuan2 == "hektometer" :
          hasil = angka / 10 
          print(angka,"dekameter dikonversi ke hektometer =",hasil, "hm")

    elif satuan2 == "3" or satuan2 == "meter" :
          hasil = angka * 10
          print(angka,"dekameter dikonversi ke meter =",hasil, "m")

    elif satuan2 == "4" or satuan2 == "desimeter" :
          hasil = angka * (10 ** 2)
          print(angka,"dekameter dikonversi ke desimeter =",hasil, "dm")

    elif satuan2 == "5" or satuan2 == "centimeter" :
          hasil = angka * (10 ** 3)
          print(angka,"dekameter dikonversi ke centimeter =",hasil, "cm")

    elif satuan2 == "6" or satuan2 == "milimeter" :
          hasil = angka * (10 ** 4)
          print(angka,"dekameter dikonversi ke milimeter =",hasil, "mm")

    else :
        print("masukkan pilihan dengan benar")
        print("dengan format angka atau nama satuan")

def meter () :
    print("\n","1.kilometer/km\n 2.hektometer/hm\n 3.dekameter/dam\n 4.desimeter/dm\n 5.centimeter/cm\n 6.milimeter/mm\n")
    satuan2 = input("Satuan meter ingin dikonversi ke satuan :")

    if satuan2 == "1" or satuan2 == "kilometer" :
          hasil = angka / (10 ** 3)
          print(angka,"meter dikonversi ke kilometer =",hasil, "km")

    elif satuan2 == "2" or satuan2 == "hektometer" :
          hasil = angka / (10 ** 2)
          print(angka,"meter dikonversi ke hektometer =",hasil, "hm")

    elif satuan2 == "3" or satuan2 == "dekameter" :
          hasil = angka / 10
          print(angka,"meter dikonversi ke dekameter =",hasil, "dam")

    elif satuan2 == "4" or satuan2 == "desimeter" :
          hasil = angka * 2
          print(angka,"meter dikonversi ke desimeter =",hasil, "dm")

    elif satuan2 == "5" or satuan2 == "centimeter" :
          hasil = angka * (10 ** 2)
          print(angka,"meter dikonversi ke centimeter =",hasil, "cm")

    elif satuan2 == "6" or satuan2 == "milimeter" :
          hasil = angka * (10 ** 3)
          print(angka,"meter dikonversi ke milimeter =",hasil, "mm")

    else :
        print("masukkan pilihan dengan benar")
        print("dengan format angka atau nama satuan")
        

def desimeter () :
    print("\n","1.kilometer/km\n 2.hektometer/hm\n 3.dekameter/dam\n 4.meter/m\n 5.centimeter/cm\n 6.milimeter/mm\n")
    satuan2 = input("Satuan desimeter ingin dikonversi ke satuan :")

    if satuan2 == "1" or satuan2 == "kilometer" :
          hasil = angka / (10 ** 4)
          print(angka,"desimeter dikonversi ke kilometer =",hasil, "km")

    elif satuan2 == "2" or satuan2 == "hektometer" :
          hasil = angka / (10 ** 3)
          print(angka,"desimeter dikonversi ke hektometer =",hasil, "hm")

    elif satuan2 == "3" or satuan2 == "dekameter" :
          hasil = angka / (10 ** 2)
          print(angka,"desimeter dikonversi ke dekameter =",hasil, "dam")

    elif satuan2 == "4" or satuan2 == "meter" :
          hasil = angka / 10
          print(angka,"desimeter dikonversi ke meter =",hasil, "m")

    elif satuan2 == "5" or satuan2 == "centimeter" :
          hasil = angka * 10
          print(angka,"desimeter dikonversi ke centimeter =",hasil, "cm")

    elif satuan2 == "6" or satuan2 == "milimeter" :
          hasil = angka * (10 ** 2)
          print(angka,"desimeter dikonversi ke milimeter =",hasil, "mm")

    else :
        print("masukkan pilihan dengan benar")
        print("dengan format angka atau nama satuan")

def centimeter () :
    print("\n","1.kilometer/km\n 2.hektometer/hm\n 3.dekameter/dam\n 4.meter/m\n 5.desimeter/dm\n 6.milimeter/mm\n")
    satuan2 = input("Satuan centimeter ingin dikonversi ke satuan :")

    if satuan2 == "1" or satuan2 == "kilometer" :
          hasil = angka / (10 ** 5)
          print(angka,"centimeter dikonversi ke kilometer =",hasil, "km")

    elif satuan2 == "2" or satuan2 == "hektometer" :
          hasil = angka / (10 ** 4)
          print(angka,"centimeter dikonversi ke hektometer =",hasil, "hm")

    elif satuan2 == "3" or satuan2 == "dekameter" :
          hasil = angka / (10 ** 3)
          print(angka,"centimeter dikonversi ke dekameter =",hasil, "dam")

    elif satuan2 == "4" or satuan2 == "meter" :
          hasil = angka / (10 ** 2)
          print(angka,"centimeter dikonversi ke meter =",hasil, "m")

    elif satuan2 == "5" or satuan2 == "centimeter" :
          hasil = angka / 10
          print(angka,"centimeter dikonversi ke desimeter =",hasil, "dm")

    elif satuan2 == "6" or satuan2 == "milimeter" :
          hasil = angka * 10
          print(angka,"centimeter dikonversi ke milimeter =",hasil, "mm")

    else :
        print("masukkan pilihan dengan benar")
        print("dengan format angka atau nama satuan")

def milimeter () :
    print("\n","1.kilometer/km\n 2.hektometer/hm\n 3.dekameter/dam\n 4.meter/m\n 5.desimeter/dm\n 6.centimeter/cm\n")
    satuan2 = input("Satuan milimeter ingin dikonversi ke satuan :")

    if satuan2 == "1" or satuan2 == "kilometer" :
          hasil = angka / (10 ** 6)
          print(angka,"milimeter dikonversi ke kilometer =",hasil, "km")

    elif satuan2 == "2" or satuan2 == "hektometer" :
          hasil = angka / (10 ** 5)
          print(angka,"milimeter dikonversi ke hektometer =",hasil, "hm")

    elif satuan2 == "3" or satuan2 == "dekameter" :
          hasil = angka / (10 ** 4)
          print(angka,"milimeter dikonversi ke dekameter =",hasil, "dam")

    elif satuan2 == "4" or satuan2 == "meter" :
          hasil = angka / (10 ** 3)
          print(angka,"milimeter dikonversi ke meter =",hasil, "m")

    elif satuan2 == "5" or satuan2 == "centimeter" :
          hasil = angka / (10 ** 2)
          print(angka,"milimeter dikonversi ke desimeter =",hasil, "dm")

    elif satuan2 == "6" or satuan2 == "milimeter" :
          hasil = angka / 10
          print(angka,"milimeter dikonversi ke centimeter =",hasil, "cm")

    else :
        print("masukkan pilihan dengan benar")
        print("dengan format angka atau nama satuan")






        
        
satuan1 = input("masukkan satuan panjang yang ingin anda konversi :")
angka = float(input("\nBerapa nilai/angka dari satuan yang ingin anda konversi :"))
print(60*"=","\n")

if satuan1 == "1" or satuan1 == "kilometer" :
    print("\nanda ingin mengkonversi satuan kilometer.")
    print("dengan jarak =",angka, "km")
    kilometer ()
    

elif satuan1 == "2" or satuan1 == "hektometer" :
    print("\nanda ingin mengkonversi satuan hektometer.")
    print("dengan jarak =",angka, "hm")
    hektometer ()
    

elif satuan1 == "3" or satuan1 == "dekameter" :
    print("\nanda ingin mengkonversi satuan dekameter.")
    print("dengan jarak =",angka, "dam")
    dekameter ()
    

elif satuan1 == "4" or satuan1 == "meter" :
    print("\nanda ingin mengkonversi satuan meter.")
    print("dengan jarak =",angka, "m")
    meter ()
    

elif satuan1 == "5" or satuan1 == "desimeter" :
    print("\nanda ingin mengkonversi satuan desimeter.")
    print("dengan jarak =",angka, "dm")
    desimeter ()
    

elif satuan1 == "6" or satuan1 == "centiimeter" :
    print("\nanda ingin mengkonversi satuan centimeter.")
    print("dengan jarak =",angka, "cm")
    centimeter ()
    

elif satuan1 == "7" or satuan1 == "milimeter" :
    print("\nanda ingin mengkonversi satuan milimeter.")
    print("dengan jarak =",angka, "mm")
    milimeter ()
    
    

else :
    print("maaf, masukkan pilihan dengan benar!")
    print("program berakhir")
