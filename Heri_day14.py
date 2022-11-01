#Perulangan
#while loop

print(10*"=","Perulangan while loop","="*10,"\n")

#tipe while menggunakan syarat

angka = 0

while angka < 20 :
    print("while angka ke :",angka)
    angka = angka + 2

print("setiap angka akan ditambah dengan 2 \n")


#tipe while menggunakan input user
print(10*"=","contoh while dengan input user","="*10,"\n")


user = int(input("masukkan angka :"))

while user != 10 :
    print("\nangka yang anda masukkan salah")
    user = int(input("masukkan angka dengan benar : "))

if user == 10 :
    print("angka yang anda input sudah benar")

    
    
    
    

