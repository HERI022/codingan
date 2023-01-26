print("\t=== Menghitung Nilai Total dan Rata-Rata ===")
print("------------------------------------------------------------")

array = []
total = 0

n = int(input("Masukkan banyaknya elemen nilai: "))
print()
for x in range(n):
    nilai = float(input("Masukkan nilai ke-{} : ".format(x+1)))
    array.append(nilai)
    
print("=========================")
print("\nHasil nilai total dari semua nilai yang di input adalah : {}".format(sum(array)))

print("Hasil rata-rata dari semua nilai yang di input adalah : {}".format(sum(array)/n))
print("===========================================================================")