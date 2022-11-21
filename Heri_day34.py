#saya akan membuat suatu pengukuran.
#yang digunakan untuk menunjukkan kategori berat badan seseorang
#Saya menggunakan rumus BMI (Body mass index)
#melengkapi program


while True :
	print("=====", "BMI (Body Mass Index)", "=====")
	
	# <17.0 Sangat Kurus, Kurang Gizi
	# 17.0 - 18.4 Kurus
	# 18.5 - 25.0 Normal
	# 25.1 - 27.0 Gemuk
	# > 27.0 Gemuk, Kelebihan berat badan.
	
	berat = int(input("masukkan berat badan anda dalam Kg :"))
	tinggi = float(input("masukkan tinggi badan anda dalam satuan meter :"))
	BMI = berat / (tinggi*tinggi)
	
	if BMI < 17.0 :
	    print("Sangat Kurus, Kurang Gizi")
	    print()
	
	elif BMI >= 17.0 and BMI <= 18.4 :
	    print("Kurus, kekurangan berat badan")
	    print()
	
	elif BMI >= 18.5 and BMI <= 25.0 :
	    print("Berat badan anda normal")
	    print()
	
	elif BMI >= 25.1 and BMI <= 27.0 :
	    print("Gemuk, kelebihan berat badan")
	    print()
	
	else :
	    print("sangat gemuk, obesitas")
	    print()


	tanya = input("Masih mau menghitung berat badan anda y/t :")
	
	if tanya == "y" or tanya == "Y" :
		print()
		
	elif tanya == "t" or tanya == "T" :
		print("Program Berakhir")
		break
		
	else :
		print("anda salah memasukkan program")
		print("Silahkan input ulang berat dan tinggi badan anda !")
		print()
		
print("TERIMA KASIH")

