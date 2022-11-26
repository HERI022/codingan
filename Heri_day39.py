# date and time
# Codingan sederhana untuk menghitung umur, hari_lahir.
# semua itu akan muncul ketika kita menginput tanggal lahir, bulan, dan tahun.

import os
lanjut = True
def menu():
	while lanjut == True :
		import datetime as dt
		
		print("\n",10*"=","Heri si Tampan dan Pemberani","="*10,"\n")
		print("Silahkan masukkan tanggal, bulan, dan tahun lahir anda !\n")
		
		tanggal = int(input("Tanggal \t:"))
		bulan = int(input("Bulan \t\t:"))
		tahun = int(input("Tahun \t\t:"))
		
		print("\n")
		tanggal_lahir = dt.date(tahun,bulan,tanggal)
		
		print(f"Tanggal lahir anda adalah :{tanggal_lahir}")
		print(f"Anda lahir pada hari :{tanggal_lahir:%A}")
		
		hari_ini = dt.date.today()
		print("\nHari ini tanggal :",hari_ini)
		print(f"sekarang hari :{hari_ini:%A}")
		
		hari = hari_ini - tanggal_lahir
		tahun = hari.days // 365
		bulan = (hari.days % 365) // 30
		
		print("\nAnda sekarang berusia",tahun, "tahun", bulan, "bulan")
		ulang()

def ulang():
	while True:
		ulang = input("Lanjut memeriksa tanggal lahir y/t :")
		os.system('clear')
		if ulang == "y" or ulang == "Y":
			menu()
		elif ulang == "t" or ulang == "T":
			global lanjut
			lanjut = False
			break
		else:
			print("Masukkan pilihan dengan benar!")
	
	print("Program selesai")

menu()