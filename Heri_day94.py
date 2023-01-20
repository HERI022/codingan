# belajar args dan kwargs
print("Contoh Sederhana Args dan Kwargs")
# args
print("=======*Args=======")

def nama(*args): # untuk kata argsnya boleh kata lain, tidak mslh 
    n = 0
    for i in args:
        n += 1
        print(str(n)+". "+ i)
nama("Heri","Fyan","Andre","Ikhsan","Aqmal","dll")


print()
print("========**Kwargs========")
# kwargs
def name(**kwargs):
    for k,v in kwargs.items():
        print(k, ":", v)

name(Ikhsan = 90, Aqmal = 80, Fyan = 70, Andre = 60, sampai = "sebanyak banyaknya\n")



print("+++++++++++++++++++++++++++++++++++")
# tambahan
# bisa di tambah lagi, dengan cara memanggil funsinya, and masukkan velue
nama("Ikhsan","Fyan","Andre","Aqmal", "dll", "tambah lagi\n")
print("+++++++++++++++++++++++++++++++++++")
name(Ikhsan = 90, Aqmal = 80, Fyan = 70, Andre = 60, sampai = "sebanyak banyaknya", tambah = "lagi")

