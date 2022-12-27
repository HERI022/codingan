luas = int(input("Masukkan luas tanah :"))

hasil = luas * 300000

if hasil >= 50000000 and hasil < 100000000 :
	print("Harga tanah sebelum di potong pajak",hasil)
	print("Dikenakan pajak 3%")
	pajak = (hasil * 3)/100
	print("Total pajak",pajak)
	jumlah = hasil - pajak
	print("total harga setelah di potong pajak",jumlah)
elif hasil >= 100000000 :
	print("Harga tanah sebelum di potong pajak",hasil)
	print("Dikenakan pajak 5%")
	pajak = (hasil * 5)/100
	print("Total pajak",pajak)
	jumlah = hasil - pajak
	print("total harga setelah di potong pajak",jumlah)
else:
	print("Harga tanah sebelum di potong pajak",hasil)
	print("Dikenakan pajak 1%")
	pajak = (hasil * 1)/100
	print("Total pajak",pajak)
	jumlah = hasil - pajak
	print("total harga setelah di potong pajak",jumlah)