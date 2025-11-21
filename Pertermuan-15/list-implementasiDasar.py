## Pembuatan Kelompok siswa

try: # akan mencoba menjalankan kode
    while True: # selama kode tidak salah, akan terus berlanjut
        
        # Variabel yang dibutuhkan
        namaKel = str(input("Nama Kelompok = ")) # beri nama kelompok
        kelompok  = []  # variabel untuk menampung nama anggota
        maxMember = 5 # maximal orang dalam kelompok

        # Proses Input data
        for kel in range(maxMember): # akan berulang selama 5x
            inputMhs = str(input("Nama Mahasiswa : ")) # input nama Mahasiswa
            kelompok.append(inputMhs) # data ditambahkan ke list kelompok, dari inputMhs


        print()
        print(f"Kelompok {namaKel} = {kelompok}") # hasil
        
# jika ada kesalahan, lapor ke except       
except KeyboardInterrupt: # Jika tekan CTRL + C
    print("\n")
    print("Keluar")
    