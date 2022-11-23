selesai = False
def menu():
    print()
    print(5*"=","KONVERSI KE SEMUA SATUAN TEMPERATUR","="*5)
    print(47*"=","\n")

    print("==> MENU PILIHAN <==")
    print("==> celcius\t index = c")
    print("==> reamur\t index = r")
    print("==> fahreinheit\t index = f")
    print("==> kelvin\t index = k")
    print()
    print("==> keluar\t index = exit/keluar")
    print()
    print(47*"=","\n")

    while selesai == False:
        satuan = input("Masukkan pilihan index :")

        if satuan == "c" or satuan == "celcius":
            celcius()

        elif satuan == "r" or satuan == "reamur":
            reamur()
        elif satuan == "f" or satuan == "fahreinheit":
            fahreinheit()
        elif satuan == "k" or satuan == "kelvin":
            kelvin()
        elif satuan == "exit" or satuan == "keluar":
            break
        else:
            print("masukkan pilihan index dengan benar!")


def ulang():
    while True:
        print()
        user = input("Apakah anda masih ingin mengkonversi y/t :")

        if user == "y" or user == "Y":
            menu()
        elif user == "t" or user == "T":
            global selesai
            selesai = True
            break
        else:
            print("Masukkan pilihan dengan benar !")

    print("program berakhir")


def celcius():
    suhu = float(input("Masukkan suhu :"))
    print(suhu, "derajat celcius")
    print(suhu, "celcius =",(suhu*(4/5)), "derajat reamur")
    print(suhu, "celcius =",(suhu*(9/5))+32, "derajat fahreinheit")
    print(suhu, "celcius =",(suhu + 273), "derajat kelvin")
    ulang()

def reamur():
    suhu = float(input("Masukkan suhu :"))
    print(suhu, "derajat reamur")
    print(suhu, "reamur =",(suhu*(4/5)), "derajat celcius")
    print(suhu, "reamur =",(suhu*(9/4))+32, "derajat fahreinheit")
    print(suhu, "reamur =",(suhu*(5/4))+273, "derajat kelvin")
    ulang()

def fahreinheit():
    suhu = float(input("Masukkan suhu :"))
    print(suhu, "derajat fahreinheit")
    print(suhu, "fahreinheit =",((5/9)*(suhu-32)), "derajat celcius")
    print(suhu, "fahreinheit =",(4/9*(suhu-32)), "derajat reamur")
    print(suhu, "fahreinheit =",(5/9)*(suhu-32)+273, "derajat kelvin")
    ulang()

def kelvin():
    suhu = float(input("Masukkan suhu :"))
    print(suhu, "derajat kelvin")
    print(suhu, "kelvin =",suhu-273, "derajat celcius")
    print(suhu, "kelvin =",(4/5*(suhu-273)), "derajat reamur")
    print(suhu, "kelvin =",(9/5)*(suhu-273)+32, "derajat fahreinheit")
    ulang()


menu()

