#Program memilih rumus kecepatan, jarak, dan waktu.
#Rumus kecepatan (v = s/t)
#Rumus jarak (s = v*t)
#Rumus waktu (t = s/v)

#ket. kecepatan(v), jarak(s), dan waktu(t)


import os

def kecepatan():
	print('=Hitung Kecepatan atau Kelajuan Siap=\n')
	jarak = float(input('Masukkan jarak dalam satuan meter per detik : '))
	waktu = float(input('Masukkan waktu dalam satuan detik : '))
	kecepatan = jarak / waktu
	print('Kecepatan =',kecepatan,'meter/detik')
	
def jarak():
	print('=Hitung Jarak atau Perpindahan Siap=\n')
	kecepatan = float(input('Masukkan kecepatan dalam satuan meter per detik : '))
	waktu = float(input('Masukkan waktu dalam satuan detik : '))
	jarak = kecepatan * waktu
	print('Jarak =',jarak,'meter')
	
def waktu():
	print('=Hitung Waktu Siap=\n')
	jarak = float(input('Masukkan jarak dalam satuan meter  : '))
	kecepatan = float(input('Masukkan kecepatan dalam satuan meter per detik : '))
	waktu = jarak / kecepatan
	print('waktu =',waktu,'detik')	
		
while True:
	print()
	print(3*'=', 'KECEPATAN, JARAK, DAN WAKTU', '='*3)
	user = int(input('Pilih rumus yang akan dipakai ! \n\n1.Hitung Kecepatan \n2.Hitung Jarak \n3.Hitung Waktu \n0.Keluar \n\nPilih nomor berapa ? : '))
	
	os.system('clear')
	print()
	
	if user == 1 :
		kecepatan()
		print()
	elif user == 2 :
		jarak()
		print()
	elif user == 3 :
		waktu()
		print()
	elif user == 0 :
		print("Program Selesai")
		break
	else :
		print("Anda salah memasukkan program")
		print("masukkan kembali pilihan dengan benar !.")
		print()
	
