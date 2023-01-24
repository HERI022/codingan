print ('PROGRAM PILIHAN')


print ('')
def memilih():
    a=input('pilihan(masukan angka)\n1-Menghitung Jarak\n2-Menghitung Energi Kinetik, Potensial, Mekanik'
            '\n3-Menghitung Gaya Couloumb\n4-Keluar\nMasukan Pilihan: ')
    return a
pilihan = 1
while pilihan <=4:
    pilihan = int(memilih())
    if pilihan == 1:
        print()
        print ('Menghitung Jarak Tempuh Kendaraan ')
        v0=float(input('Berapa Kecepatan Awal Kendaraan (meter/detik): '))
        a=float(input('Berapa Percepatan Kendaraan? (meter/detik): '))
        t=float(input('Berapa Lama Waktu Bergerak(detik): '))
        jarak=(v0*t)+(0.5*a)*t*t
        print ('Jarak Tempuh kendaraan =',int(jarak),'meter')
        print(50*'=')
        print('\n')
        continue
    elif pilihan == 2:
        print()
        print ('Menghitung Energi Kinetik, Energi Potensial dan Energi Mekanik')
        m=float(input('Berapa Massa Benda? (Kilogram): '))
        h=float(input('Berapa Ketinggian Benda? (Meter): '))
        v=float(input('Berapa Kecepatan Benda? (Meter/Detik): '))
        g=9.81
        energikinetik = 0.5*m*v*v
        energipotensial = m*g*h
        energimekanik = energipotensial + energikinetik
        print ('Hasil Perhitungan Energi Kinetik, Energi Potensial, Energi Mekanik')
        print ('Energi Kinetik Pada Benda adalah   :',energikinetik,'Joule')
        print ('Energi Potensial Pada Benda adalah :',energipotensial,'Joule')
        print ('Energi Mekanik Pada Benda adalah   :',energimekanik,'Joule')
        print ('---------------------------============--------------------------------')
        print('\n')
        continue
    elif pilihan == 3:
        print()
        print ('Menghitung Gaya Coulomb')
        Q1=float(input('Masukan Muatan Pertama: '))
        Q2=float(input('Masukan Muatan Kedua: '))
        R=float(input('Masukan Jarak Pada Muatan (Meter): '))
        k=9*10**9
        FCoulomb=k*Q1*Q2/R**2
        print()
        print ('Hasil Perhitungan Gaya Coulomb')
        print ('Gaya Coulomb adalah :',FCoulomb,'Newton')
        print ('---------------------------============--------------------------------')
        print ('\n')
        continue
    elif pilihan == 4:
        print (' ======================Wassalamualaikum.Wr.Wb====================== ')
        print (' ===========================TERIMAKASIH============================== ')
        exit();