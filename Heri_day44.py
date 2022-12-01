print("PROGRAM PYTHON MENENTUKAN NILAI INDEKS MAHASISWA")
tugas = float(input("\nMasukkan nilai Tugas, dengan format nilai (1-100) : "))
uts = float(input("Masukkan nilai UTS, dengan format nilai (1-100) : "))
uas = float(input("Masukkan nilai UAS, dengan format nilai (1-100): "))

hasil =  (0.15 * tugas) + (0.35 * uts) +  (0.50 * uas)
if hasil >= 80:
    indeks = 'A'
elif hasil >= 70:
    indeks = 'B'
elif hasil >= 55:
    indeks = 'C'
elif hasil >= 40:
    indeks = 'D'
else:
    indeks = 'E'

print("------------------------------------------------------\n")
print("Nilai Tugas anda =",tugas)
print("Nilai UTS anda =",uts)
print("Nilai UAS anda =",uas)
print("--------------------------")
print("\nNilai Akhir  = ",hasil)
print("Nilai Indeks = ",indeks)