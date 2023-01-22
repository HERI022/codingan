# looping dari list 

print("\n=== Menggunakan for ===")
kumpulan_angka = [1,3,5,7,9,11,13,15]
for angka in kumpulan_angka:
    print(f"angka = {angka}")
print("============================\n")

mahasiswa = ["Heri","Ikhsan","Andre","Fyan","Aqmal"]
for nama in mahasiswa:
    print(f"nama = {nama}")

print("============================\n")
print("=== for loop dan range ===")
kumpulan_angka = [1,3,5,2,6,3]
panjang = len(kumpulan_angka)
for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

print("============================")
print("\n=== Menggunakan while ===")
kumpulan_angka = [1,3,5,7,9,8,6]
panjang = len(kumpulan_angka)
i = 0
while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

print("============================\n")
print("=== list komprehension ===")
data = ["HERI", 0,2,3,5,6]
[print(f"data ={i}") for i in data]

# kuadrat
print("============================")
print()
print("=== kuadrat ===")
angka = [1,3,5,7,9,8,6]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print("============================\n")
print("=== enumerate ===")
data_list = ["Heri",1,3,5,7,"Fyan"]
for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")
