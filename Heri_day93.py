# program sederhana menampilkan struk 

daftar_item = [] 

def tambah_item (nama , harga):
    daftar_item.append({'nama' : nama , 'harga': harga}) 

def hitung_total():
    total = 0 
    for item in daftar_item:
        total +=item['harga'] 
    return total 

def tampilan_struk():
    for item in daftar_item:
        print(item['nama'],'\t',item['harga'])
        print('Total \t\t',hitung_total()) 

while True:
    
    nama = input("Masukkan nama item : ") 
    if nama == 'selesai':
        break 
    harga = int(input("Masukkan harga item : "))
    print("Warning! :ketik selesai untuk menampilkan struk")
    
    tambah_item(nama , harga) 

tampilan_struk() 