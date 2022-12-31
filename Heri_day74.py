print("=== PROGRAM MEMERIKSA BILANGAN PRIMA ===")
print("========================================")
print()

a=int(input("Masukkan Bilangan :"))     
if a>1:
    for x in range(2,a):
        if(a%x)==0:
            print(a,"-> Bukan bilangan Prima")
            break
    else:
        print(a,"-> Bilangan Prima")
else:
    print(a,"-> Bukan bilangan prima")