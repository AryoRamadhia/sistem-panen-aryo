def hitung_total_berat(daftar_berat):
    return sum(daftar_berat)


# Data hasil panen
daftar_berat = [10, 15, 20, 12, 18]

# Perhitungan
total_berat = hitung_total_berat(daftar_berat)

# Menampilkan hasil
print("Daftar berat:", daftar_berat, "kg")
print("Total hasil panen:", total_berat, "kg")
def hitung_total_berat(daftar_berat):
    return sum(daftar_berat)


def hitung_diskon(total_harga, persen_diskon):
    if persen_diskon > 0:
        diskon = total_harga * persen_diskon / 100
        return diskon
    else:
        return 0


# Data hasil panen
daftar_berat = [10, 15, 20, 12, 18]
harga_per_kg = 12000
persen_diskon = 10

# Menghitung hasil panen
total_berat = hitung_total_berat(daftar_berat)

# Menghitung harga
total_harga = total_berat * harga_per_kg
diskon = hitung_diskon(total_harga, persen_diskon)
harga_akhir = total_harga - diskon

# Menampilkan hasil
print("Total hasil panen:", total_berat, "kg")
print("Total harga: Rp", total_harga)
print("Diskon:", persen_diskon, "%")
print("Potongan harga: Rp", diskon)
print("Harga akhir: Rp", harga_akhir)
