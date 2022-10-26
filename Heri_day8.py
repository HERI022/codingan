print ("=====", "UKURAN BAJU", "=====")

# Berat badan < 35 kg cocok menggunakan ukuran baju S
# Berat badan >= 35 sampai <= 44 kg cocok menggunakan ukuran baju M
# Berat badan >= 45 sampai <= 54 kg cocok menggunakan ukuran baju L
# Berat badan >= 55 sampai <= 64 kg cocok menggunakan ukuran baju XL
# Berat badan >= 65 sampai <= 75 kg cocok menggunakan ukuran baju XXL

berat = int(input("Masukkan berat badan anda :"))

if berat < 35 :
    print("Anda cocok menggunakan baju yang berukuran S")
    print("Silahkan pilih baju yang berukuran S")

elif berat >= 35 and berat <= 44 :
    print("Anda cocok menggunakan baju yang berukuran M")
    print("Silahkan pilih baju yang berukuran M")

elif berat >= 45 and berat <= 54 :
    print("Anda cocok menggunakan baju yang berukuran L")
    print("Silahkan pilih baju yang berukuran L")

elif berat >= 55 and berat <= 64 :
    print("Anda cocok menggunakan baju yang berukuran XL")
    print("Silahkan pilih baju yang berukuran XL")

elif berat >= 65 and berat <= 75 :
    print("Anda cocok menggunakan baju yang berukuran XXL")
    print("Silahkan pilih baju yang berukuran XXL")

else :
    print("Maaf, ukuran baju untuk berat badan diatas 75 kg tidak tersedia")
    
