mat1 = [[6, 5, 4],
        [2, 7, 3],
        [1, 6, 2]]

mat2 = [[2, 6, 5],
        [3, 2, 4],
        [7, 1, 3]]


#Penjumlahan matriks
hasil = []
for i in range(len(mat1)):
    riks = []
    for j in range(len(mat1[i])):
        riks.append(mat1[i][j] + mat2[i][j])
    hasil.append(riks)

print("Hasil Penjumlahan 2 matriks (mat1 + mat2):")
for riks in hasil:
    print(riks)

print()

#Perkalian matriks
total = []
for i in range(len(mat1)):
    riks2 = []
    for k in range(len(mat2[0])):
        val = 0
        for j in range(len(mat1[i])):
            val += mat1[i][j] * mat2[j][k]
        riks2.append(val)
    total.append(riks2)
        
print("Hasil Perkalian 2 Matriks (mat1 * mat2) :")
for riks2 in total:
    print(riks2)
