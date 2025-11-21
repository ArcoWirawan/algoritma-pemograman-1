# 1. create array and display output

grade = [80, 77, 89]
print(grade)

# 2. Tambah elemen array
data =[]
for x in range(1, 6):
    data.append(x)
print(data)

# 3. Akses element berdasarkan indeks
print("Elemen index 0 = ", data[0])

# change data on array
data[1] = 29

# remove data
data.remove(29)