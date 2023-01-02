import sys


print('\t\t\t\t====================')
print('\t\t\t\tTOKO KAMBING IKHSAN')
print('\t\t\t\t====================')
print()

print('TOKOH KAMBING IKHSAN MENYEDIAKAN :')
print('\t\t\t1. Kambing Super   : Rp 2.000..000,-')
print('\t\t\t2. Kambing Reguler : Rp 1.500..000,-')
print('\t\t\t3. Kambing Standar : Rp 1.000..000,-')
print('\t\t\t4. Anak Kambing    : Rp 2.000..000,-')
print()

print('Toko Kambing Ikhsan Memberikan Diskon :')
print('\t\t\t1. Diskon 50% untuk pembelanjaan lebih dari 5 juta')
print('\t\t\t2. Diskon 35% untuk pembelanjaan lebih dari 3 juta sampai 5 juta')
print('\t\t\t3. Diskon 20% untuk pembelanjaan lebih dari 1,5 juta sampai 3 juta')

print()
pilihan = int(input('Mau kambing yang mana (1/2/3/4) ? : '))

if pilihan == 1 :
    hargaKambing = 2000000
elif pilihan == 2 :
    hargaKambing = 1500000
elif pilihan == 3 :
    hargaKambing = 1000000
elif pilihan == 4 :
    hargaKambing = 750000
else :
    print()
    print('Maaf Paket Yang Anda Pilih Tidak Tersedia')
    print('Atas Nama Tokoh Kambing Ikhsan mengucapkan terimakasih')
    sys.exit()

jumlah = int(input('Berapa banyak yang mau di beli ? : '))


pembelanjaan = hargaKambing*jumlah

if pembelanjaan >= 5000000 :
    diskon = 50
elif pembelanjaan >= 3000000 and pembelanjaan < 5000000 :
    diskon = 35
elif pembelanjaan >= 1500000 and pembelanjaan < 3000000 :
    diskon = 20
else:
    diskon = 0


jumlahDiskon = (pembelanjaan * diskon) / 100

hargaAkhir = pembelanjaan - jumlahDiskon

print()
print('\t\t\t\tRekap Pembelanjaan Anda')
print('\t\t\t\t=======================')
print()
print('Pilihan Paket\t :',pilihan)
print('Harga Paket\t :',hargaKambing)
print('jumlah Pembelian :',jumlah)
print('Pembelanjaan\t :',pembelanjaan)
print('Diskon\t\t :',diskon)
print('Jumlah Diskon\t :',jumlahDiskon)
print('----------------------------')
print('HARGA AKHIR      : RP.',hargaAkhir)

print()
print('Teriakasih Atas Kunjungan Anda !!!') 
