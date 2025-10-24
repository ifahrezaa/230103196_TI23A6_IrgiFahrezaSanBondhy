import os
import csv
import json
import logging

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

try:
    # 1) Membuat folder data
    os.makedirs("data", exist_ok=True)
    logging.info("Mulai proses rekap kehadiran...")

    # 2) Menulis file CSV
    with open("data/presensi.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["nim", "nama", "hadir_uts"])
        writer.writerow(["23001", "Budi", 1])
        writer.writerow(["23002", "Siti", 0])
        writer.writerow(["23003", "Andi", 1])

    # 3) Membaca kembali CSV dan hitung ringkasan
    total = hadir = 0
    with open("data/presensi.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += 1
            if int(row["hadir_uts"]) == 1:
                hadir += 1

    persentase = (hadir / total) * 100 if total > 0 else 0

    ringkasan = {
        "total_mahasiswa": total,
        "hadir": hadir,
        "persentase_hadir": f"{persentase:.2f}%"
    }

    # Simpan ke JSON
    with open("data/ringkasan.json", "w") as f:
        json.dump(ringkasan, f, indent=4)

    logging.info("Proses selesai dan file JSON berhasil disimpan.")

except Exception as e:
    logging.error(f"Gagal memproses data: {e}")
