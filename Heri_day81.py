from ensurepip import version
from os import stat, system
tampung_nama = []
tampung_nim = []
tampung_prodi = []
tampung_angkatan = []


def judul():
    print('   PROGRAM BIODATA MAHASISWA   ')
    print('=============================')

def menu():
    judul()
    print(' 1. Tambah data Mahasiswa')
    print(' 2. Lihat data Mahasiswa')
    print(' 3. Ubah data Mahasiswa')
    print(' 4. Hapus data Mahasiswa')
    print(' 5. Keluar')
    print('=============================')
    pilih2 = input('Pilih Menu : ')

    if pilih2 == '1':
        tambah()
    elif pilih2 == '2':
        lihat()
    elif pilih2 == '3':
        ubah()
    elif pilih2 == '4':
        hapus()
    elif pilih2 == '5':
        selesai()
    else:
        tidak = input('Menu Tidak Ada ')
        menu()

def tambah():
    judul()
    print('Tambah Data'.center(40))
    print('==================================')

    nama = input('Nama Mahasiswa\t  : ')
    tampung_nama.append(nama)
    nim = input('Masukkan NIM\t  : ')
    tampung_nim.append(nim)
    prodi = input('Masukan prodi\t  : ')
    tampung_prodi.append(prodi)
    angkatan = input('Masukkan Angkatan : ')
    tampung_angkatan.append(angkatan)
    
    print('==================================')
    print ('Data Tersimpan'.center(40))
    print('==================================')
    kembali = input('Kembali [enter]')
    menu()

def lihat():
    judul()
    
    for i in range (len(tampung_nama)):

        print('%d. Nama\t\t: %s'%(i+0, tampung_nama[i]))
        print('   Nim\t\t: %s'%tampung_nim[i])
        print('   Prodi\t: %s'%tampung_prodi[i])
        print('   Angkatan\t: %s'%tampung_angkatan[i])
        print('-------------------------------------')
    kembali = input('Kembali Tekan [enter]')
    menu()

def ubah():
    judul()
    def rubah():
        try:
            i = int (input('Inputkan ID : '))
            print('==================================')
            
            if (i > len(tampung_nama[i])):
                print('')
            
            else:   
                namabaru = input('Masukkan Nama Baru  : ')
                tampung_nama[i] = namabaru

                nimbaru = input('Masukkan Nim Baru   : ')
                tampung_nim[i] = nimbaru

                prodibaru = input('Masukkan Prodi Baru : ')
                tampung_prodi[i] = prodibaru

                angkatanbaru = input('Masukkan Angkatan   : ')
                tampung_angkatan[i] = angkatanbaru
            print('==================================')
            print ('Data Tersimpan'.center(40))
            print('==================================')
            kembali = input ('Kembali Tekan [enter]')
            menu()  

        except (IndexError,ValueError):
            kembali = input("Input ID bukan angka/Data tidak ada [enter]") 
            ubah()
    rubah()

def hapus():
    judul()
    def hapuss():
        try:
            print('Hapus Data'.center(40))
            print('==================================')
            i = int(input('Masukkan ID : '))
            
            if (i > len(tampung_nama[i])):
                print('')
            else:

                tampung_nama.remove(tampung_nama[i])
                tampung_nim.remove(tampung_nim[i])
                tampung_prodi.remove(tampung_prodi[i])
                tampung_angkatan.remove(tampung_angkatan[i])
            
            print('-------------------------------------')
            print ('Data Berhasil Dihapus'.center(40))
            print('-------------------------------------')
            kembali = input ('Kembali Tekan [enter]')
            menu()

        except (IndexError,ValueError):
            kembali = input("Input ID bukan angka/Data tidak ada [enter]") 
            hapus()

    hapuss()

def selesai():
    exit()

menu()