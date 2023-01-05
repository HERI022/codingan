print("----------------- Program Kasir Sederhana -----------------")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n----------------- Menu Makanan -----------------")
   print("1. Nasi Goreng\t- Rp 15.000")
   print("2. Soto\t\t- Rp 9.000")
   print("3. Mie Ayam\t- Rp 11.000")
   print("4. Bakso\t- Rp 13.000")
   print("5. Gado-gado\t- Rp 10.000")
   nomor=int(input("Masukan Pilihan: "))
   
   if nomor==1:
       porsi= int(input("Berapa Porsi: "))
       totalmkn=porsi*15000
       print (porsi," porsi Nasi Goreng Telur = Rp", totalmkn)
       mkn=("Nasi Goreng")
   elif nomor==2:
       porsi= int(input("Berapa Porsi: "))
       totalmkn=porsi*9000
       print (porsi," porsi Soto = Rp", totalmkn)
       mkn=("Soto")
   elif nomor==3:
       porsi= int(input("Berapa Porsi: "))
       totalmkn=porsi*11000
       print (porsi, " porsi Mie Ayam = Rp", totalmkn)
       mkn=("Mie Ayam")
   elif nomor==4:
       porsi= int(input("Berapa Porsi: "))
       totalmkn=porsi*13000
       print (porsi, " porsi Bakso = Rp", totalmkn)
       mkn=("Bakso")
   elif nomor==5:
       porsi= int(input("Berapa Porsi: "))
       totalmkn=porsi*10000
       print (porsi, " porsi Gado-gado = Rp", totalmkn)
       mkn=("Gado-gado")
   else:
      print("Pilihan anda tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Es teh\t- Rp 2000")
   print("2. Es jeruk\t- Rp 3500")
   print("3. Es kopi\t- Rp 4000")
   print("4. Kopi susu\t- Rp 5000")
   print("5. Susu\t\t- Rp 3000")
   nomor=int(input("Masukan Pilihan: "))

   if nomor==1:
       gelas= int(input("Berapa Gelas: "))
       totalmnm=gelas*2000
       print (gelas," Es Teh = Rp", totalmnm)
       mnm=(" Gelas Es Teh")
   elif nomor==2:
       gelas= int(input("Berapa Gelas: "))
       totalmnm=gelas*3500
       print (gelas, " Gelas Es Jeruk = Rp", totalmnm)
       mnm=("Es Jeruk")
   elif nomor==3:
       gelas= int(input("Berapa Gelas: "))
       totalmnm=gelas*4000
       print (gelas, " Gelas Es Kopi = Rp", totalmnm)
       mnm=("Es Kopi")
   elif nomor==4:
       gelas= int(input("Berapa Gelas: "))
       totalmnm=gelas*5000
       print (gelas, " Gelas Kopi susu = Rp", totalmnm)
       mnm=("Kopi susu")
   elif nomor==5:
       gelas= int(input("Berapa Gelas: "))
       totalmnm=gelas*3000
       print (gelas, " Gelas Susu = Rp", totalmnm)
       mnm=("Susu")
   else:
      print("Pilihan anda tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== S T R U K   B E L I =========")
print("==================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("==================================")
