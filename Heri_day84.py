from tkinter import *
 
modul = Tk()
modul.title("Kalkulator GUI Dengan Tkinter di Python")
modul.geometry('350x200')
 
angka1 = Label(modul, text="Masukan Nilai Pertama : ",anchor="e",width=20)
angka1.grid(column=0, row=0)
 
nilai1 = Entry(modul,width=10)
nilai1.grid(column=1,row=0)
 
 
angka2 = Label(modul, text="Masukan Nilai Kedua : ",anchor="e",width=20)
angka2.grid(column=0, row=1)
 
nilai2 = Entry(modul,width=10)
nilai2.grid(column=1,row=1)
 
total = Label(modul, text="Hasil : ",anchor="e",width=20)
total.grid(column=0, row=2)
 
hasil = Label(modul, text="0",anchor="w",width=10)
hasil.grid(column=1, row=2)
 
def tambah():
    hasil.configure(text=(int(nilai1.get())+int(nilai2.get())))
 
def kurang():
    hasil.configure(text=(int(nilai1.get())-int(nilai2.get())))
 
def kali():
    hasil.configure(text=(int(nilai1.get())*int(nilai2.get())))
 
def bagi():
    hasil.configure(text=(int(nilai1.get())/int(nilai2.get())))
 
 
btn = Button(modul, text="Tambah", command=tambah)
btn.grid(column=0, row=3)
 
btn = Button(modul, text="Kurang", command=kurang)
btn.grid(column=1, row=4)
 
btn = Button(modul, text="Kali", command=kali)
btn.grid(column=0, row=4)
 
btn = Button(modul, text="Bagi", command=bagi)
btn.grid(column=1, row=4)
 
 
modul.mainloop()