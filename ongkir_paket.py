def hitung_ongkir(berat_kg, kota, asuransi=False):
    """Menghitung biaya ongkir berdasarkan kota, berat, dan opsi asuransi."""
    tarif_dasar = {
        "Jakarta": 10000,
        "Bandung": 12000,
        "Surabaya": 15000
    }

    ongkir = tarif_dasar.get(kota, 0) + 2000 * berat_kg
    if asuransi:
        ongkir += 3000
    return ongkir


# 🔹 Contoh pemanggilan fungsi
print(hitung_ongkir(3, "Jakarta"))              # Tanpa asuransi
print(hitung_ongkir(2, "Surabaya", True))       # Dengan asuransi
