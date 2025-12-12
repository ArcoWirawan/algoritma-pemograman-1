#1. no parameter function
def Hi():
    print("Hai, sayang")
    
print("1. fungsi tanpa parameter")
Hi() # cara memanggil function


# 2. Fungsi dengan satu parameter
def Sapa(name):
    print(f"Halo, {name}")
    
print("\n2. Fungsi dengan satu parameter")
Sapa("aarwannzxp")

# 3. Fungsi dengan dua parameter
def Addtion(a,b):
    print(f"{a} + {b} = {a + b}")
    
print("\n3. Fungsi dengan dua parameter")
Addtion(7,11)

# 4. Fungsi dengan return value
def Kali(a,b):
    return f"{a} x {b} = {a * b}"

print("\n4. Fungsi dengan return value")
print(Kali(11, 12))

# ditampung dalam variabel
result = Kali(10, 2)
print(f"Hasil kali = {result}")

# 5. Fungsi dengan parameter default
def Sapa_With_Time(name, time="Pagi"):
    print(f"Halo {name}, Selamat {time}")
    
print()
Sapa_With_Time("aarwannz")
Sapa_With_Time("Budi", "Siang")
    
