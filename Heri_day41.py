#Membuat Program Login Sederhana.

import getpass

print()
print('Program Login Sederhana')
print(23*"=")

username = input('Buat username baru : ')
password = input('Buat password baru : ')
print('\n=====Username dan Password Dikonfirmasi=====')

print()
username_1 = input('Masukkan username anda : ')
password_1 = getpass.getpass('Masukkan kata sandi : ')
print()

if username == username_1 and password_1 == password :
    print(32*"=")
    print("Login diterima, Selamat datang",username)
    print(32*"=")
else:
    print(32*"=")
    print("Login ditolak, Silahkan coba lagi...!")
    print(32*"=")
