import queue

class myQueue:
    def __init__(self):
        self.items = queue.Queue()

    def isEmpety(self):
        return self.items.empty()

    def gAdd (self, item):
        self.items.put(item)

    def gOut (self):
        if not self.items.empty():
            return self.items.get()

        else:
            return ("Data Antrian Kosong")

    def size(self):
        return self.items.qsize()

    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            print("=======================")
            print("Antrian Warna")
            print("=======================")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. View Queue")
            print("4. Long Queue")
            print("5. Keluar")
            print("=======================")

            pilihan = input("Silahkan masukan pilihan anda :")
            if (pilihan == "1"):
                warna = input("Masukkan warna yang anda inginkan :")
                self.qAdd(warna)
                print("warna",warna,"telah masuk antrian")
                x = input("")
            elif (pilihan == "2"):
                temp = self.qOut()
                if temp != "Data Antrian Kosong":
                    print("warna",warna,"Keluar Antrian")
                else:
                    print("Antrian Kosong")
                x = input("")
            elif (pilihan == "3"):
                print(self.isEmpty())
                x = input("")
            elif (pilihan == "4"):
                print("Panjang Dari Queue adalah: ",str(self.size()))
                x = input("")
            elif (pilihan == "5"):
                print("Terimakasih Atas Tugas yang diberikan oleh bang fyan")
                print("silahkan tekan enter untuk keluar dari program ini")
                print("Sampai jumpa kembali")
                print(quit())
            else:
                pilih="n"

if __name__ == "_main_":
    q = myQueue()
    q.mainmenu()
    
