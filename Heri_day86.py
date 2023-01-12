from tkinter import*
import sqlite3

def login():
   
    uname=username.get()
    pwd=password.get()
    
    if uname=='' or pwd=='':
        message.set("Mengisi Kolom Kosong")
    else:
     
      conn = sqlite3.connect('Mahasiswa')
      
      cursor = conn.execute('PILIH * from ADMIN where USERNAME="%s" and PASSWORD="%s"'%(uname,pwd))
      
      if cursor.fetchone():
       message.set("Login Berhasil")
      else:
       message.set("Username atau Password salah!!!")

def Loginform():
    global login_screen
    login_screen = Tk()
    
    login_screen.title("Syaputrahery581@gmail.com")
    
    login_screen.geometry("350x250")
    login_screen["bg"]="#1C2833"
    
    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    
    Label(login_screen,width="300", text="Login From", bg="#0E6655",fg="white",font=("Arial",12,"bold")).pack()
   
    Label(login_screen, text="Username * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=10,y=150)
    
    Entry(login_screen, textvariable=username,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=330,y=160)
    
    Label(login_screen, text="Password * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=10,y=250)
    
    Entry(login_screen, textvariable=password ,show="*",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=330,y=260)
    
    Label(login_screen, text="",textvariable=message,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=50,y=520)
    
    Button(login_screen, text="Login", width=10, height=1, command=login, bg="#0E6655",fg="white",font=("Arial",12,"bold")).place(x=330,y=370)
    login_screen.mainloop()
    
Loginform()