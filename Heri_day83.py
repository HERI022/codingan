#STACK
import os
class Stack:
    def __init__(isi):
        isi.files = []
       
    def kosong(isi):
        return isi.files == []
    
    def masuk(isi, item):
        isi.files.append(item)
    
    def pop(isi):
        return isi.files.pop()
    
    def peek(isi):
        return isi.files[len(isi.files)-1]
    
    def ukuran(isi):
        return len(isi.files)
   
    
    def mainmenu(isi):
        pilih = "y"
        while (pilih == "y"):
            os.system("clear")
            print("===============================")
            print("    Menu objek stack   ")
            print("===============================")
            print("1. Masukan objek stack")
            print("2. Keluarkan objek stack")
            print("3. Memeriksa Stack")
            print("4. Tampil objek terakhir stack")
            print("5. Panjang dari stack")
            print("6. Keluar")
            print("===============================")
            pilihan=str(input(("Silakan masukan pilihan anda: ")))
            if(pilihan=="1"):
                os.system("clear")
                objek = str(input("Masukan objek yang ingin anda tambahkan : "))
                isi.masuk(objek)
                print("Object ",objek," telah ditambahkan")
                print("Enter untuk lanjut :")
                x = input("")
            elif(pilihan=="2"):
                os.system("clear")
                print("Objek ",isi.pop()," dihapus")
                x = input("")
                print("Enter untuk lanjut :")
            elif(pilihan=="3"):
                os.system("clear")
                print(isi.kosong())
                x = input("")
                print("Enter untuk lanjut :")
            elif(pilihan=="4"):
                os.system("clear")
                print("Objek terakhir: ",isi.peek())
                print("Enter untuk lanjut :")
                x = input("")
            elif(pilihan=="5"):
                os.system("clear")
                print("Panjang dari stack adalah: ",str(isi.ukuran()))
                x = input("")
                print("Enter untuk lanjut :")
            else:
                pilih="n"  
 
if __name__ == "__main__":
    s=Stack()
    s.mainmenu()