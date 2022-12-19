#Program python ATM sederhana

print('selamat datang di ATM')
print('Pilih Option :')
print('1. check uang saya')
print('2. ambil uang saya')
print('3. tabung uang saya')

pilihan = int(input('Silahkan masukkan pilihan anda :'))
uang_kamu=200000

if pilihan == 1:
    print('uang saya berjumlah Rp.200.000')
    print('besok saya lengkapi programnya')
elif pilihan == 2:
    print('uang saya berjumlah Rp.200.000, mau ambil berapa?')
    print('1. Rp.100.000')
    print('2. Rp.200.000')
    
    pilihan2=int(input('pilihan :'))
    if pilihan2 == 1:
        hasil=uang_kamu-100000
        print('uang kamu sekarang berjumlah',hasil)
        print('besok saya lengkapi programnya')
    elif pilihan2 == 2:
        hasil2=uang_kamu-200000
        print('uang kamu sekarang berjumlah',hasil2)
        print('besok saya lengkapi programnya')
    else:
        print('pilihan anda salah, mohon ulangi lagi!')
        print('besok saya lengkapi programnya')
elif pilihan == 3:
    print('uang kamu sekarang berjumlah Rp.200.000, mau tabung berapa?')
    pilihan3=int(input('masukkan jumlah uang :'))
    hasil3=uang_kamu + pilihan3
    print('jumlah uang kamu sekarang',hasil3)
    print('besok saya lengkapi programnya')
else:
    print('pilihan anda salah, silahkan ulangi kembali!')
    print('besok saya lengkapi programnya')
