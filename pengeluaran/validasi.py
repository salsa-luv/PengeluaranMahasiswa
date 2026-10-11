# Fungsi untuk memvalidasi data pengeluaran
def validasi_pengeluaran(kategori, jumlah):
    # Kategori tidak boleh kosong
    if not kategori.strip():
        raise ValueError("Kategori tidak boleh kosong.")

    # Jumlah pengeluaran harus lebih dari nol
    if jumlah <= 0:
        raise ValueError("Jumlah pengeluaran harus lebih dari 0.")

    # Jika semua pemeriksaan lolos, data dinyatakan valid
    return True
