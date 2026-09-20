def hitung_total_berat(daftar_berat):
    return sum(daftar_berat)


# Data hasil panen
daftar_berat = [10, 15, 20, 12, 18]

# Perhitungan
total_berat = hitung_total_berat(daftar_berat)

# Menampilkan hasil
print("Daftar berat:", daftar_berat, "kg")
print("Total hasil panen:", total_berat, "kg")