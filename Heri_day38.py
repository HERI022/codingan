#program mencari nilai rata-rata dalam list.
#matriks 3x3

matriks1 = [[2, 13,24],
       [20, 11, 23],
       [34, 26, 10]]
print(matriks1)
total = sum(matriks1[0])+sum(matriks1[1])+sum(matriks1[2])
print("hasil penjumlahan =",total)
rata = len(matriks1[0])+len(matriks1[1])+len(matriks1[2])
print("panjang matriks =",rata)
hasil = total / rata
print("rata-rata dari matriks 3x3 diatas =",hasil)
print()


#matriks 5x5

matriks2 = [[1, 8, 4, 10, 6],
            [3, 11, 7, 13, 15],
            [16, 21, 18, 9, 12],
            [19, 14, 22,24, 17],
            [31, 27, 35, 41, 49]]

print("matriks2 =",matriks2)
print()

#mencari nilai terbesar dan terkecil pada elemen yang ditentukan.

terbesar = max(matriks2[2])
print("nilai terbesar dari matriks 5x5 diatas elemen ke-3 adalah",terbesar)
print()

terkecil = min(matriks2[3])
print("nilai terkecil dari matriks 5x5 diatas elemen ke-4 adalah",terkecil)
print()

