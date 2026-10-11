# Mengimpor fungsi pengolahan data
from pengeluaran.processing import (
    tambah_pengeluaran,
    hitung_total,
    hitung_rata_rata,
    pengeluaran_terbesar,
    urutkan_pengeluaran,
    buat_laporan
)

# Mengimpor fungsi pengelolaan file
from pengeluaran.fileio import (
    buat_file,
    simpan_pengeluaran,
    baca_pengeluaran,
    simpan_laporan
)

# Nama file penyimpanan
NAMA_FILE = "data_pengeluaran.txt"
FILE_LAPORAN = "laporan_pengeluaran.txt"

# Menampilkan menu utama
def tampilkan_menu():
    print("\n=== PENGELUARAN HARIAN MAHASISWA ===")
    print("1. Tambah pengeluaran")
    print("2. Lihat semua pengeluaran")
    print("3. Lihat ringkasan pengeluaran")
    print("4. Urutkan pengeluaran")
    print("5. Simpan laporan")
    print("6. Keluar")

# Menambahkan data pengeluaran
def tambah_data():
    try:
        kategori = input("Kategori pengeluaran: ")
        jumlah = float(input("Jumlah pengeluaran: Rp"))
        keterangan = input("Keterangan: ")

        # Menambahkan data melalui fungsi
        data_baru = tambah_pengeluaran(
            kategori=kategori,
            jumlah=jumlah,
            keterangan=keterangan
        )

        # Menyimpan data ke file
        simpan_pengeluaran(NAMA_FILE, data_baru)
        print("Pengeluaran berhasil disimpan.")

    except ValueError as error:
        print("Input tidak valid:", error)

# Menampilkan seluruh data pengeluaran
def lihat_data():
    data = baca_pengeluaran(NAMA_FILE)

    if not data:
        print("Belum ada data pengeluaran.")
        return

    print("\n=== DAFTAR PENGELUARAN ===")

    for item in data:
        print(
            item["kategori"],
            "- Rp" + str(item["jumlah"]),
            "-", item["keterangan"]
        )

# Menampilkan ringkasan pengeluaran
def lihat_ringkasan():
    data = baca_pengeluaran(NAMA_FILE)

    if not data:
        print("Belum ada data pengeluaran.")
        return

    terbesar = pengeluaran_terbesar(data)

    print("Total pengeluaran: Rp", hitung_total(data))
    print("Rata-rata pengeluaran: Rp", hitung_rata_rata(data))
    print(
        "Pengeluaran terbesar:",
        terbesar["kategori"],
        "- Rp" + str(terbesar["jumlah"])
    )

# Mengurutkan data dari nominal terkecil
def urutkan_data():
    data = baca_pengeluaran(NAMA_FILE)

    if not data:
        print("Belum ada data pengeluaran.")
        return

    data_urut = urutkan_pengeluaran(data)

    print("\n=== PENGELUARAN DARI TERKECIL ===")

    for item in data_urut:
        print(item["kategori"], "- Rp" + str(item["jumlah"]))

# Membuat dan menyimpan laporan
def buat_laporan_file():
    data = baca_pengeluaran(NAMA_FILE)

    if not data:
        print("Belum ada data untuk dilaporkan.")
        return

    isi_laporan = buat_laporan(data)
    simpan_laporan(FILE_LAPORAN, isi_laporan)

    print("Laporan berhasil disimpan ke", FILE_LAPORAN)

# Fungsi utama program
def main():
    # Membuat file data jika belum tersedia
    buat_file(NAMA_FILE)

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            lihat_data()
        elif pilihan == "3":
            lihat_ringkasan()
        elif pilihan == "4":
            urutkan_data()
        elif pilihan == "5":
            buat_laporan_file()
        elif pilihan == "6":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

# Menjalankan program utama
if __name__ == "__main__":
    main()
