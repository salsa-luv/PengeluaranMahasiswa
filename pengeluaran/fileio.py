# Mengimpor fungsi dari processing.py
from pengeluaran.processing import tambah_pengeluaran

# Membuat file baru jika belum ada
def buat_file(nama_file):
    try:
        with open(nama_file, "x") as file:
            file.write("")
        return True
    except FileExistsError:
        return False

# Menyimpan satu pengeluaran ke file
def simpan_pengeluaran(nama_file, pengeluaran):
    with open(nama_file, "a") as file:
        file.write(
            pengeluaran["kategori"] + "|"
            + str(pengeluaran["jumlah"]) + "|"
            + pengeluaran["keterangan"] + "\n"
        )

# Membaca data pengeluaran dari file
def baca_pengeluaran(nama_file):
    data_pengeluaran = []

    try:
        with open(nama_file, "r") as file:
            for baris in file:
                data = baris.strip().split("|")

                if len(data) == 3:
                    data_pengeluaran.append({
                        "kategori": data[0],
                        "jumlah": float(data[1]),
                        "keterangan": data[2]
                    })

    except FileNotFoundError:
        print("File data belum tersedia.")

    return data_pengeluaran

# Menyimpan laporan ke file
def simpan_laporan(nama_file, isi_laporan):
    with open(nama_file, "w") as file:
        file.write(isi_laporan)
