print("# Program Hitung Volume & Luas Tabung #")
print("---------------------------------------")
print()
print("Rumus volume tabung adalah (V = π × r² × t) ")
print("Keterangan rumus :\n")
print("\tV = volume tabung")
print("\tπ = phi (22/7 atau 3,14)")
print("\tr = jari-jari tabung")
print("\tt = tinggi tabung")
print(45*"=")
print()
print("Rumus luas permukaan tabung (L = 2 π r(r + t)")
print("Keterangan rumus :\n")
print("\tL = Luas tabung")
print("\tπ = phi (22/7 atau 3,14)")
print("\tr = jari-jari tabung")
print("\tt = tinggi tabung")
print(45*"=")
print()

pi    = 22/7
jari   = float(input("Masukan Jari-jarinya (cm)  : "))
tinggi = float(input("Masukan Tinggginya  (cm)  : "))
volume = pi*jari*jari*tinggi
luas   = 2*pi*jari*(jari+tinggi)

print("-----------------Hasilnya-----------------")
print("Volume Tabung         =",volume,"cm³")
print("Luas Permukaan Tabung =",luas,"cm²")
