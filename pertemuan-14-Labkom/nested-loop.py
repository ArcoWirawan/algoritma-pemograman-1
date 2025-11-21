import os
os.system("clear")


## Nested Loop ##

# 1. Bintang segitiga
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()
    
# 2. Tabel perkalian
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()

# 3. Segitiga Terbalik
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()    
    
# 4. Persegi 5x5
for x in range(5):
    for y in range(5):
        print("*", end="")
    print()
    
    
# 5. Pola angka naik
for x in range(1, 6): # akan berjalan 
    for y in range(1, x + 1):
        print(y, end="")
    print()
  
  
 