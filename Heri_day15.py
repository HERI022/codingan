print ("=====", "Pembuatan SIM", "=====")




usia = int(input("masukan usia anda :"))


if usia <= 16 :
    print("Maaf, usia anda belum mencukupi untuk pengurusan SIM")
    print("Silahkan kembali lagi jika usia anda sudah >= 17 tahun")

else :
    nilai = int(input("masukkan nilai tes anda: "))
    lulus = "SELAMAT, anda berhak mendapatkan SIM"
    gagal = "MAAF, anda tidak berhak mendapatkan SIM"

    if nilai >= 80 :
        print(lulus)

    else :
        print(gagal)





