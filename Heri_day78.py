print("=== Menghitung luas dan volume balok ===")
print('----------------------------------------')
print()

# Menginput Panjang, lebar dan Tinggi Balok

p = int(input('masukan panjang balok (cm): '))

l = int(input('masukan lebar balok (cm): '))

t = int(input('masukan tinggi balok (cm): '))

 

# Hitung Luas Permukaan    

Luas = 2 * ( (p*l) + (p*t) + (l*t) )


# Hitung Volume Balok

Volume= p * l * t

print()
print('Jadi balok dengan ukuran :')
print('panjang\t:',p,'cm')
print('lebar\t:',l,'cm')
print('tinggi\t:',t,'cm')
print('============================')
print('luas balok\t:',Luas,'cm**2')
print('Volume balok\t:',Volume,'cm**3')

 