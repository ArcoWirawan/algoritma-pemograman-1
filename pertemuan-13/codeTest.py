# 8. Menampilkan Deret Fibonacci
a, b = 0, 1 # 2 variabel dan value dipisahkan dengan koma
count = 0
while count < 10: # selama count kurang dari 10
    print(a) # tampilkan deret f
    a, b = b, a + b
    count += 1
print()