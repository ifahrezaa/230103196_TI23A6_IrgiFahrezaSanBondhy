def jadwal_hari(hari):
    """Menampilkan jadwal kuliah berdasarkan hari tertentu."""
    jadwal = [
        {"hari": "Senin", "mata_kuliah": "Algoritma & Pemrograman"},
        {"hari": "Selasa", "mata_kuliah": "Struktur Data"},
        {"hari": "Rabu", "mata_kuliah": "Basis Data"},
        {"hari": "Kamis", "mata_kuliah": "Pemrograman Web"},
        {"hari": "Jumat", "mata_kuliah": "Kecerdasan Buatan"}
    ]

    for item in jadwal:
        if item["hari"].lower() == hari.lower():
            return f"Jadwal hari {hari}: {item['mata_kuliah']}"
    return "Hari tidak ditemukan."


# Contoh pemanggilan fungsi
print(jadwal_hari("Rabu"))
print(jadwal_hari("Minggu"))
