def menu ():
	print ("----- MENU -----")
	print ("1. KASIR")
	print ("2. KALKULATOR")
	print ("----------------")
	pilih = input("Pilih menu : ")
	if pilih == "1":
		kasir()
	elif pilih == "2":
		kalkulator()
	else:
		exit
		tanya()
  
def kasir ():
	print ("----- KASIR -----")
	aqua = 3000
	roti = 1000
	barang = input("Nama Barang : ")
	print ("Harga Barang : ",aqua)
	barang = input("Nama Barang : ")
	print ("Harga Barang : ",roti)
	total = (aqua+roti)*90/100
	print ("Total bayar setelah diskon 10% : ",total)
	tanya()


def kalkulator ():
	print ("--- KALKULATOR ---")
	print ("1. (+) 3. (*)")
	print ("2. (-) 4. (/)")
	print ("------------------")
	operasi = input("Pilih operasi : ")
	a = int(input("a : "))
	b = int(input("b : "))
	if operasi == "1":
		print ("Hasil = ",a+b)
	elif operasi == "2":
		print ("Hasil = ",a-b)
	elif operasi == "3":
		print ("Hasil = ",a*b)
	elif operasi == "4":
		print ("Hasil = ",a/b)
	else:
		print ("ERROR")
		tanya()
 
def tanya ():
	tanya = input("Kembali ke menu (y/t)? ")
	if tanya == "y":
		menu()
	elif tanya == "t":
		exit
	else:
		print ("Salah input")

username = input("Username : ")
password = input("Password : ")
if username == "HERI" and password == "D0222544":
	menu()
else:
	print ("LOGIN GAGAL")