## list 1 dimensi (single list)

# data yang saya miliki
data = [10, 20, 30, 40 ,50 ]
print(dir(data)) # pengecekan fungsi yang dapat digunakan

print()
print(f"Data = {data}")
print()

# Akses Data dengan index
# 
#[10, 20, 30, 40, 50] # list
#[0,  1,   2,  3,  4] # index

print(data[1]) # 20
print()
# input data
# inputData = int(input("Inputkan data untuk list = "))

# fungsi untuk menambahkan data -> var.append(masukan data bebas)
data.append("arwanz") # data ditambahkan dahulu
print(f"Data ditambahkan = {data}") # cek apakah data telah ditambahkan

# fungsi menghapus data -> var.remove(data yang ingin dihapus)
data.remove(10) # data akan dihapus dahulu
print(f"Data dikurangkan = {data}") # cek apakah data sudah terhapus


