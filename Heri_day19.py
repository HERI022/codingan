print("\nHERI SI TAMPAN DAN PEMBERANI")

print(5*"=","mencari harga bakso sapi /kg","="*5,"\n")

bakso_s = ((5*5) - (4*4))
bakso_i = ((4*5) - (5*4))
bu_ervin = 550000*5
bu_feni = 530000*4

hasil_eliminasi = bu_ervin - bu_feni
hasil1 = hasil_eliminasi/bakso_s

print(hasil_eliminasi)
print(bakso_s)
print("harga bakso sapi /kg adalah hasil bagi dari",hasil_eliminasi,"/",bakso_s)
print("Jadi harga bakso sapi /Kg adalah :",int(hasil1))
print("\n\n")

print(5*"=","mencari harga bakso ikan /kg","="*5,"\n")

bakso_s = ((5*4) - (4*5))
bakso_i = ((4*4) - (5*5))
bu_ervin = 550000*4
bu_feni = 530000*5

hasil_eliminasi = bu_ervin - bu_feni
hasil2 = hasil_eliminasi/bakso_i

print(hasil_eliminasi)
print(bakso_i)
print("Harga bakso ikan /kg adaLAH hasil bagi dari",hasil_eliminasi,"/",bakso_i)
print("Jadi harga bakso ikan /Kg adalah :",int(hasil2))
print("\n\n")


sapi = 2*hasil1
ikan = 3*hasil2
print("Ibu ijah membeli 2 kg bakso sapi dan 3 kg bakso ikan")
print("jadi ibu ijah harus membayar sebesar :Rp",int(sapi+ikan))






