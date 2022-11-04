#Penggunaan pass, continue, dan break pada perulangan while.

print("\n",5*"=","pass, continue, dan break","="*5)
print(38*"-")

#pass
#tidak akan dieksekusi

angka = 0

while angka < 10 :
    angka += 1
    
    if angka == 3 :
        pass #tidak ada pengaruhnya

    print(angka)

#Continue

angka = 0

print("\n","angka saat ini adalah =",angka,"\n")

while angka < 10 :
    angka += 1

    print("angka sekarang adalah :",angka)

    if angka == 5 :
        print("Sangat bagus sekali")
        continue #print yang berada di bawah continue akan di lewati.

    print("Berhasil")
        
print("Selesai \n")


#break
#break adalah kebalikan dari continue

angka = 0

while angka < 10 :
    angka += 1
    print("angka sekarang adalah :",angka)


    if angka == 5 :
        print("Angka 5 telah ditemukan")
        break # akan berhenti ketika kondisi if terpenuhi

    print("Pekerjaan yang bagus")

print("finish/selesai")


        


    
