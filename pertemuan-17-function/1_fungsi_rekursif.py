## ngerti sih sebenernya fungsi, tapi gua coba

"""
Fungsi Rekursif = fungsi yang akan terus berulang


"""

## kalian tau kan soal MTK (3! = 3 x 2 x 1)
## itulah faktorial


def faktorial(n):
   if n == 0:          # Base case
       return 1
   else:
       return n * faktorial(n-1)  # Recursive call

# Contoh penggunaan
print(faktorial(5))  # Output: 120