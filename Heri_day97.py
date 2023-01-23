import math

def menu_awal():
    pilih_menu = int(input("\nMau mencari apa?\n 1. Hipotenusa Segitiga\n 2. Tinggi segitiga\n 3. Alas Segitiga\n 4. Keluar\n\n Masukkan pilihan anda :"))
    if pilih_menu == 1:
        hipotenusa_segitiga()
       
    elif pilih_menu == 2:
        tinggi_segitiga()
        
    elif pilih_menu == 3:
        alas_segitiga()
        
    else:
        keluar_program()
        

def hipotenusa_segitiga():
    alas_segitiga = int(input("\nMasukan nilai alas dari segitiga: "))
    tinggi_segitiga = int(input("Masukan nilai tinggi dari segitiga: "))
    hipotenusa = int(math.sqrt(tinggi_segitiga ** 2 + alas_segitiga ** 2))
    print(f"\nSisi miring atau hipotenusa = {hipotenusa}")
    print(45*"=")
    menu_awal()

def tinggi_segitiga():
    hipotenusa_segitiga = int(input("\nMasukan nilai sisi miring/hipotenusa dari segitiga: "))
    alas_segitiga = int(input("\nMasukan nilai alas dari segitiga: "))
    tinggi = int(math.sqrt(hipotenusa_segitiga ** 2 - alas_segitiga ** 2))
    print(f"\nTinggi segitiga = {tinggi}")
    print(45*"=")
    menu_awal()
    
def alas_segitiga():
    tinggi_segitiga = int(input("\nMasukan nilai tinggi dari segitiga: "))
    hipotenusa_segitiga = int(input("\nMasukan nilai sisi miring/hipotenusa dari segitiga: "))
    alas = int(math.sqrt(hipotenusa_segitiga ** 2 - tinggi_segitiga ** 2))
    print(f"\nAlas segitiga = {alas}")
    print(45*"=")
    menu_awal()

def keluar_program():
    print("\n Terima Kasih\n ")

menu_awal()
