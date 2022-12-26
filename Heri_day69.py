# Menginput Nilai Variabel
x = input('Tuliskan nilai x: ')
y = input('Tuliskan nilai y: ')

tukar = x
x = y
y = tukar

print('Tukar = ',tukar)
print('X =',x)
print('Y =',y)

print('nilai x akan berubah menjadi nilai y dan begitu juga sebaliknya')
print()
print('Nilai x Setelah Ditukar adalah: {}'.format(x))
print('Nilai y Setelah Ditukar adalah: {}'.format(y))