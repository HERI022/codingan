diskon = True
def menu():
	print()
	print("Program Menentukan Harga Diskon")
	print("---------------------------------------\n")
	
	while diskon == True:
		harga = int(input("Masukkan total harga pembelian : "))
		print()
		
		if (harga >= 50000) and (harga <= 100000) :
		    hasil = (harga*10)/100
		    print("Kamu mendapatkan diskon 10% =")
		    print("Dengan potongan harga sebesar 10 persen =",int(hasil))
		    
		elif (harga > 100000) and (harga <= 200000) :
		    hasil = (harga*15)/100
		    print("Kamu mendapatkan diskon 15% =")
		    print("Dengan potongan harga sebesar 15 persen =",int(hasil))
		    
		elif (harga > 200000) and (harga <= 300000) :
		    hasil = (harga*20)/100
		    print("Kamu mendapatkan diskon 20% =")
		    print("Dengan potongan harga sebesar 20 persen =",int(hasil))
		    
		elif (harga > 300000) :
		    hasil = (harga*25)/100
		    print("Kamu mendapatkan diskon 25% =")
		    print("Dengan potongan harga sebesar 25 persen =",int(hasil))
		    
		else:
		    hasil = harga*0
		    print("Maaf, Kamu tidak mendapatkan diskon", int(hasil))
		   
		total = harga-hasil 
		print("Jumlah yang harus anda dibayarkan adalah",int(total))
		ulang()
		

def ulang():
		while True :
			kembali = input("Hitung kembali total harga pembelian y/t :")
			if kembali == "y" or kembali == "Y":
				menu()
			elif kembali == "t" or kembali == "T":
				global diskon
				diskon = False
				break
			else:
				print("Masukkan pilihan dengan benar!")
		
menu()