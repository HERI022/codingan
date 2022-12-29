#Buatlah program yang dapat menerima inputan berupa angka dengan ketentuan sebagai berikut:

#Jika angka yang diinput habis dibagi 3, maka program akan mencetak pesan "Pride of 3"

#Jika angka yang diinput habis dibagi 5, maka program akan mencetak pesan "Pride of 5"

#Jika angka yang diinput habis dibagi 3 dan 5, maka program akan mencetak pesan "Master Class



angka = int(input("Masukkan Angka :"))

if angka % 3 == 0 and angka % 5 == 0 :
	print("Angka yang anda masukkan adalah",angka)
	print("master Class")
elif angka % 5 == 0 :
	print("Angka yang anda masukkan adalah",angka)
	print("Pride of 5")
elif angka % 3 == 0 :
	print("Angka yang anda masukkan adalah",angka)
	print("Pride of 3")