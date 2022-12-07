#Membuat Program Login Sederhana.

sandi = False
def menu():
    while (sandi == False):
        print()
        print('Program Login Sederhana')
        print(23*"=")

        username = input('Buat username baru : ')
        password = input('Buat password baru : ')
        print('\n=====Username dan Password Dikonfirmasi=====')

        print()
        username_1 = input('Masukkan username anda : ')
        password_1 = input('Masukkan kata sandi : ')
        print()

        if username == username_1 and password_1 == password :
            print(32*"=")
            print("Login diterima, Selamat datang",username)
            print(32*"=")
            
        else:
            print(32*"=")
            print("Login ditolak, Silahkan coba lagi...!")
            print(32*"=")
        ulang()
        
def ulang():
    while True:
        kembali = input("Ingin menginput kembali username dan password baru y/t :")
        if kembali == "Y" or kembali == "y":
            menu()
        elif kembali == "T" or kembali == "t":
            global sandi
            sandi = True
            print("Program Berakhir")
            break

        else:
            print("masukkan pilihan dengan benar!")

menu()
