# konversi satuan temperatur atau suhu.
# program satuan celcius ke satuan lainnya.
# konversi celcius ke satuan reamur, fahreinheit, dan kelvin.

print ("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukkan suhu dalam satuan celcius: "))
print ("Suhu berada dalam", celcius, "celcius")

reamur = (4/5) * celcius
print ("Suhu dalam celcius ke reamur adalah", reamur, "reamur")

fahreinheit = ((9/5) * celcius) + 32
print ("Suhu dalam celcius ke fahreinheit adalah", fahreinheit, "fahreinheit")

kelvin = celcius + 273
print ("Suhu dalam celcius ke kelvin adalah", kelvin, "kelvin")