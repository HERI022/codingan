print(10*"=","Mencari bilangan ganjil yang habis dibagi 3","="*10)
print(9*"=","lalu menjumlahkan setiap bilangan yang muncul","="*9)
print()

mulai = 1
data = []

user = int(input("Masukkan angka batas akhir :"))

for i in range(mulai, (user+1)) :
    if i%3 == 0 and i%2 != 0 :
        data.append(i)

print()
print(data)

print()
karakter = len(data)
print("jumlah bilangan ganjil yang muncul dari",mulai, "sampai", user, "=",karakter, "bilangan ganjil\n")
print("Semua bilangan ganjil yang muncul akan di jumlahkan.")

print("hasil penjumlahan dari semua bilangan ganjil yang muncul =",sum(data),"\n")

print("\nPROGRAM SELESAI`")