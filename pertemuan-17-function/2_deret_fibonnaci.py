##  rumus fibonnaci (penjumlahan 2 angka sebelumnya)
# F^(n-1) + F^(n-2)

def Fibonnaci(angka):
    
    if angka <= 1: # ini base call, posisi default angka fibonnaci = 1
        return angka
    # Recursive Case
    else: # jika angka > 1, maka proses rekursif akan berjalan mengurangi 1 angka (-1) hingga angka sama dengan 1
        # pengurangan angka dimulai dari operasi function sebelah kiri, baru operasi kanan
        return Fibonnaci(angka - 1) + Fibonnaci(angka - 2)


# kita akan print angka deret fibonnaci ke 7

# deret fibonnaci = 1,1,2,3,5,8,13
print(Fibonnaci(7)) # 5 + 8 = 13
