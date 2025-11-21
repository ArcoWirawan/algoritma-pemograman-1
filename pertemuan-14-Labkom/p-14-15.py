# 1. Input angka < 10

while True:
    num = int(input("Angka > 10 : "))
    if num > 10:
        break
    
# 2. Login password 
passwd = "admin"
while True:
    if input("Password = ") == passwd:
        print("Login Successfull")
        break

# 3. Konfigurasi ulang input
while True:
    data = input("Your Name = ")
    ulang = str(input("Again?? [y/n] = "))
    if ulang == "n":
        break
    elif ulang != "y":
        print("Salah Input!!")
        break
    else:
        print()
        
# 4. Menjumlahkan input sampai user berhenti
total = 0
while True:
    total += int(input("Input Number here = "))
    
    # input dijadiin huruf kecil dan harus input 'n'
    if str(input("Nambah kaga [y/n] = ")).lower() == 'n':
        break
print("Total = ", total)



## Nested Loop ##

# 1. Bintang segitiga
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()