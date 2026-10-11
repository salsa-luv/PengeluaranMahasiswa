# Mengimpor fungsi validasi
from pengeluaran.validasi import validasi_pengeluaran

# Menyimpan data pengeluaran ke dalam list
data_pengeluaran = []

# Menambahkan data pengeluaran
def tambah_pengeluaran(*args, **kwargs):
    if args:
        kategori = args[0]
        jumlah = args[1]
        keterangan = args[2] if len(args) > 2 else ""
    else:
        kategori = kwargs.get("kategori", "")
        jumlah = kwargs.get("jumlah", 0)
        keterangan = kwargs.get("keterangan", "")

    # Memeriksa data sebelum disimpan
    validasi_pengeluaran(kategori, jumlah)

    # Membuat dictionary untuk satu data pengeluaran
    data_baru = {
        "kategori": kategori,
        "jumlah": jumlah,
        "keterangan": keterangan
    }

    # Menambahkan data ke dalam list
    data_pengeluaran.append(data_baru)

    return data_baru

# Menghitung total pengeluaran
def hitung_total(data):
    return sum(item["jumlah"] for item in data)

# Menghitung rata-rata pengeluaran
def hitung_rata_rata(data):
    if not data:
        return 0

    return hitung_total(data) / len(data)

# Mencari pengeluaran terbesar
def pengeluaran_terbesar(data):
    if not data:
        return None

    return max(data, key=lambda item: item["jumlah"])

# Mengurutkan pengeluaran dari nominal terkecil
def urutkan_pengeluaran(data):
    return sorted(data, key=lambda item: item["jumlah"])

# Membuat laporan pengeluaran
def buat_laporan(data):
    laporan = "LAPORAN PENGELUARAN MAHASISWA\n"

    for item in data:
        laporan += (
            item["kategori"] + " : Rp"
            + str(item["jumlah"])
            + " - " + item["keterangan"] + "\n"
        )

    laporan += "Total: Rp" + str(hitung_total(data)) + "\n"
    laporan += "Rata-rata: Rp" + str(hitung_rata_rata(data)) + "\n"

    return laporan
