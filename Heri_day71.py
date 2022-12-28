# Gaji pokok masukkan melalui input
#Gaji lembur/jam adalah Rp. 55.000
#Lama lembur lembur dimasukkan melalui fungsi input()
gaji_kotor= int(input("Masukkan gaji kotor :"))

print("Gaji lembur/jam adalah Rp.55.000")

lembur= int(input("Masukkan lama lembur (jam) :"))

print("Gaji Kotor \t:Rp.",gaji_kotor)
print("Lembur (jam)\t:",lembur, "jam")

gajiLembur = lembur * 55000

print("Gaji lembur\t:Rp.",gajiLembur)

hasil=gaji_kotor + gajiLembur

print("gaji bersih\t:Rp.",hasil)