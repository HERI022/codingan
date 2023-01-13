print(25*"=")
print("PROGRAM PERKALIAN MATRIKS")
print(25*"=")
print()
print("Masukan elemen matriks")

def matriks(x, y):
	list0 = []
	list1 = []
	list2 = []
	
	for i in range (0, x):
		print("Matriks [0,",i,"] : ", end=' ')
		inp = int(input())
		list1.append(inp)
		
	list0.append(list1)
	for i in range(0, y):
		print("Matriks [1,",i,"] :", end=' ')
		inp = int(input())
		list2.append(inp)
		
	list0.append(list2)
	return list0
	
def perkalianMatriks(x, y):
	kali = []
	
	for a in range(0, len(x)):
		baris = []
		
		for b in range(0, len(x[0])):
			total = 0
			
			for c in range(0, len(x)):
				total = x[a] [c]*y[c] [b]
				print(x[a] [c],"*",y[c] [b])
				
			baris.append(total)
		kali.append(baris)
	return kali

matriks1 = matriks(2, 2)
print("Matrik1 : ", matriks1)
matriks2 = matriks(2,2)
print("Matriks2 : ", matriks2)
kali = perkalianMatriks(matriks1, matriks2)
print("Hasil kali kedua matriks: ",kali)