# Mengimpor fungsi yang akan diuji
from pengeluaran.processing import (
    tambah_pengeluaran,
    hitung_total,
    hitung_rata_rata,
    pengeluaran_terbesar,
    urutkan_pengeluaran
)

from pengeluaran.validasi import validasi_pengeluaran

# Menguji penambahan data pengeluaran
def test_tambah_pengeluaran():
    data = tambah_pengeluaran(
        kategori="Makan",
        jumlah=15000,
        keterangan="Makan siang"
    )

    assert data["kategori"] == "Makan"
    assert data["jumlah"] == 15000
    print("Test tambah pengeluaran berhasil.")

# Menguji perhitungan total
def test_hitung_total():
    data = [
        {"kategori": "Makan", "jumlah": 15000, "keterangan": "Siang"},
        {"kategori": "Transportasi", "jumlah": 10000, "keterangan": "Ongkos"}
    ]

    assert hitung_total(data) == 25000
    print("Test hitung total berhasil.")

# Menguji perhitungan rata-rata
def test_hitung_rata_rata():
    data = [
        {"kategori": "Makan", "jumlah": 15000, "keterangan": "Siang"},
        {"kategori": "Transportasi", "jumlah": 10000, "keterangan": "Ongkos"}
    ]

    assert hitung_rata_rata(data) == 12500
    print("Test hitung rata-rata berhasil.")

# Menguji pencarian pengeluaran terbesar
def test_pengeluaran_terbesar():
    data = [
        {"kategori": "Makan", "jumlah": 15000, "keterangan": "Siang"},
        {"kategori": "Transportasi", "jumlah": 10000, "keterangan": "Ongkos"}
    ]

    terbesar = pengeluaran_terbesar(data)

    assert terbesar["jumlah"] == 15000
    print("Test pengeluaran terbesar berhasil.")

# Menguji validasi data
def test_validasi_pengeluaran():
    try:
        validasi_pengeluaran("Makan", 0)
        assert False, "Seharusnya menghasilkan ValueError."
    except ValueError:
        print("Test validasi pengeluaran berhasil.")

# Menjalankan seluruh pengujian
if __name__ == "__main__":
    test_tambah_pengeluaran()
    test_hitung_total()
    test_hitung_rata_rata()
    test_pengeluaran_terbesar()
    test_validasi_pengeluaran()

    print("\nSemua pengujian selesai.")
