mulai = True

def menu():
	while mulai == True :
		print ("=====", "Pembuatan SIM", "=====")
		
		usia = int(input("masukan usia anda :"))
		
		
		if usia <= 16 :
		    print("Maaf, usia anda belum mencukupi untuk pengurusan SIM")
		    print("Silahkan kembali lagi jika usia anda sudah >= 17 tahun")
		
		else :
		    nilai = int(input("masukkan nilai tes anda: "))
		    lulus = "SELAMAT, anda berhak mendapatkan SIM"
		    gagal = "MAAF, anda tidak berhak mendapatkan SIM"
		
		    if nilai >= 80 :
		        print(lulus)
		
		    else :
		        print(gagal)
		        
		ulang()
		     
		        
def ulang():
	while True:
		kembali=input("Masih ingin lanjut y/t :")
		if kembali == "y" or ulang == "Y":
			menu()
		elif kembali == "t" or kembali == "T":
			print("PROGRAM SELESAI")
			global mulai
			mulai = False
			break
		else:
			print("masukkan pilihan dengan benar!")
			
	print("Terimakasih")

menu()