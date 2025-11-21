## While loop 

# angka 1 -
x = 1
while x <= 10:
    print(f"Number = {x}")
    x += 1

print()

# menampilkan bilangan genap
x = 2
while x <= 20:
    # if x % 2 == 0:
    print(f"Number genap = {x}")
    x += 2
print()


# 3. Menampilkan bialgan ganjil kurang dari 10
x = 1
while x < 10:
    print(x)
    x += 2
print()

# 4. Menjumlahkan bilangan dari 1-5
i = 1 # 
total = 0
while i <= 5: 
    total += i # 0 + 1 = 1
    # total = 1
    i += 1
    # i = 2
    
    # repeat 2 -> 1 + 2 = 3
print(f"total = {total}")
print()


# 5. Input Berulangan Hingga nilai = 0
angka = int(input("Masukkan angka (0 untuk berhenti): "))
while angka != 0:
    print(f"Kamu Input Angka {angka}")
    angka = int(input("Masukkan angka (0 untuk berhenti): "))
print("End Program")
print()

# 6. Menghitung Faktorial1

n = int(input("Masukkan angka = ")) # angka yang ingin diinputkan
hasil = 1 # 
i = 1
while i <= n: # input kurang dari sama dengan angka input
    hasil *= i # angka 1 * 1
    i += 1 # angka i bertambah 1
           # Repeat
    # hasil * i -> 1 * 2 = 2
    #           -> 2 * 3 = 6
print(f"Faktorial dari {n} adalah {hasil}")


# 7. Validasi password
passwd = ""
while passwd != "47W4NZX9": # selagi password tidak sama dengan berikut
    passwd = input("Input Password = ") # ulangi terus input passoword
print("Access Success")
print()

# 8. Menampilkan Deret Fibonacci
a, b = 0, 1 # 2 variabel dan value dipisahkan dengan koma
count = 0
while count < 10: # selama count kurang dari 10
    print(a) # cetak angka a
    a, b = b, a + b
    count += 1
print()


# 9. Menghitung Banyak Data Input
jumlah = 0
while True:
    data = input("Masukkan data (ketik 'stop' untuk berhenti) : ")
    if data == "stop":
        break
    jumlah += 1
print(f"Total yang dimasukkan = {jumlah}")
print()

# 10. Game: Menebak Angka
import random
secret_num = random.randint(1, 10)
tebakan = 0

while tebakan != secret_num:
    tebakan = int(input("Masukkan angka "))

    if tebakan < secret_num:
        print("Terlalu kecil")
    elif tebakan > secret_num:
        print("Terlalu Besar")
    else:
        print(f"Congrats!! Hasil angka tebakan adalah {tebakan}")


print()

