"""
Studi Kasus 2: Diskon Toko Online

    Jika total belanja lebih dari Rp500.000 → diskon 10%
    Jika total belanja Rp500.000 atau kurang → tidak ada diskon
    Buat program untuk menghitung total bayar setelah diskon.
"""

Total = int(input("Total belanja : "))

if Total > 500000:
    # Proses perhitungan :
    # 1. Besar Diskon, Cari harga diskon yang didapat
    # 2. Harga Setelah Diskon, Kurangi harga asli dengan harga diskon
    Discount = Total * (10/100) # 10% => 10 / 100
    DiscountPrice = Total - Discount

    print(f"Total Belanjamu adalah Rp.{Total:,}")
    print(f"Diskon 10% menjadi Rp.{DiscountPrice:,}")
else:
    print(f"Total belanjamu Rp.{Total:,}")