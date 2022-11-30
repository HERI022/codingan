print()
print("PROGRAM MENENTUKAN GAJI KARIAWAN")
print("--------------------------------")
print()
print("Menentukan gaji kariawan per jam\n")
nama=str(input("Nama Pegawai    : "))
jam=int(input("Jumlah Jam Kerja : "))
upah=int(input("Gaji Perjam     : "))
print("----------------------------")
print()

if jam >= 8:
    lembur = jam - 8
    rumus = ((8 * jam * upah) + (8 * upah))

else:
    rumus = jam * upah

total = ((upah * jam) + (8 * upah * 6))
print("-----------------------------------------------------------")
print("Nama kariawan =",nama)
print("Jumlah gaji lembur perhari   :",rumus)
print("Jumlah gaji lembur dalam satu minggu :",total)
print("keterangan")
print("Jumlah jam lembur setiap hari adalah sama dalam satu minggu")
print("-----------------------------------------------------------")
