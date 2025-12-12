"""
Kelompok #1: Toko ATK Online ✓

    Kategori: Alat Tulis vs Perlengkapan Kantor

    Metode: Ambil sendiri vs Pakai kurir (+Rp 5.000)

    Diskon: 10% untuk pelanggan tetap
"""
## Step 1 : First Page and Category Select Menu
STORE_NAME = "ATK"


# Kategori barang
KATEGORI = {
    1:'Alat Tulis',
    2:'Perlengkapan kantor'
}

# list barang sesuai ketegori
list_barang = {
    # format = kategori -> kode barang -> nama barang, harga
    1: {
        101: {'nama_barang':"Buku Binder B5",
        'harga':25000},
        102: {'nama_barang':"Pulpen Gel Joyko (Pack)",
        'harga':15000},
        103 : {'nama_barang':"Sticky Note 3 Warna",
        'harga':18000},
    }, 
    
    2: {
        201:  {'nama_barang':"Stapler HD-10",
        'harga':12000},
        202: {'nama_barang':"Kalkulator 12 Digit",
        'harga':47000},
        203: {'nama_barang':"Kertas HVS A4 (1 Rim)",
        'harga':60000},
    }
}


# print(list_barang.items()) # debug kode

# first page and input number for category select 
SHOW_KATEGORI = f"""
{50*"="}

SElAMAT DATANG DI TOKO {STORE_NAME}

{50*"="}

KATEGORI:
1. {KATEGORI[1]}
2. {KATEGORI[2]}
\n
"""
print(SHOW_KATEGORI)
Category_Select = int(input("Pilih kategori [1,2] : "))





# 2. show list_barang sesuai category
if Category_Select in list_barang:
    print(f"""
{50*"="}
       Produk - {KATEGORI[Category_Select]}               
""")
    
    # ambil data dari list barang dengan key di set ke input
    barang_toko = list_barang[Category_Select]
    
    start_list_num = 1
    for kode, barang in barang_toko.items():
        rupiah_format = f"{barang['harga']:,}".replace(',','.') # mengganti format , menjadi .
        
        # template output
        print(f"{start_list_num}. {barang['nama_barang']} \t -> {rupiah_format}")
        start_list_num += 1

        # # kode barang (eksperimental)
        # print(kode)
    print(f"{50*"="}")
    
else:
    print(f"Input tidak sesuai pilihan di list!!")
    
### Pilih barang
select_barang = int(input("Pilih barang [1,2,3] = "))

# konversi kode barang menjadi list
list_kode = list(barang_toko.keys()) 
# sama seperti :
# [1]['nama_barang']
# [2]['harga']


# menyesuaikan input client ke index
# user access = 1
# list access = 0
client_number = select_barang - 1 # 

if 0 <= client_number < len(list_kode):
    # real_kode_barang : memanggil kode barang yang sudah dijadikan array
    # item_fix : 
    real_kode_barang = list_kode[client_number] # minta kode dulu dari sini
    item_fix = barang_toko[real_kode_barang] # baru ambil barang
    
    fix_price = f"{item_fix['harga']:,}".replace(',','.') 
    
    print(f"\nBerhasil Memilih : {item_fix['nama_barang']}")
    
    print(f"Harga :  Rp. {fix_price}") # harga satuan barang

    # jumlah barang
    quantity = int(input("Jumlah Barang = "))
    
    # total
    subtotal = quantity * item_fix['harga']
    print(f"Subtotal = Rp. {subtotal:,}".replace(',','.'))


## 2.2 OPERASI HARGA
# total = item_fix['harga']
# print(f'harga barang dummy = {total}')




# 3. Pengambilan barang 
Pengambilan = {
    1: {'via':'datang toko', 'biaya':0},
    2: {'via':'Kurir', 'biaya':5000}
}

Display_pengambilan = f"""
{50*"="}
Pengambilan Barang

1. {Pengambilan[1]['via']}\t => Rp.{Pengambilan[1]['biaya']:,}
2. {Pengambilan[2]['via']}\t => Rp.{Pengambilan[2]['biaya']:,}

{50*"="}
"""
print(Display_pengambilan)


select_pengiriman = int(input("Mau diambil dengan [1/2] = "))

biaya_pengiriman = 0

if select_pengiriman == 1:
    biaya_pengiriman = Pengambilan[1]['biaya']
    print(f"Biaya pengiriman = {biaya_pengiriman}")
elif select_pengiriman == 2:
    biaya_pengiriman = Pengambilan[2]['biaya']
    print(f"Biaya pengiriman = {biaya_pengiriman}")

    
Discount_member = 0
    
is_member = str(input("\nApakah anda Pelanggan tetap (y/n) = "))

Discount = 10 / 100
if is_member.lower() == 'y':
    print(f"Selamat kamu mendapat diskon 10%")
    Discount_member = subtotal * Discount
    
    # kurang_harga = subtotal - Discount_member
    # print(int(kurang_harga))

print()    
# 4. Struk Belanja (Detail Pembelian)


detail_pembelian = f"""
{50*"="}
    Detail Pembelian
{50*"="}

Item                    : {item_fix['nama_barang']} x {quantity}
Subtotal                : Rp. {subtotal:,}
Biaya Tambahan          : Rp. {biaya_pengiriman:,}
Diskon Pelanggan (10%)  : Rp. {Discount_member:,}

{50*"-"}

Total Bayar : {(subtotal + biaya_pengiriman) - Discount_member}
"""

print(detail_pembelian)


# if select_barang in Pengambilan[select_pengiriman]:
    


