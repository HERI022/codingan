print("=== PROGRAM MENGHITUNG NILAI AKHIR MAHASISWA ===\n")

nama=input("Masukkan nama lengkap anda :")
nim=input("masukkan NIM anda :")
matkul=input("masukkan mata kuliah :")
smester=input("masukkan semester :")
print()
tugas=float(input("masukkan nilai tugas :"))
uts=float(input("masukkan nilai UTS :"))
uas=float(input("masukkan nilai UAS :"))

hasil=(tugas * 0.2)+(uts * 0.4)+(uas * 0.4)
print("\n\n")
print("===== Hasil Perhitungan =====")
print("\n")
print("Nama\t\t:",nama)
print("Nim\t\t:",nim)
print("Mata Kuliah\t:",matkul)
print("Semester\t:",smester)
print("Nilai Tugas\t:",tugas)
print("Nilai UTS\t:",uts)
print("Nilai UAS\t:",uas)
print()
print("Hasil Akhir =",hasil)

if hasil >= 90:
    print("Grade : A")
elif hasil >= 80:
    print("Grade : B")
elif hasil >= 75:
    print("Grade : C")
elif hasil >= 50:
    print("Grade : D")
elif hasil < 50:
    print("Grade : E")

if hasil >= 60:
    print("Keterangan : LULUS")
else:
    print("Keterangan : TIDAK LULUS")
