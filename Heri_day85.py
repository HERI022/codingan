import tkinter as tk

objek = tk.Tk()
objek.title('Form Data Mahasiswa')
objek.geometry('500x200')

tabel1 = tk.Frame(master=objek)
tabel1['relief'] = tk.GROOVE
tabel1['borderwidth'] = 1
tabel1.pack(side=tk.LEFT, fill=tk.Y)

tabel2 = tk.Frame(master=objek)
tabel2['relief'] = tk.RIDGE
tabel2.pack(side=tk.RIGHT)

list = {
    0: 'Nama Lengkap',
    1: 'NIM   ',
    2: 'Tanggal Lahir',
    3: 'Program Studi',
    4: 'Jurusan  '
    }
i = 4
for i in list:
    label = tk.Label(master=tabel1)
    label['text'] = list[i], ':'
    label.grid(row=i, column=0, sticky=tk.W)

    masuk = tk.Entry(master=tabel2)
    masuk['width'] = 50
    masuk.grid(row=i, column=1, sticky=tk.W)
    i = i+1

    la = tk.Label(master=tabel1)
    la['text'] = '{Jenis Kelamin} :'
    la.grid(row=10, column=0, sticky=tk.W)
    va = tk.IntVar()
    ra1 = tk.Radiobutton(master=tabel2, text='Pria', variable=va, value=1)
    ra1.grid(row=10, column=0, sticky=tk.W)

    ra2 = tk.Radiobutton(master=tabel2, text='Wanita', variable=va, value=2)
    ra2.grid(row=10, column=1, sticky=tk.W)

tombol1 = tk.Button(master=tabel2)
tombol1['text'] = 'Selesai'
tombol1.grid(row=11, column=0, sticky=tk.W)

tombol2 = tk.Button(master=tabel2)
tombol2['text'] = 'Batal'
tombol2.grid(row=11, column=1, sticky=tk.W)

objek.mainloop()
