# Kelahiran 1965 - 1979 masuk dalam generasi X
# Kelahiran 1980 - 1994 masuk dalam generasi Y (Milenial)
# Kelahiran 1995 sampai sekarang masuk dalam generasi Z.

print("\n",5*"=","PENENTUAN GENERASI X, Y, DAN Z BERDASARKAN TAHUN LAHIR","="*5)
print(34*"_ ", "\n")

nama = input("Masukkan nama anda :")
tahun = int(input("Masukkan tahun lahir anda :"))

if tahun >= 1965 and tahun <= 1979 :
    print("Nama kamu ",nama)
    print("Kamu lahir pada tahun ",tahun)
    print("kamu masuk dalam generasi X")

elif tahun >= 1980 and tahun <= 1994 :
    print("Nama kamu ",nama)
    print("Kamu lahir pada tahun ",tahun)
    print("kamu masuk dalam generasi Y (Milenial)")

elif tahun >= 1995 :
    print("Nama kamu ",nama)
    print("Kamu lahir pada tahun ",tahun)
    print("kamu masuk dalam generasi Z")

else :
    print("Nama kamu ",nama)
    print("Kamu lahir pada tahun ",tahun)
    print("kamu masuk dalam generasi Baby Boomer")
    print("Baby Boomer adalah generasi sebelum generasi X")
    
