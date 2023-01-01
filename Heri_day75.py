print("=== Program Membuat Resi Pengiriman Barang ===")
print()
nama_pengirim = input("Masukkan nama Pengirim :")
nama_penerima = input("masukkan nama penerima :")
alamat_pengirim = input("Masukkan alamat pengiriman :")
alamat_penerima = input("Masukkan alamat penerima :")
berat_barang = float(input("Masukkan berat barang (kg) :"))
ongkos_kirim = 8000  # per kilogram

# Hitung total ongkos kirim
total_ongkos_kirim = ongkos_kirim * berat_barang

# Cetak detail pengiriman
print("\n")
print("===============================")
print("Detail Pengiriman Barang")
print("===============================")
print()
print("Nama Pengirim\t: " + nama_pengirim)
print("Nama Penerima\t: " + nama_penerima)
print("Alamat Pengirim\t: " + alamat_pengirim)
print("Alamat Penerima\t: " + alamat_penerima)
print("Berat Barang\t: " + str(berat_barang) + " kg")
print("Ongkos Kirim\t: Rp. " + str(ongkos_kirim) + " per kg")
print("Total Ongkos Kirim: Rp. " + str(total_ongkos_kirim))
print()
print("===============================")