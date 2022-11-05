#Menentukan bilangan ganjil atau genap dengan perulangan dan percabangan

print("\n")
print("Program mengecek bilangan ganjil atau genap")
print("-------------------------------------------")
print("\n")

print("menggunakan: perulangan for")
print(" \t   : perulangan while")
print(" \t   : Input user")
print("\n")

#Menggunakan perulangan for

for bilangan in range(1, 11) :
   
    if (bilangan%2) != 0 :
        print(bilangan,"bilangan ganjil")

    elif (bilangan%2) == 0 :
        print(bilangan,"bilangan genap")

print("\n")

#Menggunakan perulangan while

angka = 0

while angka < 11 :
    angka += 1

    if (angka%2) == 0 :
        print(angka,"masuk dalam bilangan genap")

    elif (angka%2) != 0 :
        print(angka,"masuk dalam bilangan ganjil")
print("\n")

#menggunakan input user

angka = int(input("masukkan bilangan yang ingin anda cek :"))

if (angka%2) != 0 :
    print(angka,"adalah bilangan ganjil")

elif (angka%2) == 0 :
    print(angka,"adalah bilangan genap")
        
