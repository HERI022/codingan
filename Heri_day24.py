#program mencari hasil persamaan kuadrat
#menentukan hasil dari x1 dan x2 dari persamaan kuadrat
#saya mengimpor cmath dari library python
#modul cmath dengan fungsi sqrt.

print(55*"-")
print("\n",10*"=","MENYELESAIKAN PERSAMAAN KUADRAT","="*10,"\n")
print(55*"-")
print("\n","bentuk umum persamaan kuadrat adalah ax**2 + bx + c = 0")

import cmath

z = "(ax**2 + bx + c = 0)"

a = int(input("masukkan nilai dari a :"))
b = int(input("masukkan nilai dari b :"))
c = int(input("masukkan nilai dari c :"))

rumus = int((b**2)-(4*a*c))

#mencari dan menentukan nilai dari x1 dan x2

x1 = (-b - cmath.sqrt(rumus))/(2*a)
x2 = (-b + cmath.sqrt(rumus))/(2*a)

print("\nhasil dari x1 adalah",(x1))
print("hasil dari x2 adalah",(x2))

print("\njadi himpunan penyelesaian dari",z)
print("x1 =",x1,"dan", "x2 =",x2)

print("\n\nPROGRAM SELESAI")

