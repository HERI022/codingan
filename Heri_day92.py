# Penskalaan merupakan suatu prosedur penempatan atau pemberian nilai (kuantifikasi) suatu karakteristik objek amatan dengan suatu bilangan yang berasal dari suatu kontinum tertentu.

print("\n=== PROGRAM PENGSKALAAN ===")
print()
x1 = int(input("Masukkan nilai dari x1 : "))
x2 = int(input("Masukkan nilai dari x2 : "))
x3 = int(input("Masukkan nilai dari x3 : "))
print()
y1 = int(input("Masukkan nilai y1 : "))
y2 = int(input("Masukkan nilai y2 : "))
y3 = int(input("Masukkan nilai y3 : "))

print("\n=== POSISI AWAL ===")
print("titik1 : ", x1,",",y1)
print("titik2 : ", x2,",",y2)
print("titik3 : ", x3,",",y3)

sx = int(input("Masukkan nilai kelas sx : "))
yx = int(input("Masukkan nilai kelas yx : "))

print("\n=== POSISI AKHIR ===")

print("titik1 : ", x1 * sx,",",y1 * yx)
print("titik2 : ", x2 * sx,",",y2 * yx)
print("titik3 : ", x3 * sx,",",y3 * yx)