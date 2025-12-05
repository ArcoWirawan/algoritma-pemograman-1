# 1. faktorial rekursif 
def Faktorial_rekursif(n):
    if n ==0 or n == 1:
        return 1
    return n * Faktorial_rekursif(n - 1)

print("1. Faktorial rekursif")
print(f"Faktorial 5 = {Faktorial_rekursif(5)}") # 5 . 4 . 3 . 2 . 1 = 120

# 2. Fibonnaci sequence
def Fibonnaci(s):
    if s <= 1:
        return s
    else:
        # rumus fibonnaci = suku sebelumnya + suku dua sebelumnya
        return Fibonnaci(s - 1) + Fibonnaci(s - 2) 
    
print("\n2. Fibonnaci sequence")
print(f"Fibonnaci 7 = {Fibonnaci(7)}")


# 3. Jumlah angka 1 hingga n
def Pangkat(Angka, Eksponen):
    if Eksponen == 0: # jika pangkat = 0 
        return 1 # hasilnuya akan 1 
    return Angka * Pangkat(Angka, Eksponen - 1)

print(Pangkat(10, 2)) # 10 x 10 = 100

